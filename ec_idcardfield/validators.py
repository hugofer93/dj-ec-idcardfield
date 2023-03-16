from re import compile as re_compile

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.regex_helper import _lazy_re_compile
from django.utils.translation import gettext_lazy as _


class IdcardValidator(RegexValidator):
    NUMBER_DIGITS = 10
    NATURAL_PERSONS = 1
    PUBLIC_RUC = 2  # state company
    LEGAL_PERSONS = 3
    FOREIGNERS_WITHOUT_IDCARD = LEGAL_PERSONS
    idcard_regex = r'^[0-2]{1}[0-9]{9}'
    regex = re_compile(idcard_regex + '$')
    message = _('Enter a valid number.')
    code = 'invalid'

    def __call__(self, value):
        super().__call__(value)
        self.common_validator(value)

    def get_persons_type(self):
        """Get a tuple with the persons list.

        Returns:
            tuple: List of persons types.
        """
        persons_type = (
            self.NATURAL_PERSONS,
            self.PUBLIC_RUC,
            self.LEGAL_PERSONS,
            self.FOREIGNERS_WITHOUT_IDCARD,
        )
        return persons_type

    def common_validator(self, value):
        """Common validator for Idcards and R.U.C.

        Args:
            value (str): Idcard number or R.U.C.

        Raises:
            ValidationError: Province code and/or Person type are incorrect.
        """
        person_type = None
        province_code = int(value[0:2])
        # There are only 24 provinces in Ecuador
        if 0 <= province_code <= 24:
            third_digit = int(value[2])
            # third digit indicates the person type
            if 0 <= third_digit < 6:
                person_type = self.NATURAL_PERSONS
            elif third_digit == 6:
                person_type = self.PUBLIC_RUC
            elif third_digit == 9:
                # Legal persons and foreigners without idcard
                # have the same validation pattern
                person_type = self.LEGAL_PERSONS
        if person_type:
            return self.core_validator(value, person_type)
        raise ValidationError(self.message, code=self.code,
                              params={'value': value})

    def core_validator(self, value, person_type):
        """Core validator for Idcards and R.U.C.

        Args:
            value (str): Idcard number or R.U.C.
            person_type (int): Person type.

        Raises:
            ValidationError: Has 13 digits and the last 3 digits are '000'
            ValidationError: If the check digit is incorrect.
        """
        ndigits = len(value)
        # if is RUC, check that the last 3 digits are greater than 0
        if ndigits == 13 and int(value[-3:]) < 1:
            raise ValidationError(self.message, code=self.code,
                                  params={'value': value})
        assert isinstance(person_type, int)
        assert person_type in self.get_persons_type()

        # for natural persons
        if person_type == self.NATURAL_PERSONS:
            base = 10
            check_digit = int(value[9])
            coefficients = (2, 1, 2, 1, 2, 1, 2, 1, 2)
        # for public R.U.C.
        elif person_type == self.PUBLIC_RUC:
            base = 11
            check_digit = int(value[8])
            coefficients = (3, 2, 7, 6, 5, 4, 3, 2)
        # for legal persons or foreigners without idcard
        elif (person_type == self.LEGAL_PERSONS
                or person_type == self.FOREIGNERS_WITHOUT_IDCARD):
            base = 11
            check_digit = int(value[9])
            coefficients = (4, 3, 2, 7, 6, 5, 4, 3, 2)

        total = 0
        for index in range(0, len(coefficients)):
            result = int(value[index]) * coefficients[index]
            if person_type == self.NATURAL_PERSONS:
                if result < 10:
                    total += result
                else:
                    total += int(str(result)[0]) + int(str(result)[1])
            else:
                total += result

        mod = total % base
        value = base - mod if mod != 0 else 0
        if value != check_digit:
            raise ValidationError(self.message, code=self.code,
                                  params={'value': value})


class RUCValidator(IdcardValidator):
    NUMBER_DIGITS = 13
    ruc_regex = IdcardValidator.idcard_regex + '[0-2]{1}[0-9]{2}'
    regex = re_compile(ruc_regex + '$')


class IdcardOrRUCValidator(RUCValidator):
    def __call__(self, value):
        self.set_regex(value)
        RegexValidator.__call__(self, value)
        self.common_validator(value)

    def set_regex(self, value):
        """Change the regex if the value is Idcard.

        Args:
            value (str): Idcard number or R.U.C.
        """
        if len(value) == IdcardValidator.NUMBER_DIGITS:
            regex = IdcardValidator.regex
        else:
            regex = RUCValidator.regex
        self.regex = _lazy_re_compile(regex, self.flags)


validate_idcard = IdcardValidator()

validate_ruc = RUCValidator()

validate_idcard_or_ruc = IdcardOrRUCValidator()
