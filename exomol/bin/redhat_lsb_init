#!/bin/bash

if [ ! -d  /usr/X11R6/lib/X11/xserver ]; then
  mkdir -p /usr/X11R6/lib/X11/xserver
fi

if [ -f /usr/lib/xserver/SecurityPolicy ]; then
  ln -snf /usr/lib/xserver/SecurityPolicy /usr/X11R6/lib/X11/xserver/SecurityPolicy
fi

if [ -f /usr/lib64/xserver/SecurityPolicy ]; then
  ln -snf /usr/lib64/xserver/SecurityPolicy /usr/X11R6/lib/X11/xserver/SecurityPolicy
fi

if [ -d /usr/share/X11/fonts ]; then
  ln -snf /usr/share/X11/fonts /usr/X11R6/lib/X11/fonts
fi

if [ -f /usr/share/X11/rgb.txt ]; then
  ln -snf /usr/share/X11/rgb.txt /usr/X11R6/lib/X11/rgb.txt
fi
