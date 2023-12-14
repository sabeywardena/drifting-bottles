from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainPage(Screen):
    pass

class ProfilePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)

        self.layout.add_widget(back_button)

        self.user_score_label = Label(text='User score: 100', size_hint_y=None, height=50)

        edit_btn = Button(text='Edit', size_hint=(None, None), size=(100, 50))
        edit_btn.bind(on_press=self.toggle_editing)

        save_btn = Button(text='Save', size_hint=(None, None), size=(100, 50))
        save_btn.bind(on_press=self.save_profile)

        button_layout = BoxLayout(size_hint_y=None, height=50)
        button_layout.add_widget(edit_btn)
        button_layout.add_widget(save_btn)

        self.layout.add_widget(self.user_score_label)
        self.layout.add_widget(button_layout)

        self.layout.add_widget(Label(size_hint=(1, None), height=80))

        self.details_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=200, spacing=10, padding=20)
        self.name_input = TextInput(hint_text='Name', size_hint_y=None, height=60, readonly=True)
        self.age_input = TextInput(hint_text='Age', size_hint_y=None, height=60, readonly=True)
        self.gender_input = TextInput(hint_text='Gender', size_hint_y=None, height=60, readonly=True)
        self.email_input = TextInput(hint_text='Email', size_hint_y=None, height=60, readonly=True)

        self.details_layout.add_widget(self.name_input)
        self.details_layout.add_widget(self.age_input)
        self.details_layout.add_widget(self.gender_input)
        self.details_layout.add_widget(self.email_input)

        self.layout.add_widget(self.details_layout)

        self.layout.add_widget(Label(text='Bio:', size_hint_y=None, height=30))
        self.bio_input = TextInput(size_hint_y=None, height=100, multiline=True, readonly=True)
        self.layout.add_widget(self.bio_input)

        self.layout.add_widget(Label(text='Hobby:', size_hint_y=None, height=30))
        self.hobby_input = TextInput(size_hint_y=None, height=100, multiline=True, readonly=True)
        self.layout.add_widget(self.hobby_input)

        self.add_widget(self.layout)

        self.edit_mode = False
        self.disable_inputs()

    def toggle_editing(self, instance):
        self.edit_mode = not self.edit_mode
        if self.edit_mode:
            self.enable_inputs()
        else:
            self.disable_inputs()

    def enable_inputs(self):
        for input_field in [self.name_input, self.age_input, self.gender_input, self.email_input,
                            self.bio_input, self.hobby_input]:
            input_field.readonly = False
            input_field.background_color = (1, 1, 1, 1)

    def disable_inputs(self):
        for input_field in [self.name_input, self.age_input, self.gender_input, self.email_input,
                            self.bio_input, self.hobby_input]:
            input_field.readonly = True
            input_field.background_color = (0.7, 0.7, 0.7, 1)

    def save_profile(self, instance):
        if self.edit_mode:
            print(f"Name: {self.name_input.text}")
            print(f"Age: {self.age_input.text}")
            print(f"Gender: {self.gender_input.text}")
            print(f"Email: {self.email_input.text}")
            print(f"Bio: {self.bio_input.text}")
            print(f"Hobby: {self.hobby_input.text}")

            # Disable editing after saving
            self.toggle_editing(None)

    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_page'

class ProfileApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage(name='main_page'))
        sm.add_widget(ProfilePage(name='profile'))
        return sm

if __name__ == '__main__':
    ProfileApp().run()
