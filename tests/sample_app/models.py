from django.db.models import Model

from ec_idcardfield.models import IdcardField, IdcardOrRUCField, RUCField


# IDCARD FIELD

class MandatoryIdcard(Model):
    idcard = IdcardField()


class OptionalIdcard(Model):
    idcard = IdcardField(blank=True, default='')


# RUC FIELD

class MandatoryRUC(Model):
    ruc = RUCField()


class OptionalRUC(Model):
    ruc = RUCField(blank=True, default='')


# IDCARD OR RUC FIELD

class MandatoryIdcardOrRUC(Model):
    idcard_or_ruc = IdcardOrRUCField()


class OptionalIdcardOrRUC(Model):
    idcard_or_ruc = IdcardOrRUCField(blank=True, default='')
