from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class ProfilePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, pos_hint={'center_x': 0.5, 'center_y': .7})

        # Add elements at the beginning
        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)

        user_score_label = Label(text='User score: 100', size_hint_y=None, height=50)

        edit_btn = Button(text='Edit', size_hint=(None, None), size=(100, 50))

        # Add the elements to the layout
        layout.add_widget(back_button)
        layout.add_widget(user_score_label)
        layout.add_widget(edit_btn)

        # Spacer to create space between the elements above and details_layout
        layout.add_widget(Label(size_hint=(1, None), height=80))

        details_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=200, spacing=10, padding=20)
        details_layout.add_widget(TextInput(hint_text='Name', size_hint_y=None, height=60))
        details_layout.add_widget(TextInput(hint_text='Age', size_hint_y=None, height=60))
        details_layout.add_widget(TextInput(hint_text='Gender', size_hint_y=None, height=60))
        details_layout.add_widget(TextInput(hint_text='Email', size_hint_y=None, height=60))
        layout.add_widget(details_layout)

        # Bio
        layout.add_widget(Label(text='Bio:', size_hint_y=None, height=30))
        layout.add_widget(TextInput(size_hint_y=None, height=100, multiline=True))

        # Hobby
        layout.add_widget(Label(text='Hobby:', size_hint_y=None, height=30))
        layout.add_widget(TextInput(size_hint_y=None, height=100, multiline=True))

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'main_page'
