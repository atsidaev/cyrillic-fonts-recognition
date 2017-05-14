#!/bin/bash
# Selenium
if [ ! -f geckodriver -a ! "1`which geckodriver`" != "1" ]
then
	ARCH=32
	uname -a | grep x64 && ARCH=64
	GECKOVER=v0.13.0
	GECKOTGZ=geckodriver-$GECKOVER-linux${ARCH}.tar.gz
	wget https://github.com/mozilla/geckodriver/releases/download/$GECKOVER/$GECKOTGZ
	tar xf $GECKOTGZ geckodriver
	rm $GECKOTGZ
	sudo mv geckodriver $HOME/.local/bin
fi
pip3 install selenium
pip3 install configparser

#pillow and font tools
sudo apt-get install libjpeg-dev libfreetype6-dev zlib1g-dev
pip3 install fonttools
pip3 install pillow
pip3 install numpy
pip3 install tqdm
pip3 install imutils
pip3 install scipy
#opencv
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python3-dev python3-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

cd ~
git clone https://github.com/opencv/opencv.git
cd ~/opencv
mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
make
sudo make install

pip3 install opencv-python
