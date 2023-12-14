from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

class CreateBottle(Screen):
    def __init__(self, window_size=(300, 500), **kwargs):
        super().__init__(**kwargs)

        self.size = window_size
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(None, None), size=self.size)

        layout.add_widget(Label(text='Create a Bottle Message', size_hint_y=None, height=50))

        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        anonymous_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)

        anonymous_label = Label(text='Anonymous:', size_hint_x=None, width=100, color=(0, 0, 0, 1))
        self.anonymous = CheckBox(size_hint_x=None, width=50)  # Adjust the width as needed
        anonymous_layout.add_widget(anonymous_label)
        anonymous_layout.add_widget(self.anonymous)
        
        toggle_button = Button(text='Toggle', size_hint_x=None, width=100)
        toggle_button.bind(on_press=lambda instance: self.toggle_checkbox_state(self.anonymous, toggle_button))
        
        anonymous_layout.add_widget(toggle_button)
        layout.add_widget(anonymous_layout)

        layout.add_widget(Label(text='Age Range:', size_hint_y=None, height=30))
        self.lowest_age_input = TextInput(hint_text='Lowest Age', multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.lowest_age_input)
        self.highest_age_input = TextInput(hint_text='Highest Age', multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.highest_age_input)

        layout.add_widget(Label(text='Description:', size_hint_y=None, height=30))
        self.description_input = TextInput(text='', multiline=True, size_hint_y=None, height=150)
        layout.add_widget(self.description_input)

        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        button_layout.add_widget(Button(text='Save'))
        send_button = Button(text='Send')
        send_button.bind(on_press=self.on_send_pressed)
        button_layout.add_widget(send_button)
        layout.add_widget(button_layout)

        self.add_widget(layout)

    def toggle_checkbox_state(self, checkbox, toggle_button):
        checkbox.active = not checkbox.active
        if checkbox.active:
            toggle_button.background_color = (0, 1, 0, 1)
        else:
            toggle_button.background_color = (0.7, 0.7, 0.7, 1)

    def on_send_pressed(self, instance):
        self.show_notification("Message sent! Returning to the main page in 3 seconds.")
        Clock.schedule_once(lambda dt: self.go_back(None), 3)

    def show_notification(self, message):
        popup = Popup(title='Notification',
                      content=Label(text=message),
                      size_hint=(None, None), size=(300, 100))
        popup.open()

    def go_back(self, instance):
        self.manager.current = 'main_page'

class CreateBottleApp(App):
    def build(self):
        return CreateBottle(window_size=(300, 500))

if __name__ == '__main__':
    CreateBottleApp().run()
