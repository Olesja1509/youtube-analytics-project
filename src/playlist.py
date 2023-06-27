import json
import os
from datetime import timedelta
import operator

from googleapiclient.discovery import build
from pytube import Playlist, YouTube, extract


class PlayList:
    """Класс для плей-листа ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id) -> None:
        super().__init__()
        self.__playlist_id = playlist_id

        self.playlist = self.youtube.playlists().list(id=self.__playlist_id, part='snippet').execute()
        self.playlist_items = self.playlist['items']
        self.playlist_snippet = self.playlist_items[0]['snippet']

        self.title = self.playlist_snippet['title']
        self.url = 'https://www.youtube.com/playlist?list=' + self.__playlist_id

    @property
    def playlist_id(self):
        return self.__playlist_id

    def print_info(self):
        """Выводит в консоль информацию о плей-листе"""
        print(json.dumps(self.playlist, indent=2, ensure_ascii=False))

    @property
    def total_duration(self):
        """Возвращает суммарную длительность плей-листа в формате datetime.timedelta"""
        sec = 0
        link = Playlist(self.url)
        for i in link.video_urls:
            video_length = YouTube(i).length
            sec += video_length
        duration = timedelta(seconds=sec)
        return duration

    def show_best_video(self):
        """возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""

        dict_video = {}

        link = Playlist(self.url)
        for i in link.video_urls:
            video_id = extract.video_id(i)
            video = self.youtube.videos().list(id=video_id, part='statistics').execute()
            video_items = video['items']
            statistics = video_items[0]['statistics']

            like_count = statistics['likeCount']
            dict_video['https://youtu.be/' + video_id] = like_count

        max_value = max(dict_video.items(), key=operator.itemgetter(1))
        return max_value[0]
