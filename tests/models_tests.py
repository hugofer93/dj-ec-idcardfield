import pytest

from tests.sample_app.models import (
    MandatoryIdcard,
    MandatoryIdcardOrRUC,
    MandatoryRUC,
    OptionalIdcard,
    OptionalIdcardOrRUC,
    OptionalRUC,
)
from tests.sample_app.values import VALID_IDCARD, VALID_RUC


# IDCARD FIELD

@pytest.mark.django_db()
def test_mandatory_idcard():
    obj = MandatoryIdcard.objects.create(idcard=VALID_IDCARD)
    assert obj.idcard == VALID_IDCARD


@pytest.mark.django_db()
def test_optional_idcard():
    obj = OptionalIdcard.objects.create()
    assert obj.idcard == ''


# RUC FIELD

@pytest.mark.django_db()
def test_mandatory_ruc():
    obj = MandatoryRUC.objects.create(ruc=VALID_RUC)
    assert obj.ruc == VALID_RUC


@pytest.mark.django_db()
def test_optional_ruc():
    obj = OptionalRUC.objects.create()
    assert obj.ruc == ''


# IDCARD OR RUC FIELD

@pytest.mark.django_db()
def test_mandatory_idcard_or_ruc():
    obj = MandatoryIdcardOrRUC.objects.create(idcard_or_ruc=VALID_IDCARD)
    assert obj.idcard_or_ruc == VALID_IDCARD
    obj = MandatoryIdcardOrRUC.objects.create(idcard_or_ruc=VALID_RUC)
    assert obj.idcard_or_ruc == VALID_RUC


@pytest.mark.django_db()
def test_optional_idcard_or_ruc():
    obj = OptionalIdcardOrRUC.objects.create()
    assert obj.idcard_or_ruc == ''
