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
    coin_matrix = np.zeros((Window.size[0],Window.size[0]),bool)

    def set_coin(self, size, pos):
        coin_worthes = [1,2,5,10,20,50,100,200]
        posible_coins = {1 : 0.7, 2 : 0.75, 5 : 0.8, 10 : 0.7, 20 : 0.75, 50 : 1.0, 100 : 0.93, 200 : 1.09}
        random_coin = randint(0, 7)

        self.worth = coin_worthes[random_coin]#.get(1,'not found')#randint(1,8)
        self.size = (size/6)*(posible_coins.get(self.worth)), (size/6)*(posible_coins.get(self.worth))
        self.vel = [0,0]#[randint(1,5), randint(1,5)]
        max_coin_size = (size/6)*(posible_coins.get(max(coin_worthes))), (size/6)*(posible_coins.get(max(coin_worthes)))
        radius = int((self.size[0]+max_coin_size[0])/2)
        for i in range(pos[1]-radius, pos[1] + radius):
            dis_vert = (float(i-pos[1]))/radius
            alpha = np.arcsin((dis_vert))
            cos = np.cos(alpha)
            dis_hori = int(cos*radius)
            self.coin_matrix[range(pos[0]-dis_hori, pos[0]+dis_hori), i] = 1
        test = np.transpose(np.nonzero(self.coin_matrix))  #zum debuggen
        test2 = self.coin_matrix                            # zum debuggen
        return self



class GameScreen(Screen):
    counter = NumericProperty(0)
    selected = ObjectProperty(None)
    sel = BooleanProperty(False)
    coins = ListProperty()
    sum = NumericProperty(0)


    def generate_random_coins(self):
        generated_coins = []
        table_matrix = np.zeros((Window.size[0], Window.size[1]),bool)
        max_coin_size = 1.09*Window.size[0]/6                       #TODO connect with Variables in class method set_coin??
        for i in range(0, Window.size[0]):
            if (i < (max_coin_size/2)) or (i > (Window.size[0]-(max_coin_size/2))):
                table_matrix [(i,range(0,int(Window.size[1])))] = 1
            else:
                table_matrix[(i, range(0, int(max_coin_size/2)))] = 1
                table_matrix[(i, range(int(Window.size[1]-(max_coin_size/2)), Window.size[1]))] = 1

        for i in range(12):
            self.counter += 1
            coin = Coin()
            coin_pos_X = randint(coin.size[0],Window.size[0]-coin.size[0])
            coin_pos_Y = randint(coin.size[0], int(Window.size[1]/1.5-(coin.size[1])))
            coin_pos = (coin_pos_X, coin_pos_Y)
            coin.set_coin(Window.size[0], coin_pos)
            coin.center = coin_pos_X, coin_pos_Y
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