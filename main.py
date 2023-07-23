import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MainGridLayout(Widget):
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    place = ObjectProperty(None)

    def handle_press(self) -> None:
        name = self.name.text
        age = self.age.text
        place = self.place.text
        # print response
        print(f"Hi {name}! you're {age} years old and from {place}")
        # clear inputs
        self.handle_clear()

    def handle_clear(self) -> None:
        self.name.text = ""
        self.age.text = ""
        self.place.text = ""


class MainApp(App):
    def build(self):
        return MainGridLayout()

if __name__ == "__main__":
    MainApp().run()