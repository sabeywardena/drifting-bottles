from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import Screen

class CreateBottle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 'Back' button at the top
        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        # Title for the create bottle message
        layout.add_widget(Label(text='Create a Bottle Message', size_hint_y=None, height=50))

        # Age slider
        layout.add_widget(Label(text='Age:', size_hint_y=None, height=30))
        age_slider = Slider(min=0, max=100, value=20, size_hint_y=None, height=50)
        layout.add_widget(age_slider)

        # Gender checkboxes
        layout.add_widget(Label(text='Gender:', size_hint_y=None, height=30))
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

        # Anonymous checkbox
        anonymous_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        anonymous = CheckBox()
        anonymous_layout.add_widget(Label(text='Anonymous:'))
        anonymous_layout.add_widget(anonymous)
        layout.add_widget(anonymous_layout)

        # Description text input
        layout.add_widget(Label(text='Description:', size_hint_y=None, height=30))
        description = TextInput(text='Looking for a study partner for chem 101!', size_hint_y=None, height=150)
        layout.add_widget(description)

        # Save and send buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        save_button = Button(text='Save')
        send_button = Button(text='Send')
        button_layout.add_widget(save_button)
        button_layout.add_widget(send_button)
        layout.add_widget(button_layout)

        # Add the main layout to the screen
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main_page'

# To run the app and see this screen, you would typically have a main.py file with an App class.
# Here's a very simple example of how you could run this screen by itself:

class CreateBottleApp(App):
    def build(self):
        return CreateBottle()
    
if __name__ == '__main__':
    CreateBottleApp().run()    