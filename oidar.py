#!/usr/bin/env python3

import os, time, sys, fnmatch
from pygame import mixer  # Load the popular external library

critical_hosts=['9.9.9.9', '8.8.8.8', '1.1.1.1', '192.168.0.1']
warning_hosts=['1.2.3.4']


audio_dir='./audio'
fail_counter=0
tolerance=0

def find(pattern, path):
  result = []
  for root, dirs, files in os.walk(path):
    for name in files:
      if fnmatch.fnmatch(name, pattern):
        result.append(os.path.join(root, name))
  return result

song_list=find('*.mp3', audio_dir)
if len(song_list) < 1:
  # no songs found
  print('Error: no songs found in directory ' + audio_dir)
  sys.exit(1)

for host in critical_hosts:
  print(host)
  response = os.system("ping -c 1 " + host)
  if response == 0:
    print(host, 'is up!')
  else:
    print(host, 'is down!')
    fail_counter += 1

if fail_counter == 0:
  # all is fine
  sys.exit(0)
elif fail_counter <= tolerance:
  # not perfect - but good enough
  sys.exit(1)
else:
  # omg - the internet is down!1!!!
  print("Jen, the internet is down! Let's play some music!")
  #mixer.init()
  for song in song_list:
    print(song)
    #mixer.music.load(song)
    #mixer.music.play()
    #while mixer.music.get_busy():  # wait for music to finish playing
    #  time.sleep(1)
