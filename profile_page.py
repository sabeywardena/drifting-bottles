from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

class ProfilePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # User score
        layout.add_widget(Label(text='User score: 100', size_hint_y=None, height=30))

        # Profile details
        edit_btn = Button(text='Edit', size_hint=(None, None), size=(100, 50))
        layout.add_widget(edit_btn)

        details_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=5)
        details_layout.add_widget(TextInput(hint_text='Name', size_hint_y=None, height=30))
        details_layout.add_widget(TextInput(hint_text='Age', size_hint_y=None, height=30))
        details_layout.add_widget(TextInput(hint_text='Gender', size_hint_y=None, height=30))
        details_layout.add_widget(TextInput(hint_text='Email', size_hint_y=None, height=30))
        layout.add_widget(details_layout)

        # Bio
        layout.add_widget(Label(text='Bio:', size_hint_y=None, height=30))
        layout.add_widget(TextInput(size_hint_y=None, height=100, multiline=True))

        # Hobby
        layout.add_widget(Label(text='Hobby:', size_hint_y=None, height=30))

        # Footer with icons (placeholder for now)
        footer = BoxLayout(size_hint_y=None, height=50)
        footer.add_widget(Button(background_normal='bottle.png', size_hint=(None, None), size=('50dp', '50dp')))
        footer.add_widget(Button(background_normal='search.png', size_hint=(None, None), size=('50dp', '50dp')))
        footer.add_widget(Button(background_normal='person.png', size_hint=(None, None), size=('50dp', '50dp')))
        layout.add_widget(footer)

        self.add_widget(layout)

    # You would add functions to handle editing and saving profile details here.
