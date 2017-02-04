## TuneIn radio tracker ##

#### dispay the current song that is playing in console ####


  You will need python3 and `beautifulsoup` library

  To install dependency `pip install bs4`

  Search data will be saved in your home directory
  /radio/name_of_the_station.txt

  You can add your radio station in file `TuneInRadioParser` in `__stations` section,

  like `'kexp': '/radio/KEXP-FM-903-s32537'`

  where `kexp` is abbreviated name  
  and `/radio/KEXP-FM-903-s32537` is the link to page

  To run script, type `python3 app.py kexp` in project direcory, where `kexp` is the
  name of radio station, described above

  Add `!` to the end of command, like
  `python3 app.py kexp !` to mark this song as favorite

### Enjoy! ###
