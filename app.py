__author__ = 'bitybite'

from entities.TuneInRadioParser import TuneInRadioParser
from time import strftime
import os
import sys
import settings

station = ''
favorite = False

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
    TuneInRadioParser.print_available_stations()
    sys.exit()

if TuneInRadioParser.is_station_exists(station):
    song = TuneInRadioParser.get_song(station)
    print('**Listening now: ' + song)

    if not settings.save_to_file:
        sys.exit(0)

    if song not in TuneInRadioParser.get_skip_words():
        if len(song) > 0:
            filename = settings.save_path
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
            print('Cannot parse song')
    else:
        print('**Cannot parse ' + song + ' , will skip')
else:
    print('..Cannot...understand what are you listening')
