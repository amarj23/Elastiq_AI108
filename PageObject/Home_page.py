from selenium.webdriver.common.by import By


class Home_Page:
    Text_search_box = '//*[@id="example_filter"]/label/input'
    Text_table_xpath = '//*[@id="example"]/tbody/tr'
    Text_entries = "//*[@id = 'example_info']"

    def __init__(self, driver):
        self.driver = driver

    def entries(self):
        text = self.driver.find_element(By.XPATH, "//*[@id = 'example_info']")

    def table_rows(self):
        lenth = len(self.driver.find_elements(By.XPATH, self.Text_table_xpath))
        return lenth

    def search_box(self):
        self.driver.find_element(By.XPATH, self.Text_search_box).send_keys('New York')


