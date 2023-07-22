import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MainGridLayout(Widget):
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    place = ObjectProperty(None)

class MainApp(App):
    def build(self):
        return MainGridLayout()

if __name__ == "__main__":
    MainApp().run()