# create_bottle.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class CreateBottle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Create a Bottle Message'))
        # Here you would add your widgets for creating a bottle message
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main_page'