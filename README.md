# oidar

reverse internet radio (only works, when internet is down)

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
- etc.?

## Monitoring concept
- if a certain share of network checks fails, music plays. Loud music plays. Loud, irritating music plays.
- service needs to be checkable via network (eg via a checkmk check)
