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
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        # set age widget
        self.add_widget(Label(text="Your age:"))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)
        # set place widget
        self.add_widget(Label(text="Your place:"))
        self.place = TextInput(multiline=False)
        self.add_widget(self.place)
        # set button widget
        self.submit_button = Button(text="Submit", on_press=self.on_press)
        self.add_widget(self.submit_button)

    def on_press(self, instance):
        name = self.name.text
        age = self.age.text
        place = self.place.text

        # set an response widget
        self.add_widget(Label(text=f"Hi {name}! you're {age} years old and from {place}. Nice to meet you :)"))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()