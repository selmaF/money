#!/bin/bash
cd ~/Documents/PycharmProjects/money/learn_coins

buildozer android debug deploy
rsync -rtv ~/Documents/PycharmProjects/money/learn_coins/bin ~/Dropbox/kivy_money/Apps
