import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
import kivy.uix.gridlayout as gridl
from kivy.uix.label import Label
from kivy.uix.button import Button


class ButtonsGrid(App):
    def build(self):
        layout = gridl.GridLayout(cols=3, rows=3)
        layout.add_widget(Button(text='0,0'))
        layout.add_widget(Button(text='0,1'))
        layout.add_widget(Button(text='0,2'))
        layout.add_widget(Button(text='1,0'))
        layout.add_widget(Button(text='1,1'))
        layout.add_widget(Button(text='1,2'))
        layout.add_widget(Button(text='2,0'))
        layout.add_widget(Button(text='2,1'))
        layout.add_widget(Button(text='2,2'))
        return layout


if __name__ == '__main__':
    ButtonsGrid().run()
