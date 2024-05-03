# MyLibrary/__init__.py

from .Button import Button


class MyLibrary:
    def __init__(self):
        self.my_button = Button(10, 20, "My Button")

    def click_my_button(self):
        self.my_button.click()
