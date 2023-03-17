__version__ = '0.1.0'

try:
    from django.utils.version import get_docs_version
    django_version = get_docs_version()
    if float(django_version) < 2.2:
        error_msg = f'django version {django_version} not supported.'
        print(ImportError(error_msg))
        exit()
except ImportError:
    print('django is not installed')
