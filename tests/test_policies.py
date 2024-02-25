import pytest

from lerobot.common.policies.factory import make_policy

from .utils import init_config


@pytest.mark.parametrize(
    "env_name",
    [
        "simxarm",
        "pusht",
    ],
)
def test_factory(env_name):
    cfg = init_config(overrides=[f"env={env_name}"])
    policy = make_policy(cfg)
