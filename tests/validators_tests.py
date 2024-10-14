import pytest

from django.core.exceptions import ValidationError

from dj_ec_idcardfield.validators import (
    validate_idcard,
    validate_idcard_or_ruc,
    validate_ruc,
)
from tests.sample_app.values import (
    EXTRA_NUMBER_IDCARD,
    EXTRA_NUMBER_RUC,
    INCOMPLETE_IDCARD,
    INCOMPLETE_RUC,
    INCORRECT_IDCARD,
    INCORRECT_RUC,
    VALID_IDCARD,
    VALID_RUC,
)


# IDCARD FIELD

def test_valid_idcard():
    assert validate_idcard(VALID_IDCARD) is None


def test_incorrect_idcard():
    with pytest.raises(ValidationError):
        validate_idcard(INCORRECT_IDCARD)


def test_incomplete_idcard():
    with pytest.raises(ValidationError):
        validate_idcard(INCOMPLETE_IDCARD)


def test_extra_number_idcard():
    with pytest.raises(ValidationError):
        validate_idcard(EXTRA_NUMBER_IDCARD)


# RUC FIELD

def test_valid_ruc():
    assert validate_ruc(VALID_RUC) is None


def test_incorrect_ruc():
    with pytest.raises(ValidationError):
        validate_idcard(INCORRECT_RUC)


def test_incomplete_ruc():
    with pytest.raises(ValidationError):
        validate_ruc(INCOMPLETE_RUC)


def test_extra_number_ruc():
    with pytest.raises(ValidationError):
        validate_ruc(EXTRA_NUMBER_RUC)


# check if you can reuse the validator,
# this implies constantly changing the regex in the validator.
@pytest.mark.parametrize(
    'value',
    [VALID_IDCARD, VALID_RUC, VALID_IDCARD, VALID_RUC])
def test_valid_idcard_or_ruc(value):
    assert validate_idcard_or_ruc(value) is None
    assert validate_idcard_or_ruc(VALID_RUC) is None
    assert validate_idcard_or_ruc(VALID_IDCARD) is None


# check if you can reuse the validator,
# this implies constantly changing the regex in the validator.
@pytest.mark.parametrize(
    'value',
    [INCORRECT_IDCARD, INCOMPLETE_IDCARD, EXTRA_NUMBER_IDCARD,
     INCORRECT_RUC, INCOMPLETE_RUC, EXTRA_NUMBER_RUC])
def test_invalid_idcard_or_ruc(value):
    with pytest.raises(ValidationError):
        validate_idcard_or_ruc(value)
    with pytest.raises(ValidationError):
        validate_idcard_or_ruc(INCOMPLETE_RUC)
    with pytest.raises(ValidationError):
        validate_idcard_or_ruc(INCOMPLETE_IDCARD)
