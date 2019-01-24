import os, shutil
import pytest


@pytest.fixture(scope="session", autouse=True)
def my_fixture(request):
    print ('INITIALIZATION')
    yield None
    print ('TEAR DOWN')


