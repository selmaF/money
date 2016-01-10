#!/bin/bash
cd ~/money/learn_coins
pwd
git pull
buildozer android debug deploy
rsync -rtv ~/money/learn_coins/bin ~/Dropbox/kivy_money/Apps
