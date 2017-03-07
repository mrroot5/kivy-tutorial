import kivy
kivy.require('1.9.1')

from kivy.app import App
import kivy.uix.gridlayout as gridl
from kivy.uix.button import Button

class ButtonsGrid(App):
    def build(self):
        layout = gridl.GridLayout(cols=3, rows=3)
        # Boton por defecto
        layout.add_widget(Button(text='0,0'))
        # Boton personalizado:
        # Podemos agregar todas las propiedades
        # directamente al constructor
        customBtn = Button(id="btnUp", text='Click Me!!')
        # O podemos agregarlas posteriormente
        customBtn.bold=True
        customBtn.background_color=[255, 0, 0, 1]
        customBtn.bind(on_press=self.clicked)
        layout.add_widget(customBtn)
        layout.add_widget(Button(text='0,2'))
        layout.add_widget(Button(text='1,0'))
        layout.add_widget(Button(text='1,1'))
        layout.add_widget(Button(text='1,2'))
        layout.add_widget(Button(text='2,0'))
        layout.add_widget(Button(text='2,1'))
        layout.add_widget(Button(text='2,2'))
        return layout
        
    def clicked(self, btn):
        print(btn.text)

if __name__ == '__main__':
    ButtonsGrid().run()
