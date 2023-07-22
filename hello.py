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
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 50
        # new grid for inputs
        self.input_grids = GridLayout(
            row_force_default = True,
            row_default_height = 50
        )
        self.input_grids.cols = 2
        # set name widget
        self.input_grids.add_widget(Label(text="Your name:"))
        self.name = TextInput(multiline=False)
        self.input_grids.add_widget(self.name)
        # set age widget
        self.input_grids.add_widget(Label(text="Your age:"))
        self.age = TextInput(multiline=False)
        self.input_grids.add_widget(self.age)
        # set place widget
        self.input_grids.add_widget(Label(text="Your place:"))
        self.place = TextInput(multiline=False)
        self.input_grids.add_widget(self.place)

        # add input grids
        self.add_widget(self.input_grids)

        # set button widget
        self.submit_button = Button(
            text="Submit",
            on_press=self.on_press,

            # styling
            size_hint_y = None,
            height = 50
        )
        self.add_widget(self.submit_button)

    def on_press(self, instance):
        name = self.name.text
        age = self.age.text
        place = self.place.text

        # set an response widget
        self.add_widget(Label(
            text=f"Hi {name}! you're {age} years old and from {place}. Nice to meet you :)")
        )

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()