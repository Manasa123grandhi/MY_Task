import re
import time

from library.excel_lib import ReadExcel
from library.config import Config


class TrainModule:

    read_xl = ReadExcel()
    locator_train = read_xl.read_locators(Config.TRAIN_LOCATORS_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def enter_From_text(self,From_text):
        locator = self.locator_train["enter_From_text"]
        self.driver.find_element(*locator).send_keys(From_text)

    def click_From(self):
        locator = self.locator_train["click_From"]
        self.driver.find_element(*locator).click()

    def enter_To_text(self,To_text):
        locator = self.locator_train["enter_To_text"]
        self.driver.find_element(*locator).send_keys(To_text)

    def click_TO(self):
        locator = self.locator_train["click_TO"]
        self.driver.find_element(*locator).click()

    def click_tomarrow(self):
        locator = self.locator_train["click_tomarrow"]
        self.driver.find_element(*locator).click()
    def click_Search_btn(self):
        locator = self.locator_train["click_Search_btn"]
        self.driver.find_element(*locator).click()

    def click_ticket(self):
        locator=self.locator_train["click_ticket"]
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(*locator))
        # self.driver.find_element(*locator).click()

    def click_Check_box(self):
        locator = self.locator_train["click_Check_box"]
        self.driver.find_element(*locator).click()

    def enter_User_id(self,User_id_text):
        locator = self.locator_train["enter_User_id"]
        self.driver.find_element(*locator).send_keys(User_id_text)


    # def enter_User_id_text_field(self,User_id_text):
    #     locator = self.locator_train["enter_User_id_text_field"]
    #     self.driver.find_element(*locator).send_keys(User_id_text)

    def click_Valid_id(self):
        locator = self.locator_train["click_Valid_id"]
        self.driver.find_element(*locator).click()

    def click_AddTravel_btn(self):
        locator = self.locator_train["click_AddTravel_btn"]
        self.driver.find_element(*locator).click()

    def click_Gen_female(self):
        locator = self.locator_train["click_Gen_female"]
        self.driver.find_element(*locator).click()

    def enter_Name_text(self,Name_text):
        locator = self.locator_train["enter_Name_text"]
        self.driver.find_element(*locator).send_keys(Name_text)

    # def enter_Name_text_field(self,Name_text):
    #     locator = self.locator_train["enter_Name_text_field"]
    #     self.driver.find_element(*locator).send_keys(Name_text)

    def enter_Age_text(self,Age_text):
        locator = self.locator_train["enter_Age_text"]
        self.driver.find_element(*locator).send_keys(Age_text)

    # def enter_Age_text_field(self,Age_text):
    #     locator = self.locator_train["enter_Age_text_field"]
    #     self.driver.find_element(*locator).send_keys(Age_text)

    def click_Breath_drop(self):
        locator = self.locator_train["click_Breath_drop"]
        self.driver.find_element(*locator).click()

    def click_Upper_btn(self):
        locator = self.locator_train["click_Upper_btn"]
        self.driver.find_element(*locator).click()

    def click_Save_btn(self):
        locator = self.locator_train["click_Save_btn"]
        self.driver.find_element(*locator).click()

    def click_Mobile_text_field(self):
        locator = self.locator_train["enter_Mobile_text_field"]
        self.driver.find_element(*locator).click()

    def enter_Mobile_text(self,Mobile_text):
        if isinstance(Mobile_text,float):
            Mobile_text = str(int(Mobile_text))
        assert len(Mobile_text) == 10
        locator = self.locator_train["enter_Mobile_text"]
        self.driver.find_element(*locator).send_keys(Mobile_text)

    def click_Email_text_field(self):
        locator = self.locator_train["enter_Email_text_field"]
        self.driver.find_element(*locator).click()

    def enter_Email_text(self, Email_text ):
        time.sleep(3)
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern,Email_text)
        assert result !=[], "invalid email"
        locator = self.locator_train["enter_Email_text"]
        self.driver.find_element(*locator).send_keys(Email_text)

    def click_label_text_field(self):
        locator = self.locator_train["click_label_text_field"]
        self.driver.find_element(*locator).click()

    def click_Booknow_button(self):
        locator = self.locator_train["click_Booknow_btn"]
        self.driver.find_element(*locator).click()

    def click_UPI_drop_button(self):
        locator = self.locator_train["click_UPI_drop_btn"]
        self.driver.find_element(*locator).click()

    def click_Barcode_button(self):
        locator = self.locator_train["click_Barcode_btn"]
        self.driver.find_element(*locator).click()


















