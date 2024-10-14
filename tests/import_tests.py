from importlib import import_module, reload as reload_module
from sys import modules as sys_modules
from types import ModuleType

import pytest
from pytest_mock import MockerFixture


def get_code_from_module(module_path: ModuleType) -> str:
    """Get code from a module.

    Args:
        module_path (ModuleType): Module Python Path.

    Returns:
        str: Python Module Code.
    """
    module = reload_module(module_path)
    module_loader = module.__loader__
    module_name = module.__name__
    module_code = module_loader.get_source(module_name)
    return module_code


def test_compatible_django_version(mocker: MockerFixture) -> None:
    package_name = 'dj_ec_idcardfield'
    del sys_modules[package_name]
    import_module(package_name)
    from dj_ec_idcardfield import DJANGO_MIN_VERSION
    assert DJANGO_MIN_VERSION


def test_incompatible_django_version(mocker: MockerFixture) -> None:
    import dj_ec_idcardfield
    from dj_ec_idcardfield import DJANGO_MIN_VERSION

    module_init_code = get_code_from_module(dj_ec_idcardfield)
    DJANGO_VERSION_INCOMPATIBLE = str(float(DJANGO_MIN_VERSION) - 0.1)

    mocker.patch(
        'django.utils.version.get_docs_version',
        return_value=DJANGO_VERSION_INCOMPATIBLE)
    with pytest.raises(ImportError, match=DJANGO_VERSION_INCOMPATIBLE):
        exec(module_init_code)


def test_import_without_django(mocker: MockerFixture) -> None:
    import dj_ec_idcardfield

    package_name = 'django'
    error_message = f"No module named '{package_name}'"
    module_init_code = get_code_from_module(dj_ec_idcardfield)

    mocker.patch(
        'django.utils.version.get_docs_version',
        side_effect=ModuleNotFoundError(error_message))
    with pytest.raises(ModuleNotFoundError, match=error_message):
        exec(module_init_code)

    import_module('django.utils.version')


def test_compatible_drf_version(mocker: MockerFixture) -> None:
    package_name = 'dj_ec_idcardfield'
    del sys_modules[package_name]
    import_module('dj_ec_idcardfield.serializers')
    from dj_ec_idcardfield import DRF_MIN_VERSION
    assert  DRF_MIN_VERSION


def test_incompatible_drf_version(mocker: MockerFixture) -> None:
    import rest_framework

    from dj_ec_idcardfield import (
        DRF_MIN_VERSION,
        serializers as serialzers_module,
    )

    module_code = get_code_from_module(serialzers_module)
    DRF_VERSION_INCOMPATIBLE = str(float(DRF_MIN_VERSION) - 0.1)
    package_name = 'rest_framework'

    class DRFMock:
        __version__ = DRF_VERSION_INCOMPATIBLE

    mocker.patch.dict(sys_modules, {package_name: DRFMock()})

    mocker.patch.object(
        rest_framework,
        '__version__',
        DRF_VERSION_INCOMPATIBLE)
    with pytest.raises(ImportError, match=DRF_VERSION_INCOMPATIBLE):
        exec(module_code)


def test_import_without_drf(mocker: MockerFixture) -> None:
    from dj_ec_idcardfield import serializers as serialzers_module

    module_code = get_code_from_module(serialzers_module)
    package_name = 'rest_framework'
    error_message = "No module named 'rest_framework'"

    class DRFMock:
        def __getattribute__(self, name):
            raise ModuleNotFoundError(error_message)

    mocker.patch.dict(sys_modules, {package_name: DRFMock()})
    with pytest.raises(ModuleNotFoundError, match=error_message):
        exec(module_code)

    # * RELOAD IMPORT OF `rest_framework` MODULE FOR OTHER TESTS.
    package_name = 'rest_framework'
    del sys_modules[package_name]
    import_module(package_name)
