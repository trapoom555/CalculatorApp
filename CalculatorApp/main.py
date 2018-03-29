from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder

class CalcGridLayout(GridLayout):
    Builder.load_file('eiei.kv')
    def calculate(self, calculation):
        if calculation:
            try :
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"
        
class calculatorapp(App):
    def build(self):
        return CalcGridLayout()

if __name__ == "__main__" :
    calculatorapp().run()