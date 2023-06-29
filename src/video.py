import json
import os

from googleapiclient.discovery import build


class Video:
    """Класс для видео ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id) -> None:
        self.__video_id = video_id

        try:
            self.video = self.youtube.videos().list(id=self.__video_id, part='snippet,statistics').execute()
            self.video_items = self.video['items']
            self.video_snippet = self.video_items[0]['snippet']
            self.statistics = self.video_items[0]['statistics']

            self.title = self.video_snippet['title']
            self.url = 'https://www.youtube.com/watch?v=' + self.__video_id
            self.view_count = self.statistics['viewCount']
            self.like_count = self.statistics['likeCount']

        except IndexError:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    @property
    def video_id(self):
        return self.__video_id

    def __str__(self):
        return self.title

    def print_info(self):
        """Выводит в консоль информацию о видео"""
        print(json.dumps(self.video, indent=2, ensure_ascii=False))


class PLVideo(Video):
    def __init__(self, video_id, playlist_id) -> None:
        super().__init__(video_id)
        self.__playlist_id = playlist_id

    @property
    def playlist_id(self):
        return self.__playlist_id
