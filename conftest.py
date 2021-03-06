"""
Configures the test suite and describe the global fixture that can be used
in functional tests.

"""
import pytest
import shutil
from open_cobol_ide import __version__
from open_cobol_ide.app import Application
from open_cobol_ide.logger import setup_logging
from open_cobol_ide.settings import Settings

setup_logging(__version__, debug=True)

_app = None


try:
    shutil.rmtree('test/testfiles/bin')
except OSError:
    pass


@pytest.fixture(scope="session")
def app(request):
    global _app
    # always starts with default settings
    s = Settings()
    s.clear()
    s.perspective = 'default'
    _app = Application(parse_args=False)

    def fin():
        global _app
        _app.exit()
        del _app

    # _app.win.hide()
    request.addfinalizer(fin)
    return _app
