__author__ = 'bitybite'

import requests
import settings
from bs4 import BeautifulSoup


class TuneInRadioParser:
    @staticmethod
    def print_available_stations():
        for x in settings.stations:
            print('station ' + x + ' '
                  + settings.tune_in_link + settings.stations[x])

    @staticmethod
    def get_skip_words():
        return settings.skipWords

    @staticmethod
    def is_station_exists(station):
        if station in settings.stations:
            return True
        else:
            return False

    @staticmethod
    def get_song(station):
        print('..grabbing info from ' + station)
        r = requests.get(settings.tune_in_link + settings.stations[station])
        if r.status_code != 200:
            print(r.raise_for_status())

        parser = BeautifulSoup(r.text, 'html.parser')
        elements = parser.find_all('p', {'data-testid': 'guideItemTitleSubtitle'})
        if elements:
            song = elements[0].text
        else:
            raise Exception('Cannot parse page')

        return song
