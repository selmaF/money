from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.graphics import Line, Color
from kivy.properties import (ObjectProperty, BooleanProperty, NumericProperty, ListProperty)
from random import random, randint
from kivy.core.window import Window
from kivy.vector import Vector as Vec
from kivy.clock import Clock
from kivy.utils import platform

extra_packages = 0

try:
    from plyer import vibrator
    extra_packages = 1
except ImportError:
    print 'Not all Packages are installed on Pc'


# toDo create StartScreen, SettingScreen, switch Screens /rodstar97
# toDo create random Coins but not on the Borders and no self Intersection /Selma
# toDo Scale Coins to Image Resolution
# toDo  Coin dynamics with other coins
# toDo optional Gyroscope, Sounds & Adds




#Window.size = (768, 924)


class Goal(Widget):
    pass




class Coin(Widget):
    counter = NumericProperty()
    worth = NumericProperty()
    vel = ListProperty()
    tmp_vec = ListProperty()

    def set_coin(self, size):
        coin_worthes = [1,2,5,10,20,50,100,200]
        posible_coins = {1 : 0.7, 2 : 0.75, 5 : 0.8, 10 : 0.7, 20 : 0.75, 50 : 1.0, 100 : 0.93, 200 : 1.09}
        random_coin = randint(0, 7)

        self.worth = coin_worthes[random_coin]#.get(1,'not found')#randint(1,8)
        self.size = (size/6)*(posible_coins.get(coin_worthes[random_coin])), (size/6)*(posible_coins.get(coin_worthes[random_coin]))
        self.vel = [0,0]#[randint(1,5), randint(1,5)]
        return self



class Game(RelativeLayout):
    counter = NumericProperty(0)
    selected = ObjectProperty(None)
    sel = BooleanProperty(False)
    coins = ListProperty()
    sum = NumericProperty(0)




    def generate_random_coins(self):
        generated_coins = []
        for i in range(12):
            self.counter += 1
            coin = Coin()
            coin_pos_X = randint(coin.size[0],Window.size[0]-coin.size[0])
            coin_pos_Y = randint(coin.size[0], int(Window.size[1]/1.5-(coin.size[1])))
            coin.set_coin(Window.size[0])
            coin.center = coin_pos_X, coin_pos_Y
            coin.counter = self.counter
            generated_coins.append(coin)

        for coin in generated_coins:
            self.add_widget(coin)
        self.coins = generated_coins


    def android_vibration(self):
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



class CoinApp(App):
    def build(self):
        self.title = 'Widget Selection'
        game = Game()
        game.generate_random_coins()
        Clock.schedule_interval(game.update, 1.0/60)
        return game


if __name__ == '__main__':
    CoinApp().run()



'''
# Add first coin on middle spot with random offset
self.counter += 1
first_coin = Coin()
first_coin_pos =int(Window.size[0]/2), int(Window.size[1]/3)
print type(first_coin_pos)
first_coin.center = first_coin_pos
first_coin.counter = self.counter
self.add_widget(first_coin)
'''