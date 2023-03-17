from django.forms import Form

from dj_ec_idcardfield.forms import IdcardField, IdcardOrRUCField, RUCField


# IDCARD FIELD

class MandatoryIdcardForm(Form):
    idcard = IdcardField()


class OptionalIdcardForm(Form):
    idcard = IdcardField(required=False)


# RUC FIELD

class MandatoryRUCForm(Form):
    ruc = RUCField()


class OptionalRUCForm(Form):
    ruc = RUCField(required=False)


# IDCARD OR RUC FIELD

class MandatoryIdcardOrRUCForm(Form):
    idcard_or_ruc = IdcardOrRUCField()


class OptionalIdcardOrRUCForm(Form):
    idcard_or_ruc = IdcardOrRUCField(required=False)
