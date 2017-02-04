__author__ = 'bitybite'

import requests
from bs4 import BeautifulSoup


class TuneInRadioParser:
    __tuneIn_link = 'http://tunein.com'
    __stations = {
        'kexp': '/radio/KEXP-FM-903-s32537',
        'got': '/radio/GotRadio-Indie-Underground-s49685/'
    }
    __skipWords = ['US', 'Variety Mix']

    def print_available_stations(self):
        for x in self.__stations:
            print('station ' + x + ' '
                  + self.__tuneIn_link + self.__stations[x])

    def get_skip_words(self):
        return self.__skipWords

    def is_station_exists(self, station):
        if station in self.__stations:
            return True
        else:
            return False

    def get_song(self, station):

        print('..grabbing info from ' + station)
        r = requests.get(self.__tuneIn_link + self.__stations[station])
        if r.status_code != 200:
            print(r.raise_for_status())

        parser = BeautifulSoup(r.text, 'html.parser')
        song = parser.find('li', 'guide-item').find('div', 'content').find('h3').string

        return song
