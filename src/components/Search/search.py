from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

class RangeSliderApp(App):
    def build(self):
        return SearchBottle()

class SearchBottle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, pos_hint={'center_x': 0.5, 'center_y': 1})

        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        layout.add_widget(Label(text='Age Range', size_hint_y=None, height=30))

        self.lowest_age_input = TextInput(hint_text='Lowest Age', multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.lowest_age_input)

        self.highest_age_input = TextInput(hint_text='Highest Age', multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.highest_age_input)

        layout.add_widget(Label(text='Preferences', size_hint_y=None, height=30))

        self.game_title_input = TextInput(hint_text='Preferred Title', multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.game_title_input)

        self.gaming_platform_input = TextInput(hint_text='Time', multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.gaming_platform_input)

        button_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        save_button = Button(text='SAVE')
        find_button = Button(text='FIND')
        find_button.bind(on_press=self.go_to_choose)
        button_box.add_widget(save_button)
        button_box.add_widget(find_button)
        layout.add_widget(button_box)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main_page'

    def go_to_choose(self, instance):
        lowest_age = self.lowest_age_input.text
        highest_age = self.highest_age_input.text
        preferred_game_title = self.game_title_input.text
        gaming_platform = self.gaming_platform_input.text

        print(f"Lowest Age: {lowest_age}")
        print(f"Highest Age: {highest_age}")
        print(f"Preferred Game Title: {preferred_game_title}")
        print(f"Gaming Platform: {gaming_platform}")

        self.manager.current = 'choose_bottle'

if __name__ == '__main__':
    RangeSliderApp().run()
