#!/usr/bin/env bash

#IFACE=wlp2s0
IFACE=enp1s0
ALARM_AUDIO_FILE=alarm.wav
HOST_TO_PING=192.168.0.1

if [[ "$IFACE" = "" ]]; then
	export IFACE=eth0
	printf "IFACE was set to %s\n" ${IFACE}
else
	printf "IFACE get from environ(%s)\n" ${IFACE}
fi


PING_CMD="ping -I ${IFACE} -c 1 ${HOST_TO_PING} > /dev/null"

function play_sound()
{
  printf "Playing sound...\n"
	aplay ${ALARM_AUDIO_FILE}

}


until eval $PING_CMD; do
  printf "ConnectionError, retry...\n"
  sleep 3
done

play_sound

exit 0
