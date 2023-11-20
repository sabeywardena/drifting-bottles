import sys
from datetime import datetime
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock

class IconLabel(ButtonBehavior, Label):
    pass

class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical')

        # Header with icons
        header = BoxLayout(size_hint_y=None, height=100, orientation='horizontal')
        
        # Time label with the current time
        self.time_label = IconLabel(size_hint_x=None, width=100)
        self.update_time()  # Initialize with current time
        header.add_widget(self.time_label)

        # Spacer widget to push text to the middle
        spacer_left = BoxLayout(size_hint_x=1)
        header.add_widget(spacer_left)

        # Drifting Bottle text (centered)
        header.add_widget(Label(text='Drifting Bottle', size_hint_x=None, width=200, halign='center'))

        # Spacer widget to push settings button to the right
        spacer_right = BoxLayout(size_hint_x=1)
        header.add_widget(spacer_right)

        # Settings button (right-aligned)
        settings_button = Button(background_normal=r'C:\Users\52558\Desktop\KivyTest\drifting-bottles-main\src\assets\setting.png', size_hint=(None, None), size=(90, 90))
        settings_button.bind(on_press=self.go_to_settings)
        header.add_widget(settings_button)

        main_layout.add_widget(header)

        # Middle content area
        middle_content = Label(text='No messages right now')
        main_layout.add_widget(middle_content)

        # Footer with navigation icons
        footer = BoxLayout(size_hint_y=None, height=50, orientation='horizontal',
                           spacing=(Window.width - (3 * 120)) / 7)
        
        bottle_button = Button(background_normal=r'C:\Users\52558\Desktop\KivyTest\drifting-bottles-main\src\assets\bottle.png', size_hint=(None, None), size=(120, 120))
        bottle_button.bind(on_press=self.go_to_create_bottle)
        footer.add_widget(bottle_button)
        
        search_button = Button(background_normal=r'C:\Users\52558\Desktop\KivyTest\drifting-bottles-main\src\assets\search.png', size_hint=(None, None), size=(120, 120))
        search_button.bind(on_press=self.go_to_search)
        footer.add_widget(search_button)

        profile_button = Button(background_normal=r'C:\Users\52558\Desktop\KivyTest\drifting-bottles-main\src\assets\person.png', size_hint=(None, None), size=(120, 120))
        profile_button.bind(on_press=self.go_to_profile)
        footer.add_widget(profile_button)

        main_layout.add_widget(footer)
        self.add_widget(main_layout)

        # Schedule to update the time every second
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        # Update the time label with the current time
        self.time_label.text = datetime.now().strftime('%H:%M:%S')

    def go_to_create_bottle(self, instance):
        self.manager.current = 'create_bottle'

    def go_to_profile(self, instance):
        self.manager.current = 'profile_page'

    def go_to_settings(self, instance):
        self.manager.current = 'settings'

    def go_to_search(self, instance):
        self.manager.current = 'search'
        
class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main'))
        return sm

if __name__ == '__main__':
    TestApp().run()
