# oidar

reverse internet radio (only works, when internet is down)

## Requirements
- Python3
- Python lib pygame
- audio setup
- mp3 audio file(s) in subdir ./audio

## Installation
- pip3 install pygame

## Usage
- edit oidar.py and adjust:
  - list of ```critical_hosts```
  - adjust ```tolerance``` if needed to allow for one or more failing hosts without raising the alarm
- chmod 755 oidar.py
- test:
  - ./oidar.py
- add oidar.py to cron

## Hardware setup
- Raspberry Pi
- LAN connection
- external speakers

## Software setup
- Raspbian (patching via cron-apt)
- Python script to detect internet connection
- $MP3 player software
- CC music [Source](https://www.epidemicsound.com/commercial-subscription/)

## Check script
- checks connection to a set of network services

## Network services to be checked
- ping targets
  - 9.9.9.9
  - etc.
- retrieve content via http [maybe like this](https://www.kite.com/python/answers/how-to-check-internet-connection-in-python)
- etc.?

## Monitoring concept
- if a certain share of network checks fails, music plays. Loud music plays. Loud, irritating music plays.
- service needs to be checkable via network (eg via a checkmk check)
