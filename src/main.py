# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.components.LandingPage.main_page import MainPage
from src.components.Settings.background import Background
from src.components.Settings.devices import Devices
from src.components.Settings.notifications import Notifications
from src.components.ThrowBottle.create_bottle import CreateBottle
from kivy.core.window import Window
from src.components.Profile.profile_page import ProfilePage
from src.components.Settings.settings import SettingsPage

class DriftingBottleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(SettingsPage(name='settings'))
        sm.add_widget(CreateBottle(name='create_bottle'))
        sm.add_widget(ProfilePage(name='profile_page'))
        sm.add_widget(Notifications(name='notifications'))
        sm.add_widget(Background(name='background'))
        sm.add_widget(Devices(name='devices'))
        Window.size = (360, 640)
        return sm

if __name__ == '__main__':
    DriftingBottleApp().run()
