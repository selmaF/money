from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.graphics import Line, Color
from kivy.properties import (ObjectProperty, BooleanProperty, NumericProperty, ListProperty)
from random import random, randint
from kivy.core.window import Window
from kivy.clock import Clock



Window.size = (768, 924)


class Goal(Widget):
    pass




class Coin(Widget):
    counter = NumericProperty()
    worth = NumericProperty()

    def set_coin(self):
        coin_worthes = [1,2,5,10,20,50,100,200]
        posible_coins = {1 : 0.7, 2 : 0.75, 5 : 0.8, 10 : 0.7, 20 : 0.75, 50 : 1.0, 100 : 0.93, 200 : 1.09}
        random_coin = randint(0, 7)

        self.worth = coin_worthes[random_coin]#.get(1,'not found')#randint(1,8)
        self.size = self.size[0]*(posible_coins.get(coin_worthes[random_coin])), self.size[1]*(posible_coins.get(coin_worthes[random_coin]))
        #print posible_coins.get(coin_worthes[random_coin],1)
        return self



class Game(RelativeLayout):
    counter = NumericProperty(0)
    selected = ObjectProperty(None)
    sel = BooleanProperty(False)
    coins = ListProperty()
    sum = NumericProperty(0)


# toDo create random Coins but not on the Borders and no self Intersection

    def generate_random_coins(self):
        generated_coins = []
        for i in range(12):
            self.counter += 1
            coin = Coin()
            proxy_coin_size = coin.size * 2
            #coinPos = int(random()*Window.size[0])+(coin.size[0]/2), int(random()*Window.size[1]/3.5+(coin.size[1]/2))
            coin_pos_X = randint(coin.size[0],Window.size[0]-coin.size[0])
            coin_pos_Y = randint(coin.size[0], int(Window.size[1]/3.5-(coin.size[1])))
            coin.set_coin()
            coin.center = coin_pos_X, coin_pos_Y
            coin.counter = self.counter
            generated_coins.append(coin)

        for coin in generated_coins:
            self.add_widget(coin)
        self.coins = generated_coins


    def sum_coins_welth(self):
        worth = 0
        for coin in self.coins:
            if coin.collide_widget(self.ids.goal_id):
                worth += coin.worth
        return worth


    def on_touch_down(self, touch):
        for child in self.coins:
            if child.collide_point(*touch.pos):
                self.selected = child
                self.sel = True
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
            child.center = touch.pos
            self.ids.sum_id.text = str(self.sum_coins_welth())

            with self.canvas:
                touch.ud['line']=Line(rectangle=(child.x-5,child.y-5,child.width+10,child.height+10),width=1, dash_length=5,dash_offset=2)



    def on_touch_up(self, touch):

        if self.sel == True:
            self.canvas.remove(touch.ud['line'])
            self.sel = False


class CoinApp(App):
    def build(self):
        self.title = 'Widget Selection'
        game = Game()
        game.generate_random_coins()
        #Clock.schedule_interval(game.update, 1.0/60)
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