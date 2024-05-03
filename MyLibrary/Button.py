# MyLibrary/Button.py

from .BaseWidget import BaseWidget


class Button(BaseWidget):
    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.label = label

    def click(self):
        print(f"Clicked {self.label}")
