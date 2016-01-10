from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest

#class CoinGame(Widget):
    #pass


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/""find?q+{}&type+like"
        search_url = search_template.format(self.search_input.text)
        request =  UrlRequest(search_url, self.found_location)

    def found_location(self,request,data):
        citties = ["{} ({})".format(d['name'], d['sys']['country'])for d in data['list']]
        print "\n".format(citties)


class CoinApp(App):
    def testIt(self):
        pass

    #def build(self):
        #return CoinGame()


if __name__ == "__main__":
    CoinApp().run()
