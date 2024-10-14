from django.forms import ModelForm

from dj_ec_idcardfield.forms import (
    IdcardField as FormIdcardField,
    IdcardOrRUCField as FormIdcardOrRUCField,
    RUCField as FormRUCField,
)
from tests.sample_app.forms import (
    MandatoryIdcardForm,
    OptionalIdcardForm,
    MandatoryIdcardOrRUCForm,
    OptionalIdcardOrRUCForm,
    MandatoryRUCForm,
    OptionalRUCForm,
)
from tests.sample_app.models import (
    MandatoryIdcard,
    MandatoryIdcardOrRUC,
    MandatoryRUC,
    OptionalIdcard,
    OptionalIdcardOrRUC,
    OptionalRUC,
)
from tests.sample_app.values import (
    INCORRECT_IDCARD,
    INCORRECT_RUC,
    VALID_IDCARD,
    VALID_RUC,
)


# IDCARD FIELD

def test_valid_idcard_form():
    data = {'idcard': VALID_IDCARD}
    form = MandatoryIdcardForm(data)
    assert form.is_valid()
    assert form.cleaned_data.get('idcard') == VALID_IDCARD
    assert not form.errors


def test_invalid_idcard_form():
    data = {'idcard': INCORRECT_IDCARD}
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
    data = {'ruc': INCORRECT_RUC}
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
    data = {'idcard_or_ruc': INCORRECT_RUC}
    form = MandatoryIdcardOrRUCForm(data)
    assert not form.is_valid()
    assert form.errors

    data = {'idcard_or_ruc': INCORRECT_IDCARD}
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


# IDCARD FORM FIELD FROM MODELFORM

def test_idcard_form_from_model():
    class MandatoryIdcardModelForm(ModelForm):
        class Meta:
            model = MandatoryIdcard
            fields = '__all__'

    modelform = MandatoryIdcardModelForm()
    modelform_field = list(modelform.fields.values())[0]
    assert type(modelform_field) == FormIdcardField
    assert modelform_field.required == True


def test_optional_idcard_form_from_model():
    class OptionalIdcardModelForm(ModelForm):
        class Meta:
            model = OptionalIdcard
            fields = '__all__'

    modelform = OptionalIdcardModelForm()
    modelform_field = list(modelform.fields.values())[0]
    assert type(modelform_field) == FormIdcardField
    assert modelform_field.required == False


# RUC FORM FIELD FROM MODELFORM

def test_ruc_form_from_model():
    class MandatoryRUCModelForm(ModelForm):
        class Meta:
            model = MandatoryRUC
            fields = '__all__'

    modelform = MandatoryRUCModelForm()
    modelform_field = list(modelform.fields.values())[0]
    assert type(modelform_field) == FormRUCField
    assert modelform_field.required == True


def test_optional_ruc_form_from_model():
    class OptionalRUCModelForm(ModelForm):
        class Meta:
            model = OptionalRUC
            fields = '__all__'

    modelform = OptionalRUCModelForm()
    modelform_field = list(modelform.fields.values())[0]
    assert type(modelform_field) == FormRUCField
    assert modelform_field.required == False


# IDCARD OR RUC FORM FIELD FROM MODELFORM

def test_idcard_or_ruc_form_from_model():
    class MandatoryIdcardOrRUCModelForm(ModelForm):
        class Meta:
            model = MandatoryIdcardOrRUC
            fields = '__all__'

    modelform = MandatoryIdcardOrRUCModelForm()
    modelform_field = list(modelform.fields.values())[0]
    assert type(modelform_field) == FormIdcardOrRUCField
    assert modelform_field.required == True


def test_optional_idcard_or_ruc_form_from_model():
    class OptionalIdcardOrRUCModelForm(ModelForm):
        class Meta:
            model = OptionalIdcardOrRUC
            fields = '__all__'

    modelform = OptionalIdcardOrRUCModelForm()
    modelform_field = list(modelform.fields.values())[0]
    assert type(modelform_field) == FormIdcardOrRUCField
    assert modelform_field.required == False
