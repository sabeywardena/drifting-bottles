from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class Notifications(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size=(300,500), spacing=40, pos_hint={'center_y': 1})
        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition.direction = 'right'  # Optional: sets the animation direction to right
        self.manager.current = 'settings'
