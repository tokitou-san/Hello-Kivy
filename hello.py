import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, *args, **kwargs):
        # initialize constructor
        super(MyGridLayout, self).__init__(*args, **kwargs)
        # configure no:of cols
        self.cols = 2
        # set name widget
        self.add_widget(Label(text="Your name:"))
        self.add_widget(TextInput(multiline=False))
        # set age widget
        self.add_widget(Label(text="Your age:"))
        self.add_widget(TextInput(multiline=False))
        # set place widget
        self.add_widget(Label(text="Your place:"))
        self.add_widget(TextInput(multiline=False))
        # set button widget
        self.add_widget(Button(text="Submit"))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()