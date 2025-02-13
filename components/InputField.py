from base.base_element import BaseElement


class InputField(BaseElement):
    def send_keys(self, text):
        self.find_element().send_keys(text)

    def get_attribute(self, attribute):
        return self.find_element().get_attribute(attribute)