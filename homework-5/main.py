import datetime

from src.playlist import PlayList

if __name__ == '__main__':
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')
    assert pl.title == "Moscow Python Meetup №81"
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    duration = pl.total_duration
    assert str(duration) == "1:49:50"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 6590.0

    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"
