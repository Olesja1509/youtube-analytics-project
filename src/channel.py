import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__title = None
        self.__description = None
        self.__url = None
        self.__subscriber_count = None
        self.__video_count = None
        self.__view_count = None

        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.channel_items = self.channel['items']
        self.channel_snippet = self.channel_items[0]['snippet']
        self.statistics = self.channel_items[0]['statistics']

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        """Возвращает название канала"""
        self.__title = self.channel_snippet['title']
        return self.__title

    @property
    def description(self):
        """Возвращает описание канала"""
        self.__description = self.channel_snippet['description']
        return self.__description

    @property
    def url(self):
        """Возвращает ссылку на канал"""
        self.__url = 'https://www.youtube.com/channel/' + self.__channel_id
        return self.__url

    @property
    def subscriber_count(self):
        """Возвращает количество подписчиков"""
        self.__subscriber_count = self.statistics['subscriberCount']
        return self.__subscriber_count

    @property
    def video_count(self):
        """Возвращает количество видео"""
        self.__video_count = self.statistics['videoCount']
        return self.__video_count

    @property
    def view_count(self):
        """Возвращает общее количество просмотров"""
        self.__view_count = self.statistics['viewCount']
        return self.__view_count

    @classmethod
    def get_service(cls):
        """класс-метод get_service(),возвращающий объект для работы с YouTube API"""
        return Channel.youtube

    def to_json(self, file_name):
        """метод, сохраняющий в файл значения атрибутов экземпляра Channel"""
        channel_info = {'channel_id': self.channel_id, 'title': self.title, 'description': self.description,
                        'url': self.url, 'subscriber_count': self.subscriber_count,
                        'video_count': self.video_count, 'view_count': self.view_count}

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(json.dumps(channel_info, indent=2, ensure_ascii=False))
