import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class MainGridLayout(Widget):
    pass

class MainApp(App):
    def build(self):
        return MainGridLayout()

if __name__ == "__main__":
    MainApp().run()