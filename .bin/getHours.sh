#!/bin/bash 
date=$(date "+%T")
notify-send.sh --replace-file=/tmp/date "$date" --expire-time=1500

