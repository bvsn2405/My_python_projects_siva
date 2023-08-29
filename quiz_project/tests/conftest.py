import pytest
from django.core.management import call_command


@pytest.fixture(autouse=True)
def enable_db_reset():
    """
    Custom fixture to reset the database before each test.
    """
    call_command('flush', interactive=False, verbosity=0)
