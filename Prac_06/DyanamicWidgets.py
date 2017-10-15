from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.button import Label

NAMES = ["John", "Bill", "Bob"]

class DynamicWidgets(App):

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('DynamicWidgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in NAMES:
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)

DynamicWidgets().run()