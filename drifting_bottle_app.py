
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider

class DriftingBottleForm(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Add the age slider
        self.add_widget(Label(text='Age:'))
        self.age_slider = Slider(min=0, max=100, value=20)
        self.add_widget(self.age_slider)

        # Add the gender checkboxes
        self.add_widget(Label(text='Gender:'))
        gender_layout = BoxLayout(orientation='horizontal')
        self.male = CheckBox(group='gender')
        self.female = CheckBox(group='gender')
        self.other = CheckBox(group='gender')
        gender_layout.add_widget(Label(text='M'))
        gender_layout.add_widget(self.male)
        gender_layout.add_widget(Label(text='F'))
        gender_layout.add_widget(self.female)
        gender_layout.add_widget(Label(text='Other'))
        gender_layout.add_widget(self.other)
        self.add_widget(gender_layout)

        # Add the anonymous checkbox
        self.anonymous = CheckBox()
        self.add_widget(Label(text='Anonymous:'))
        self.add_widget(self.anonymous)

        # Add the description text input
        self.add_widget(Label(text='Description:'))
        self.description = TextInput(text='Looking for a study partner for chem 101!')
        self.add_widget(self.description)

        # Add save and send buttons
        button_layout = BoxLayout(orientation='horizontal')
        save_button = Button(text='Save')
        send_button = Button(text='Send')
        button_layout.add_widget(save_button)
        button_layout.add_widget(send_button)
        self.add_widget(button_layout)

class DriftingBottleApp(App):
    def build(self):
        return DriftingBottleForm()

if __name__ == '__main__':
    DriftingBottleApp().run()
