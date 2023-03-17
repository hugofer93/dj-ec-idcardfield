import pytest

from django.core.exceptions import ValidationError

from dj_ec_idcardfield.validators import (
    validate_idcard,
    validate_idcard_or_ruc,
    validate_ruc,
)
from tests.sample_app.values import (
    INCOMPLETE_IDCARD,
    INCOMPLETE_RUC,
    INCORRECT_IDCARD,
    INCORRECT_RUC,
    INVALID_IDCARD,
    INVALID_RUC,
    INVALID_RUC_WITH_000,
    VALID_IDCARD, VALID_RUC,
)


# IDCARD FIELD

def test_valid_idcard():
    assert validate_idcard(VALID_IDCARD) is None


def test_incomplete_idcard():
    with pytest.raises(ValidationError):
        validate_idcard(INCOMPLETE_IDCARD)


def test_incorrect_idcard():
    with pytest.raises(ValidationError):
        validate_idcard(INCORRECT_IDCARD)


def test_invalid_idcard():
    with pytest.raises(ValidationError):
        validate_idcard(INVALID_IDCARD)


# RUC FIELD

def test_valid_ruc():
    assert validate_ruc(VALID_RUC) is None


def test_incomplete_ruc():
    with pytest.raises(ValidationError):
        validate_ruc(INCOMPLETE_RUC)


def test_incorrect_ruc():
    with pytest.raises(ValidationError):
        validate_idcard(INCORRECT_RUC)


def test_invalid_ruc():
    with pytest.raises(ValidationError):
        validate_ruc(INVALID_RUC)


def test_invalid_ruc_with_000():
    with pytest.raises(ValidationError):
        validate_ruc(INVALID_RUC_WITH_000)


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
    [INVALID_RUC_WITH_000, INVALID_IDCARD, INVALID_RUC, INVALID_IDCARD,
     INCOMPLETE_IDCARD, INCORRECT_RUC, INVALID_RUC, INCOMPLETE_IDCARD,
     INCOMPLETE_RUC])
def test_invalid_idcard_or_ruc(value):
    with pytest.raises(ValidationError):
        validate_idcard_or_ruc(value)
    with pytest.raises(ValidationError):
        validate_idcard_or_ruc(INVALID_RUC)
    with pytest.raises(ValidationError):
        validate_idcard_or_ruc(INVALID_IDCARD)
