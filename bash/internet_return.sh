#!/usr/bin/env bash

#IFACE=enp1s0
ALARM_AUDIO_FILE=alarm.wav
HOST_TO_PING=8.8.8.8
RETRY_TIME=7

if [[ "$IFACE" = "" ]]; then
	printf "Using default route to ping.\n"
	PING_CMD="ping -c 1 ${HOST_TO_PING} > /dev/null"
else
	printf "IFACE get from environ(%s)\n" ${IFACE}
	PING_CMD="ping -I ${IFACE} -c 1 ${HOST_TO_PING} > /dev/null"
fi

function play_sound()
{
  printf "Playing sound...\n"
	aplay ${ALARM_AUDIO_FILE}

}

function print_date() {
	local connection_rec_time=$(date +%c)
	echo "Connection recovery at: ${connection_rec_time}"
}


until eval $PING_CMD; do
  sleep ${RETRY_TIME}
done

print_date
play_sound

exit 0
