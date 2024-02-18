#!/usr/bin/env bash
nitrogen --restore
# picom &
redshift &

# output names differ when using the nvidia gpu
if xrandr | grep eDP-1-1; then
    export INTERNAL_OUTPUT="eDP-1-1"
    export EXTERNAL_OUTPUT="HDMI-1-1"
elif xrandr | grep eDP-1; then
    export INTERNAL_OUTPUT="eDP-1"
    export EXTERNAL_OUTPUT="HDMI-1"
elif xrandr | grep eDP1; then
    export INTERNAL_OUTPUT="eDP1"
    export EXTERNAL_OUTPUT="HDMI1"
fi

sxhkd &

nm-applet &

dunst &

~/software/aw-qt &

xrandr --auto
xrandr --output HDMI-1 --same-as eDP-1

