from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import Screen

class SearchBottle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Back button at the top
        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        # Section title for age
        layout.add_widget(Label(text='Age', size_hint_y=None, height=30))

        # Age slider
        age_slider = Slider(min=0, max=100, value=20, size_hint_y=None, height=50)
        layout.add_widget(age_slider)

        # Section title for gender
        layout.add_widget(Label(text='Gender', size_hint_y=None, height=30))

        # Gender checkboxes
        gender_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        male = CheckBox(group='gender')
        female = CheckBox(group='gender')
        other = CheckBox(group='gender')
        gender_layout.add_widget(Label(text='M'))
        gender_layout.add_widget(male)
        gender_layout.add_widget(Label(text='F'))
        gender_layout.add_widget(female)
        gender_layout.add_widget(Label(text='Other'))
        gender_layout.add_widget(other)
        layout.add_widget(gender_layout)

        # Section title for title
        layout.add_widget(Label(text='Title', size_hint_y=None, height=30))

        # Title text input
        title_input = TextInput(text='', multiline=False, size_hint_y=None, height=50)
        layout.add_widget(title_input)

        # Save and Find buttons
        button_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        save_button = Button(text='SAVE')
        find_button = Button(text='FIND')
        button_box.add_widget(save_button)
        button_box.add_widget(find_button)
        layout.add_widget(button_box)

        # Add the main layout to the screen
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main_page'

class SearchBottleApp(App):
    def build(self):
        return SearchBottle()

if __name__ == '__main__':
    SearchBottleApp().run()
