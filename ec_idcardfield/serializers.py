try:
    from rest_framework.serializers import CharField
except ImportError:
    ModuleNotFoundError('django rest framework is not installed')

from ec_idcardfield.validators import (
    validate_idcard,
    validate_idcard_or_ruc,
    validate_ruc,
)


class IdcardField(CharField):
    default_error_messages = {'invalid': validate_idcard.message}

    def to_internal_value(self, data):
        validate_idcard(data)
        return data


class RUCField(CharField):
    default_error_messages = {'invalid': validate_ruc.message}

    def to_internal_value(self, data):
        validate_ruc(data)
        return data


class IdcardOrRUCField(IdcardField, RUCField):
    default_error_messages = {'invalid': validate_idcard_or_ruc.message}

    def to_internal_value(self, data):
        validate_idcard_or_ruc(data)
        return data
