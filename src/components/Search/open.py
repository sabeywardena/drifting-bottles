from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Open(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, pos_hint={'center_x': 0.5, 'center_y': 1})

        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        layout.add_widget(
            Label(text='Anyone want to go explore boston this weekend?', size_hint_y=None, height=30, font_size=30))

        reply_button = Button(text='Reply', size_hint_y=None, height=50)
        reply_button.bind(on_press=self.go_back)
        layout.add_widget(reply_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main_page'
