import pytest
from src.channel import Channel


@pytest.fixture
def channel_1():
    return Channel('12345')


def test_channel_init(channel_1):
    assert channel_1.channel_id == '12345'
