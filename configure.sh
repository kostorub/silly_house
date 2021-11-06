#!/bin/bash
CUR_DIR=`pwd`

sudo apt update && \ 
sudo apt upgrade -y && \
sudo apt install -y gcc python3-venv python3-dev libatlas-base-dev libwebp-dev libtiff5 libopenjp2-7 libilmbase-dev libopenexr-dev \
ffmpeg libgtk-3-0 libgpiod-dev portaudio19-dev && \
python3 -m venv venv && \
$CUR_DIR/venv/bin/python3 -m pip install -U pip setuptools wheel && \
$CUR_DIR/venv/bin/python3 -m pip install -r requirements.txt
