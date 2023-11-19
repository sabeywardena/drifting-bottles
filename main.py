# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from main_page import MainPage
from create_bottle import CreateBottle
from kivy.core.window import Window
from profile_page import ProfilePage  # Your profile page screen

class DriftingBottleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(CreateBottle(name='create_bottle'))
        sm.add_widget(ProfilePage(name='profile_page'))
        Window.size = (360, 640)
        return sm

if __name__ == '__main__':
    DriftingBottleApp().run()