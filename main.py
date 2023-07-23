import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("float_layout.kv")
class MainGridLayout(Widget):
    pass


class MainApp(App):
    def build(self):
        Window.clearcolor = (240/255, 240/255, 240/255, 1)
        return MainGridLayout()

if __name__ == "__main__":
    MainApp().run()