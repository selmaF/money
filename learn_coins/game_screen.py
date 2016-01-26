from kivy.uix.screenmanager import Screen






from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import  ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Line, Color
from kivy.properties import (ObjectProperty, BooleanProperty, NumericProperty, ListProperty)
from random import random, randint
from kivy.vector import Vector as Vec
from kivy.clock import Clock
from kivy.utils import platform
import numpy as np
import math

class Goal(Widget):
    pass


class Coin(Widget):
    counter = NumericProperty()
    worth = NumericProperty()
    vel = ListProperty()
    tmp_vec = ListProperty()

    def set_coin(self, size, pos):
        coin_worthes = [1,2,5,10,20,50,100,200]
        posible_coins = {1 : 0.7, 2 : 0.75, 5 : 0.8, 10 : 0.7, 20 : 0.75, 50 : 1.0, 100 : 0.93, 200 : 1.09}
        random_coin = randint(0, 7)

        self.worth = coin_worthes[random_coin]#.get(1,'not found')#randint(1,8)
        self.size = (min(size)/6)*(posible_coins.get(self.worth)), (min(size)/6)*(posible_coins.get(self.worth))
        self.vel = [0, 0]#[randint(1,5), randint(1,5)]
        self.center = int(pos[1]), int(pos[0])

        return self


class Matrix(ObjectProperty):
    def __init__(self, window_size):
        self.window_size = window_size
        self.table = np.zeros((window_size[0], window_size[1]), bool)
        self.coin = np.zeros((window_size[0], window_size[1]), bool)
        self.border = np.zeros((window_size[0], window_size[1]), bool)
        self.max_coin_size = int(np.ceil(1.09*window_size[0]/6))     #TO DO connect with Variables in class method set_coin??

    def set_border(self, coin_size):
        self.border = np.zeros((self.window_size[0], self.window_size[1]), bool)
        for i in range(0, self.window_size[0]):
            if (i < (coin_size/2)) or (i > (self.window_size[0]-(coin_size/2))):
                self.table[(i, range(0, int(self.window_size[1])))] = 1
            else:
                self.border[(i, range(0, int(coin_size/2)))] = 1
                self.border[(i, range(int(self.window_size[1]*0.55), self.window_size[1]))] = 1
        return

    def set_coin(self, coin):
        self.set_border(coin.size[0])
        pos = self.find_new_position()
        coin.set_coin(self.window_size, (pos[1], pos[0]))

        radius = int((coin.size[0] + self.max_coin_size)/2)

         # if pos is near matrix-border

        maxdistance = { "left" : radius, "right" : radius, "up" : radius, "down" : radius}

        if pos[0] - radius < 0:
            maxdistance["up"] = radius - pos[0]
        elif pos[0] + radius > self.window_size[0]:
            maxdistance["down"] = self.window_size[0] - pos[0]
        if pos[1] - radius < 0:
            maxdistance["left"] = radius - pos[1]
        elif pos[1] + radius > self.window_size[1]:
            maxdistance["right"] = self.window_size[1] - pos[1]

        for i in range(pos[1]-maxdistance["right"], pos[1]+maxdistance["left"]):
            distance = int(np.cos(np.arcsin(((float(i-pos[1]))/radius)))*radius)

            if distance > maxdistance["up"]:
                self.coin[range(pos[0]-maxdistance["up"], pos[0]+distance), i] = 1
            elif distance > maxdistance["down"]:
                self.coin[range(pos[0]-distance, pos[0]+maxdistance["down"]), i] = 1
            else:
                self.coin[range(pos[0]-distance, pos[0]+distance), i] = 1

        self.table = self.table + self.coin
        test = np.transpose(np.nonzero(np.invert(self.coin)))  #zum debuggen
        test2 = self.coin
        return

    def find_new_position(self):
        possible_pixel = np.transpose(np.nonzero(np.invert(self.table + self.border)))
        pos_index = randint(0, possible_pixel.size/2)
        coin_pos = possible_pixel[pos_index]
        return coin_pos


class GameScreen(Screen):
    counter = NumericProperty(0)
    selected = ObjectProperty(None)
    sel = BooleanProperty(False)
    coins = ListProperty()
    sum = NumericProperty(0)

    def generate_random_coins(self):
        generated_coins = []
        matrix = Matrix(Window.size)
        coin_row = []
        for i in range(12):
            self.counter += 1
            coin = Coin()
            matrix.set_coin(coin)
            coin.counter = self.counter
            generated_coins.append(coin)

        for coin in generated_coins:
            self.add_widget(coin)

        self.coins = generated_coins


    def android_vibration(self):
        try:
            from plyer import vibrator
            extra_packages = 1
        except ImportError:
            print 'Not all Packages are installed on Pc'
        if extra_packages == 1:
            if platform == 'android':
                vibrator.vibrate(0.1)


    def sum_coins_welth(self):
        worth = 0
        for coin in self.coins:
            if coin.collide_widget(self.ids.goal_id):
                worth += coin.worth
        return worth

    def update(self,dt):
        for coin in self.coins:
            if coin.pos[0] <= 0 and coin.vel[0] < 0:
                coin.vel[0] *= -1
                self.android_vibration()
            if coin.pos[0] >= Window.size[0]-coin.size[0] and coin.vel[0] > 0:
                coin.vel[0] *= -1
                self.android_vibration()
            if coin.pos[1] <= 0 and coin.vel[1] < 0:
                coin.vel[1] *= -1
                self.android_vibration()
            if coin.pos[1] >= Window.size[1]-coin.size[1] and coin.vel[1] > 0:
                coin.vel[1] *= -1
                self.android_vibration()

        for coin in self.coins:
            coin.pos = Vec(coin.vel) + Vec(coin.pos)
            coin.vel = Vec(coin.vel) *0.87
            self.ids.sum_id.text = str(self.sum_coins_welth())





    def on_touch_down(self, touch):
        for child in self.coins:
            if child.collide_point(*touch.pos):
                self.selected = child
                self.sel = True
                    #print 'ahha'
                with self.canvas:
                    Color(0,0,0)
                    touch.ud['line'] = Line(rectangle=(child.x-5,child.y-5,child.width+10,child.height+10), dash_length=5, dash_offset=2)
                    break

        # if touch.x<100 and touch.y<100: why ?
        # return super(Ex46, self).on_touch_down(touch) why ?
        #print touch.x, touch.y

        # for child in self.children:
        # print child.ids['id01'].text


    def on_touch_move(self, touch):

        if self.sel == True:
            self.canvas.remove(touch.ud['line'])
            child = self.selected
            child.tmp_vec =  Vec(touch.pos) - Vec(child.center)
            child.center = touch.pos

            self.ids.sum_id.text = str(self.sum_coins_welth())
            #self.ids.sum_id.text = str(self.selected.tmp_vec)

            with self.canvas:
                touch.ud['line']=Line(rectangle=(child.x-5,child.y-5,child.width+10,child.height+10),width=1, dash_length=5,dash_offset=2)



    def on_touch_up(self, touch):

        if self.sel == True:
            self.canvas.remove(touch.ud['line'])
            self.selected.vel = self.selected.tmp_vec
            self.sel = False

    def on_enter(self):
        self.generate_random_coins()