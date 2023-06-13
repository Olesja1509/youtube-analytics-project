import pytest
import json
from src.channel import Channel


@pytest.fixture
def smeshariki():
    smeshariki = Channel("UCxaznoDkqXdpsP4H273CXRg")
    return smeshariki


def test_channel_init(smeshariki):
    assert smeshariki.channel_id == "UCxaznoDkqXdpsP4H273CXRg"
    assert smeshariki.title == "ПинКод"
    assert smeshariki.description == "В какое бы опасное путешествие ни отправились Смешарики, чтобы с ними " \
                                     "ни случилось, им всегда помогут советы Лосяша и изобретения Пина. " \
                                     "Чтобы продолжать познавать окружающий мир, Пин изобретает машину «Умнолёт», " \
                                     "способную перемещаться и по земле, и по воде, и в далёком космосе. Смешарикам " \
                                     "предстоит совершить немало открытий, услышать разнообразные научные теории " \
                                     "и пережить новые захватывающие приключения!"
    assert smeshariki.url == "https://www.youtube.com/channel/UCxaznoDkqXdpsP4H273CXRg"
    assert smeshariki.subscriber_count == "235000"
    assert smeshariki.video_count == "430"
    assert smeshariki.view_count == "176928091"


def test_to_json(smeshariki):
    channel_info = {'channel_id': smeshariki.channel_id,
                    'title': smeshariki.title,
                    'description': smeshariki.description,
                    'url': smeshariki.url,
                    'subscriber_count': smeshariki.subscriber_count,
                    'video_count': smeshariki.video_count,
                    'view_count': smeshariki.view_count}
    smeshariki.to_json('smeshariki.json')

    with open('smeshariki.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    assert data == channel_info
