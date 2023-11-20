from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class SettingsPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', size=(300,500), spacing=40, pos_hint={'center_y': 1})
        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        background_button = Button(text="Background", size_hint_y=None, height=50)
        background_button.bind(on_press=self.nav_background)
        layout.add_widget(background_button)

        notifications_button = Button(text="Notifications", size_hint_y=None, height=50)
        notifications_button.bind(on_press=self.nav_notifications)
        layout.add_widget(notifications_button)

        devices_button = Button(text="Devices", size_hint_y=None, height=50)
        devices_button.bind(on_press=self.nav_devices)
        layout.add_widget(devices_button)

        self.add_widget(layout)


    def nav_notifications(self, instance):
        self.manager.current = 'notifications'

    def nav_background(self, instance):
        self.manager.current = 'background'

    def nav_devices(self, instance):
        self.manager.current = 'devices'

    def go_back(self, instance):
        self.manager.transition.direction = 'right'  # Optional: sets the animation direction to right
        self.manager.current = 'main_page'
