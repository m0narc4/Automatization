from base.base_element import BaseElement


class Button(BaseElement):
    def send_keys(self, text):
        self.find_element().send_keys(text)