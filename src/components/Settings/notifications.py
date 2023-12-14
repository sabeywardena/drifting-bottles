from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton

class Notifications(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.show_notifications = False

        layout = BoxLayout(orientation='vertical', size=(300, 500), spacing=20, pos_hint={'center_y': 1})

        back_button = Button(text='Back', size_hint_y=None, height=50)
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

        toggle_button = ToggleButton(text='Show notification when you open the App', size_hint_y=None, height=50)
        toggle_button.bind(on_release=self.toggle_notifications)
        layout.add_widget(toggle_button)

        self.notifications_label = Label(text='', size_hint_y=None, height=150)
        layout.add_widget(self.notifications_label)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'settings'

    def toggle_notifications(self, instance):
        self.show_notifications = not self.show_notifications
        self.display_notifications() if self.show_notifications else self.hide_notifications()

    def display_notifications(self):
        new_notification = "You have a new message!"
        self.notifications.append(new_notification)

        if self.show_notifications:
            if self.notifications:
                notification_text = "\n".join(self.notifications)
                self.notifications_label.text = notification_text
            else:
                self.notifications_label.text = "No new notifications."

    def hide_notifications(self):
        self.notifications_label.text = ""  
