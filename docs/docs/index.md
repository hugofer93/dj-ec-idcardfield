# django-ec-idcardfield

An Idcard and RUC field for Ecuador for Django Models, Forms, and Serializers.


## Installation

It requires Python 3.6.1+ and Django 2.2+ to run.

`pip install django-ec-idcardfield`


## Usage

### Settings

First, add `'ec_idcardfield'` to your `INSTALLED_APPS` in `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'ec_idcardfield',
    ...
]
```

### Models

```python
from django.db.models import Model

from ec_idcardfield.models import IdcardField, IdcardOrRUCField, RUCField


class MandatoryIdcard(Model):
    idcard = IdcardField()


class OptionalIdcard(Model):
    idcard = IdcardField(blank=True, default='')


class MandatoryRUC(Model):
    ruc = RUCField()


class OptionalRUC(Model):
    ruc = RUCField(blank=True, default='')


class MandatoryIdcardOrRUC(Model):
    idcard_or_ruc = IdcardOrRUCField()


class OptionalIdcardOrRUC(Model):
    idcard_or_ruc = IdcardOrRUCField(blank=True, default='')
```

### Forms

```python
from django.forms import Form

from ec_idcardfield.forms import IdcardField, IdcardOrRUCField, RUCField


class MandatoryIdcardForm(Form):
    idcard = IdcardField()


class OptionalIdcardForm(Form):
    idcard = IdcardField(required=False)


class MandatoryRUCForm(Form):
    ruc = RUCField()


class OptionalRUCForm(Form):
    ruc = RUCField(required=False)


class MandatoryIdcardOrRUCForm(Form):
    idcard_or_ruc = IdcardOrRUCField()


class OptionalIdcardOrRUCForm(Form):
    idcard_or_ruc = IdcardOrRUCField(required=False)
```

### Serializers

Before using Serializer fields, you must install Django REST Framework 3.9.3+:

`pip install djangorestframework`


```python
from rest_framework.serializers import Serializer

from ec_idcardfield.serializers import IdcardField, IdcardOrRUCField, RUCField


class MandatoryIdcardSerializer(Serializer):
    idcard = IdcardField()


class OptionalIdcardSerializer(Serializer):
    idcard = IdcardField(required=False, allow_blank=True)


class MandatoryRUCSerializer(Serializer):
    ruc = RUCField()


class OptionalRUCSerializer(Serializer):
    ruc = RUCField(required=False, allow_blank=True)


class MandatoryIdcardOrRUCSerializer(Serializer):
    idcard_or_ruc = IdcardOrRUCField()


class OptionalIdcardOrRUCSerializer(Serializer):
    idcard_or_ruc = IdcardOrRUCField(required=False, allow_blank=True)
```


## Testing

```bash
# clone repository
git clone https://github.com/hugofer93/django-ec-idcardfield/

# up service with Docker
docker-compose up -d

# run tests
docker-compose exec idcardfield poetry run pytest

# if you want to test compat with others versions
docker-compose exec idcardfield poetry run tox
```


## License
Released under __MIT License__.
