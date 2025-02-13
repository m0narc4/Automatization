from SeleniumWait import Wait


class BaseElement:
    def __init__(self, locator):
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return Wait.visibility(self.locator)

    def get_text(self):
        return self.find_element().text