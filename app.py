__author__ = 'bitybite'

import sys
sys.path.append('entities')

from time import strftime
from entities.TuneInRadioParser import TuneInRadioParser
from os.path import expanduser
import os

station = ''
favorite = False
parser = TuneInRadioParser()

if len(sys.argv) == 2:
    station = sys.argv[1]
elif len(sys.argv) == 3:
    station = sys.argv[1]
    try:
        if sys.argv[2] == '!':
            print('**It\'s your favorite!!!')
            favorite = True
        else:
            print('**Cannot distinguish is it your fav track or not')
    except IndexError:
        print('**Cannot distinguish is it your fav track or not')
else:
    print('********************************************\n'
          '  | Please specify correct params, like    |\n'
          '  |  user@user:~> app [station_name] <!>   |\n'
          '  |  where [station_name] is station name  | \n'
          '  |  and <!> if you really like this song  |\n'
          '********************************************\n')
    parser.print_available_stations()
    sys.exit()

if parser.is_station_exists(station):
    song = parser.get_song(station)
    print('**Listening now: ' + song)

    if song not in parser.get_skip_words():
        if len(song) > 0:
            filename = expanduser("~") + '/radio/'
            if not os.path.exists(filename):
                os.makedirs(filename)
            filename += '__' + station + '.txt'
            print('**Writing to file ' + filename)
            with open(filename, 'a') as out:
                if favorite:
                    res = out.write(song + ' ::: ' + strftime("%Y-%m-%d %H:%M") + ' ::: !' + '\n')
                else:
                    res = out.write(song + ' ::: ' + strftime("%Y-%m-%d %H:%M") + '\n')
    else:
        print('**Cannot parse ' + song + ' , will skip')
else:
    print('..Cannot...understand what are you listening')
