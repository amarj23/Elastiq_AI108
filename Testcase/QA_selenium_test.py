from PageObject.Home_page import Home_Page


class Test_reg_01:

    def test_01(self, setup):
        self.driver = setup
        self.hp = Home_Page(self.driver)
        self.hp.search_box()
        self.driver.implicitly_wait(5)
        rows = self.hp.table_rows()
        if rows == 5:
            print(f'we found {rows} entries out of 24')
            assert True
        else:
            print(f'we found {rows} entries out of 24')
            assert False

