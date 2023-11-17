# main_page.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Footer with icons
        footer = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')
        bottle_button = Button(background_normal='bottle.jpg')
        bottle_button.bind(on_press=self.go_to_create_bottle)
        footer.add_widget(bottle_button)
        footer.add_widget(Button(background_normal='search.png'))
        footer.add_widget(Button(background_normal='person.png'))

        layout.add_widget(footer)
        self.add_widget(layout)

    def go_to_create_bottle(self, instance):
        self.manager.current = 'create_bottle'
