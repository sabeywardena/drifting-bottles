# main_page.py
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.lang import Builder

class IconLabel(ButtonBehavior, Label):
    pass


class MainPage(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical')

        # Header with icons
        header = BoxLayout(size_hint_y=None, height=100, orientation='horizontal')
        time_label = IconLabel(text='9:59', size_hint_x=None, width=100)

        header.add_widget(time_label)
        header.add_widget(Label(text='Drifting Bottle', halign='center'))
        settings_button = Button(background_normal='settings.png', size_hint=(None, None), size=(90, 90))
        settings_button.bind(on_press=self.go_to_settings)
        header.add_widget(settings_button)
        main_layout.add_widget(header)

        # Middle content area
        middle_content = Label(text='you dont have messages right now')
        main_layout.add_widget(middle_content)

        # Footer with navigation icons
        footer = BoxLayout(size_hint_y=None, height=50, orientation='horizontal',
                           spacing=(Window.width - (3 * 120)) / 7)
        bottle_button = Button(background_normal='bottle.png', size_hint=(None, None), size=(120, 120))
        bottle_button.bind(on_press=self.go_to_create_bottle)
        footer.add_widget(bottle_button)
        footer.add_widget(Button(background_normal='search.png', size_hint=(None, None), size=(120, 120)))
        profile_button = Button(background_normal='person.png', size_hint=(None, None), size=(120, 120))
        profile_button.bind(on_press=self.go_to_profile)
        footer.add_widget(profile_button)

        main_layout.add_widget(footer)
        with footer.canvas.before:
            Color(251/255, 1, 241/255,.4)  # RGBA color values (adjust as needed)
            self.footer_background = Rectangle(pos=footer.pos, size=(120,Window.width))
        footer.bind(pos=self.update_background, size=self.update_background)

        self.add_widget(main_layout)

    def update_background(self, instance, value):
        self.footer_background.pos = instance.pos
        self.footer_background.size = (Window.width,130)

    def go_to_create_bottle(self, instance):
        self.manager.current = 'create_bottle'

    def go_to_profile(self, instance):
        self.manager.current = 'profile_page'

    def go_to_settings(self, instance):
        self.manager.current = 'settings'
