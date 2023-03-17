from rest_framework.serializers import Serializer

from dj_ec_idcardfield.serializers import (
    IdcardField,
    IdcardOrRUCField,
    RUCField,
)


# IDCARD FIELD

class MandatoryIdcardSerializer(Serializer):
    idcard = IdcardField()


class OptionalIdcardSerializer(Serializer):
    idcard = IdcardField(required=False, allow_blank=True)


# RUC FIELD

class MandatoryRUCSerializer(Serializer):
    ruc = RUCField()


class OptionalRUCSerializer(Serializer):
    ruc = RUCField(required=False, allow_blank=True)


# IDCARD OR RUC FIELD

class MandatoryIdcardOrRUCSerializer(Serializer):
    idcard_or_ruc = IdcardOrRUCField()


class OptionalIdcardOrRUCSerializer(Serializer):
    idcard_or_ruc = IdcardOrRUCField(required=False, allow_blank=True)
