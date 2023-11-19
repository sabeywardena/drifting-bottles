# main_page.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

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

        # Container for WiFi and Settings icons
        icons_layout = BoxLayout(orientation='vertical', size_hint_x=None, width=50)
        wifi_icon = Image(source='wifi.png', size_hint=(None, None), size=(50, 50))
        settings_icon = Image(source='setting.png', size_hint=(None, None), size=(50, 50))
        icons_layout.add_widget(wifi_icon)
        icons_layout.add_widget(settings_icon)

        header.add_widget(icons_layout)
        main_layout.add_widget(header)

        # Middle content area
        middle_content = Label(text='you dont have messages right now')
        main_layout.add_widget(middle_content)

        # Footer with navigation icons
        footer = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')
        bottle_button = Button(background_normal='bottle.png', size_hint=(None, None), size=(120, 50))
        bottle_button.bind(on_press=self.go_to_create_bottle)
        footer.add_widget(bottle_button)
        footer.add_widget(Button(background_normal='search.png', size_hint=(None, None), size=(120, 50)))
        profile_button = Button(background_normal='person.png', size_hint=(None, None), size=(120, 50))
        profile_button.bind(on_press=self.go_to_profile)
        footer.add_widget(profile_button)


        main_layout.add_widget(footer)
        self.add_widget(main_layout)

    def go_to_create_bottle(self, instance):
        self.manager.current = 'create_bottle'

    def go_to_profile(self, instance):
        self.manager.current = 'profile_page'
