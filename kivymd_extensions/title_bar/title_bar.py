from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.material_resources import DEVICE_TYPE

import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.properties import ListProperty, BooleanProperty, StringProperty
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.logger import Logger

import os

with open(
        os.path.join(os.path.dirname(__file__), "title_bar.kv"),
        encoding="utf-8",
) as kv:
    Builder.load_string(kv.read())


class MDTitleBar(MDBoxLayout):
    title_color = ListProperty()
    """
    :attr:`title_color` is an :class:`~kivy.properties.ListProperty`
    and defaults to `[]`.
    """

    title_halign = StringProperty('left')
    """
    :attr:`title_halign` is an :class:`~kivy.properties.StringProperty`
    and defaults to `left`.
    """

    separator = BooleanProperty(True)
    """
    :attr:`title_color` is an :class:`~kivy.properties.BooleanProperty`
    and defaults to `True`, if `False` separator will be delete.
    """

    icon = StringProperty(os.path.join(os.path.dirname(kivy.__file__), 'data', 'logo', 'kivy-icon-64.png'),
                          allownone=True
                          )
    """
    :attr:`icon` is an :class:`~kivy.properties.StringProperty`
    and defaults to `kivy-icon-64.png`, `None` allowed.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        App.get_running_app().bind(icon=self._change_icon)
        self.window_size = None, None

        self._set_custom_titlebar()
        Clock.schedule_once(self._remove_separator)

    def _set_custom_titlebar(self):
        if DEVICE_TYPE == 'desktop':
            if not Window.custom_titlebar:
                Window.custom_titlebar = True

                if Window.set_custom_titlebar(self):
                    return
            else:
                Logger.warning("Window: titlebar already added")
                return

        Clock.schedule_once(lambda dt: self._rm_widget())
        Logger.error("Window: setting custom titlebar Not allowed on this system")

    def _rm_widget(self):
        self.clear_widgets()
        self.height = 0

    def _remove_separator(self, dt: float):
        if not self.separator:
            self.remove_widget(self.ids.separator)

    def _change_icon(self, inst, icon: str):
        """
        if `MDTitleBar` icon is `None`, so the change in the application `icon` should not be reflected on the widget
        """

        if self.icon:
            self.icon = icon

    @staticmethod
    def roll_up(inst):
        inst.anim_complete()
        Window.minimize()

    def restore(self, inst):
        inst.anim_complete()

        if all(not x for x in self.window_size):
            Window.maximize()
            self.window_size = Window.size
        else:
            if Window.size == self.window_size:
                Window.restore()
            else:
                Window.maximize()
                self.window_size = Window.size
