from tests.sample_app.forms import (
    MandatoryIdcardForm,
    OptionalIdcardForm,
    MandatoryIdcardOrRUCForm,
    OptionalIdcardOrRUCForm,
    MandatoryRUCForm,
    OptionalRUCForm,
)
from tests.sample_app.values import (
    INVALID_IDCARD,
    INVALID_RUC,
    VALID_IDCARD, VALID_RUC,
)


# IDCARD FIELD

def test_valid_idcard_form():
    data = {'idcard': VALID_IDCARD}
    form = MandatoryIdcardForm(data)
    assert form.is_valid()
    assert form.cleaned_data.get('idcard') == VALID_IDCARD
    assert not form.errors


def test_invalid_idcard_form():
    data = {'idcard': INVALID_IDCARD}
    form = MandatoryIdcardForm(data)
    assert not form.is_valid()
    assert form.errors


def test_optional_idcard_form():
    data = {'idcard': ''}
    form = OptionalIdcardForm(data)
    assert form.is_valid()
    assert form.cleaned_data.get('idcard') == ''
    assert not form.errors


# RUC FIELD

def test_valid_ruc_form():
    data = {'ruc': VALID_RUC}
    form = MandatoryRUCForm(data)
    assert form.is_valid()
    assert form.cleaned_data.get('ruc') == VALID_RUC
    assert not form.errors


def test_invalid_ruc_form():
    data = {'ruc': INVALID_RUC}
    form = MandatoryRUCForm(data)
    assert not form.is_valid()
    assert form.errors


def test_optional_ruc_form():
    data = {'ruc': ''}
    form = OptionalRUCForm(data)
    assert form.is_valid()
    assert form.cleaned_data.get('ruc') == ''
    assert not form.errors


# IDCARD OR RUC FIELD

def test_valid_idcard_or_ruc_form():
    data = {'idcard_or_ruc': VALID_RUC}
    form = MandatoryIdcardOrRUCForm(data)
    assert form.is_valid()
    assert form.cleaned_data.get('idcard_or_ruc') == VALID_RUC
    assert not form.errors

    data = {'idcard_or_ruc': VALID_IDCARD}
    form = MandatoryIdcardOrRUCForm(data)
    assert form.is_valid()
    assert form.cleaned_data.get('idcard_or_ruc') == VALID_IDCARD
    assert not form.errors


def test_invalid_idcard_or_ruc_form():
    data = {'idcard_or_ruc': INVALID_RUC}
    form = MandatoryIdcardOrRUCForm(data)
    assert not form.is_valid()
    assert form.errors

    data = {'idcard_or_ruc': INVALID_IDCARD}
    form = MandatoryIdcardOrRUCForm(data)
    assert not form.is_valid()
    assert form.errors


def test_optional_idcard_or_ruc_form():
    data = {'idcard_or_ruc': ''}
    form = OptionalIdcardOrRUCForm(data)
    assert form.is_valid()
    assert form.cleaned_data.get('idcard_or_ruc') == ''
    assert not form.errors

    data = {'idcard_or_ruc': ''}
    form = OptionalIdcardOrRUCForm(data)
    assert form.is_valid()
    assert form.cleaned_data.get('idcard_or_ruc') == ''
    assert not form.errors
