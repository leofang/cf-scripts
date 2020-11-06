import os

import pytest
from conda_forge_tick import global_sensitive_env


@pytest.fixture
def env_setup():
    old_pwd = os.environ.pop("PASSWORD", None)
    os.environ["PASSWORD"] = os.environ.get("TEST_PASSWORD_VAL", "unpassword")
    old_pwd2 = os.environ.pop("pwd", None)
    os.environ["pwd"] = "pwd"
    if "TEST_PASSWORD_VAL" not in os.environ:
        global_sensitive_env.hide_env_vars()
    yield
    if "TEST_PASSWORD_VAL" not in os.environ:
        global_sensitive_env.reveal_env_vars()
    if old_pwd:
        os.environ["PASSWORD"] = old_pwd
    if old_pwd2:
        os.environ["pwd"] = old_pwd2
