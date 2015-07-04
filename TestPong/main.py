
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    winPoint = 6  
    
    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(6,0).rotate(randint(0,360))
    
    def update(self, dt): 
        
        if self.player1.score == self.winPoint:
            self.player1.status = 'Gewonnen'
            self.player2.status = 'Verloren'
            return
        elif self.player2.score == self.winPoint:
            self.player2.status = 'Gewonnen'
            self.player1.status = 'Verloren'
            return
        
        self.ball.move()        

        #bounce of paddels
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        
        # bounce off top and bottom
        if(self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        
        # went of to a side to scare piont?
        if self.ball.x  < 0:
            self.player2.score += 1
            self.serve_ball()
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball()
            
       
            
            
    def on_touch_move(self,touch):
        if touch.x < self.width/3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width/3:
            self.player2.center_y = touch.y

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game
        
class PongBall(Widget):
    
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
            self.pos = Vector(*self.velocity) + self.pos
            
class PongPaddle(Widget):
    score = NumericProperty(0)
    status = StringProperty("")
  
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y)/(self.height/2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset
            
if __name__ == '__main__':
    PongApp().run()

