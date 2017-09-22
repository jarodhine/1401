from kivy.app import App
from kivy.lang import Builder

M_TO_KM = 1.609


class Converter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('ScratchEx1.kv')
        return self.root

    def calculate(self):
        value = self.validMiles()
        result = value * M_TO_KM
        self.root.ids.output.text = str(result)

    def increment(self, change):
        value = self.validMiles() + change
        self.root.ids.input.text = str(value)
        self.calculate()

    def validMiles(self):
        try:
            value = float(self.root.ids.input.text)
            return value
        except ValueError:
            return 0

Converter().run()
