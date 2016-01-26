from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.graphics import Color, Ellipse, Line


class GraphInterface(Widget):
    node = ObjectProperty(None)



class GraphApp(App):

    def build(self):
        node = GraphNode()
        game = GraphInterface()

        createNodeButton = Button(text = 'CreateNode', pos=(100,0))
        createEdgeButton = Button(text = 'CreateEdge')
        game.add_widget(createNodeButton)
        game.add_widget(createEdgeButton)

        def createNode(instance):
            game.add_widget(GraphNode())
            print "Node Created"

        def createEdge(instance):
            game.add_widget(GraphEdge())
            print "Edge Created"

        createNodeButton.bind(on_press=createNode)
        createEdgeButton.bind(on_press=createEdge)
        return game

class GraphNode(Button):

    def moveNode(self):
        with touch:
            self.pos=[touch.x-25, touch.y-25]


   #def onTouchMove(self, touch):
   #   if self.collide_point(touch.x, touch.y):
   #       self.pos=[touch.x-25, touch.y-25]
    pass

class GraphEdge(Widget):

    def __init__(self, **kwargs):
        super(GraphEdge, self).__init__(**kwargs)
        with self.canvas:
            Line(points=[100, 100, 200, 100, 100, 200], width=1)
    pass

if __name__ == '__main__':

    GraphApp().run()