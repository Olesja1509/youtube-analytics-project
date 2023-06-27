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

        self.channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        self.channel_items = self.channel['items']
        self.channel_snippet = self.channel_items[0]['snippet']
        self.statistics = self.channel_items[0]['statistics']

        self.title = self.channel_snippet['title']
        self.description = self.channel_snippet['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscriber_count = self.statistics['subscriberCount']
        self.video_count = self.statistics['videoCount']
        self.view_count = self.statistics['viewCount']

    def __str__(self):
        return f'{self.title} ({self.url})'

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @classmethod
    def get_service(cls):
        """класс-метод get_service(),возвращающий объект для работы с YouTube API"""
        return cls.youtube

    def __add__(self, other):
        """метод для операции сложения"""
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """метод для операции вычитания"""
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __gt__(self, other):
        """метод для операции сравнения «больше»"""
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        """метод для операции сравнения «больше или равно»"""
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def __lt__(self, other):
        """метод для операции сравнения «меньше»"""
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        """метод для операции сравнения «меньше или равно»"""
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __eq__(self, other):
        """метод для определения равенства"""
        return int(self.subscriber_count) == int(other.subscriber_count)

    def to_json(self, file_name):
        """метод, сохраняющий в файл значения атрибутов экземпляра Channel"""
        channel_info = {'channel_id': self.__channel_id, 'title': self.title, 'description': self.description,
                        'url': self.url, 'subscriber_count': self.subscriber_count,
                        'video_count': self.video_count, 'view_count': self.view_count}

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(json.dumps(channel_info, indent=2, ensure_ascii=False))
