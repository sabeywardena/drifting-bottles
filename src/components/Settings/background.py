from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.colorpicker import ColorPicker
from kivy.core.window import Window

class Background(Screen):
    def __init__(self, color_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.color_callback = color_callback

        initial_color = (0, 0, 1, 1)
        Window.clearcolor = initial_color

        main_layout = BoxLayout(orientation='vertical', spacing=10)
        back_button = Button(text='Back', size_hint=(1, 0.1))
        back_button.bind(on_press=self.go_back)
        main_layout.add_widget(back_button)

        color_picker = ColorPicker(size_hint=(1, 0.8))
        color_picker.bind(color=self.on_color)
        main_layout.add_widget(color_picker)

        self.add_widget(main_layout)

    def go_back(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'settings'

    def on_color(self, instance, value):
        if self.color_callback:
            self.color_callback(value)