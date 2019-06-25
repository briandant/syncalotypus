"""Settings to configure the application."""

from os import environ

from dotenv import load_dotenv
load_dotenv(verbose=True)


# OR, explicitly providing path to '.env'
# from pathlib import Path  # python3 only
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

def _fix_booleans(var):
    FALSIES = ['False', 'false', '0', 0, 'No', 'no']
    TRUTHIES = ['True', 'true', '1', 1, 'Yes', 'yes']

    if var in FALSIES:
        return False
    if var in TRUTHIES:
        return True
    else:
        return var


def get_env_variable(var_name, default=None):
    """ Get the environment variable or return exception """
    if default is not None:
        return _fix_booleans(environ.get(var_name, default))
    try:
        return _fix_booleans(environ[var_name])
    except KeyError:
        error_msg = "Please set the %s environment variable" % var_name
        raise KeyError(error_msg)


CONFIG_FILE = get_env_variable('SYNCALOTYPUS_CONFIG_FILE', '~/.syncalotypus.yaml')
