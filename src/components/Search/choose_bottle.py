from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class ChooseBottle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, pos_hint={'center_x': 0.5, 'center_y': .5})

        # Back button at the top
        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        image = Image(source='assets/bottle.png')  # Replace with the actual path to your image
        layout.add_widget(image)

        # Save and Find buttons
        button_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        select_button = Button(text='SELECT')
        select_button.bind(on_press=self.go_open)
        throw_back_button = Button(text='THROW BACK')
        throw_back_button.bind(on_press=self.go_search)
        button_box.add_widget(select_button)
        button_box.add_widget(throw_back_button)
        layout.add_widget(button_box)

        # Add the main layout to the screen
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main_page'

    def go_search(self, instance):
        self.manager.current = 'search'

    def go_open(self,instance):
        self.manager.current = 'open'
