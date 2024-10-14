from tests.sample_app.serializers import (
    MandatoryIdcardSerializer,
    MandatoryIdcardOrRUCSerializer,
    MandatoryRUCSerializer,
    OptionalIdcardSerializer,
    OptionalIdcardOrRUCSerializer,
    OptionalRUCSerializer,
)
from tests.sample_app.values import (
    INCORRECT_IDCARD,
    INCORRECT_RUC,
    VALID_IDCARD,
    VALID_RUC,
)


# IDCARD FIELD

def test_valid_idcard_serializer():
    data = {'idcard': VALID_IDCARD}
    serializer = MandatoryIdcardSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.data.get('idcard') == VALID_IDCARD
    assert not serializer.errors


def test_invalid_idcard_serializer():
    data = {'idcard': INCORRECT_IDCARD}
    serializer = MandatoryIdcardSerializer(data=data)
    assert not serializer.is_valid()
    assert serializer.errors


def test_optional_idcard_serializer():
    data = {'idcard': ''}
    serializer = OptionalIdcardSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.data.get('idcard') == ''
    assert not serializer.errors


# RUC FIELD

def test_valid_ruc_serializer():
    data = {'ruc': VALID_RUC}
    serializer = MandatoryRUCSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.data.get('ruc') == VALID_RUC
    assert not serializer.errors


def test_invalid_ruc_serializer():
    data = {'ruc': INCORRECT_RUC}
    serializer = MandatoryRUCSerializer(data=data)
    assert not serializer.is_valid()
    assert serializer.errors


def test_optional_ruc_serializer():
    data = {'ruc': ''}
    serializer = OptionalRUCSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.data.get('ruc') == ''
    assert not serializer.errors


# IDCARD OR RUC FIELD

def test_valid_idcard_or_ruc_serializer():
    data = {'idcard_or_ruc': VALID_IDCARD}
    serializer = MandatoryIdcardOrRUCSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.data.get('idcard_or_ruc') == VALID_IDCARD
    assert not serializer.errors

    data = {'idcard_or_ruc': VALID_RUC}
    serializer = MandatoryIdcardOrRUCSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.data.get('idcard_or_ruc') == VALID_RUC
    assert not serializer.errors


def test_invalid_idcard_or_ruc_serializer():
    data = {'idcard_or_ruc': INCORRECT_IDCARD}
    serializer = MandatoryIdcardOrRUCSerializer(data=data)
    assert not serializer.is_valid()
    assert serializer.errors

    data = {'idcard_or_ruc': INCORRECT_RUC}
    serializer = MandatoryIdcardOrRUCSerializer(data=data)
    assert not serializer.is_valid()
    assert serializer.errors


def test_optional_idcard_or_ruc_serializer():
    data = {'idcard_or_ruc': ''}
    serializer = OptionalIdcardOrRUCSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.data.get('idcard_or_ruc') == ''
    assert not serializer.errors
