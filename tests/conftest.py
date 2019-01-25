import os, shutil
import pytest


@pytest.fixture(scope="session", autouse=True)
def initialization_and_clean_up(request):
    # nothing to do for initialization
    yield None
    # clean up
    shutil.rmtree("tests/temp")


