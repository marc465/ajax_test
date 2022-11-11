class Page:

    def __init__(self, driver):
        self.driver = driver


    def find_element(self, xpath: str):
        """
        Шукає елемент на сторінці за XPATH
        """
        return self.driver.find_element_by_xpath(xpath)


    def click_element(self, xpath: str):
        """
        Натискає на переданий елемент
        """
        self.driver.find_element_by_xpath(xpath).clik()


    def input_data(self, element, data):
        """
        Вводить дані в зазначене поле
        """
        element.clear()
        element.send_keys(data)


    def is_element_there(self, xpath: str):
        """
        Повертає True, якщо елемент знайдений на сторінці і False у зворотному випадку
        """
        try:
            self.driver.find_element_by_xpath(xpath)
            return True
        except:
            return False
