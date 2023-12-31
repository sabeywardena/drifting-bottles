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

        header = BoxLayout(size_hint_y=None, height=100, orientation='horizontal')
        
        self.time_label = IconLabel(size_hint_x=None, width=100, color=(0, 0, 0, 1))
        self.update_time()
        header.add_widget(self.time_label)

        spacer_left = BoxLayout(size_hint_x=1)
        header.add_widget(spacer_left)

        header.add_widget(Label(text='Drifting Bottle', size_hint_x=None, width=200, halign='center', color=(0, 0, 0, 1)))

        spacer_right = BoxLayout(size_hint_x=1)
        header.add_widget(spacer_right)

        settings_button = Button(background_normal='assets/settings.png', size_hint=(None, None), size=(90, 90))
        settings_button.bind(on_press=self.go_to_settings)
        header.add_widget(settings_button)

        main_layout.add_widget(header)

        middle_content = Label(
            text='No messages right now\nYou can change the background color in Settings',
            color=(0, 0, 0, 1),
            valign='middle'
            )


        main_layout.add_widget(middle_content)

        footer = BoxLayout(size_hint_y=None, height=50, orientation='horizontal',
                           spacing=(Window.width - (3 * 120)) / 7)
        
        bottle_button = Button(background_normal='assets/bottle.png', size_hint=(None, None), size=(120, 120))
        bottle_button.bind(on_press=self.go_to_create_bottle)
        footer.add_widget(bottle_button)
        
        search_button = Button(background_normal='assets/loupe.png', size_hint=(None, None), size=(120, 120))
        search_button.bind(on_press=self.go_to_search)
        footer.add_widget(search_button)

        profile_button = Button(background_normal='assets/user.png', size_hint=(None, None), size=(120, 120))
        profile_button.bind(on_press=self.go_to_profile)
        footer.add_widget(profile_button)

        with footer.canvas.before:
            Color(251/255, 255/255, 241/255, .7) 
            self.footer_background = Rectangle(pos=footer.pos, size=(Window.width, 120))

        footer.bind(pos=self.update_background, size=self.update_background)

        main_layout.add_widget(footer)
        self.add_widget(main_layout)
        
        Clock.schedule_interval(self.update_time, 1)

    def update_background(self, instance, value):
        self.footer_background.pos = instance.pos
        self.footer_background.size = (Window.width, 120)

    def update_time(self, *args):
        self.time_label.text = datetime.now().strftime('%H:%M:%S')

    def go_to_create_bottle(self, instance):
        self.manager.current = 'create_bottle'

    def go_to_profile(self, instance):
        self.manager.current = 'profile_page'

    def go_to_settings(self, instance):
        self.manager.current = 'settings'

    def go_to_search(self, instance):
        self.manager.current = 'search'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main_page'))
        return sm