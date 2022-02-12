#!/usr/bin/env python3

import os, time, sys
from pygame import mixer  # Load the popular external library

critical_hosts=['9.9.9.9', '8.8.8.8', '1.1.1.1']
warning_hosts=['1.2.3.4']


fail_counter=0
tolerance=1

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
  mixer.init()
  mixer.music.load('./audio/All_My_Friends_Hate_Me_-_Blood.mp3')
  mixer.music.play()
  while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
