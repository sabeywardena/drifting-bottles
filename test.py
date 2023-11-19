from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.window import Window


class ImageButton(ButtonBehavior, Image):
    pass


class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Header with the title, WiFi/battery indicators, and settings icon
        header = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')
        header.add_widget(Label(text='9:59', size_hint_x=None, width=100))
        header.add_widget(Label(text='Drifting Bottle', halign='center'))

        # Right part of the header for icons
        icons_layout = BoxLayout(orientation='vertical', size_hint_x=None, width=50)
        icons_layout.add_widget(Image(source='wifi.png', allow_stretch=True, keep_ratio=False))
        icons_layout.add_widget(Image(source='setting.png', allow_stretch=True, keep_ratio=False))
        header.add_widget(icons_layout)

        self.add_widget(header)

        # Message label
        self.add_widget(Label(text='you dont have messages right now'))

        # Footer with the icons resized and evenly spaced
        footer = BoxLayout(size_hint_y=None, height=50, orientation='horizontal')
        footer.add_widget(ImageButton(source='bottle.jpg'))
        footer.add_widget(ImageButton(source='search.png'))
        footer.add_widget(ImageButton(source='person.png'))
        self.add_widget(footer)


class DriftingBottleApp(App):
    def build(self):
        Window.size = (360, 640)
        return HomePage()


if __name__ == '__main__':
    DriftingBottleApp().run()
