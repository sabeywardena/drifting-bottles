# main.py
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from components.LandingPage.main_page import MainPage
from components.Settings.background import Background
from components.Settings.devices import Devices
from components.Settings.notifications import Notifications
from components.ThrowBottle.create_bottle import CreateBottle
from components.Search.search import SearchBottle
from components.Profile.profile_page import ProfilePage
from components.Settings.settings import SettingsPage
from components.Search.choose_bottle import ChooseBottle
from components.Search.open import Open
from kivy.core.window import Window

class DriftingBottleApp(App):
    def build(self):
        sm = ScreenManager()

        # Add screens to the ScreenManager
        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(SettingsPage(name='settings'))

        # Calculate window size
        screen_width = Window.width - 150
        screen_height = Window.height + 400
        width_factor = 0.8  # Adjust this factor as needed
        height_factor = 0.9  # Adjust this factor as needed
        window_width = int(screen_width * width_factor)
        window_height = int(screen_height * height_factor)
        Window.size = (window_width, window_height)

        # Create a CreateBottle screen with the window size
        create_bottle_screen = CreateBottle(window_size=(window_width, window_height), name='create_bottle')
        sm.add_widget(create_bottle_screen)

        sm.add_widget(SearchBottle(name='search'))
        sm.add_widget(ProfilePage(name='profile_page'))
        sm.add_widget(Notifications(name='notifications'))
        sm.add_widget(Background(name='background', color_callback=self.change_background_color))
        sm.add_widget(ChooseBottle(name='choose_bottle'))
        sm.add_widget(Devices(name='devices'))
        sm.add_widget(Open(name='open'))

        return sm

    def change_background_color(self, color):
        # Update the background color based on the callback
        Window.clearcolor = color
        # You can also save the selected color for later use if needed
        self.selected_color = color

if __name__ == '__main__':
    DriftingBottleApp().run()