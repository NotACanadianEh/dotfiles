#!/bin/sh

case "$1" in
    --toggle)
	if [ "$(pgrep dropbox)" ]; then
	    pkill -f dropbox
	else
	    dropbox &
	fi
	;;
    *)
	if [ "$(pgrep dropbox)" ]; then
	    echo ""
	else
	    echo "Dropbox is not running"
	fi
	;;
esac
