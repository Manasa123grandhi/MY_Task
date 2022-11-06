import datetime
import time

import pytest
from library.excel_lib import ReadExcel
from POM.trainmodule import TrainModule
from library.config import Config




class TestTrainModule:
    read_xl = ReadExcel()
    data = read_xl.read_testdata(Config.TRAIN_TESTDATA_SHEET)
    @pytest.mark.parametrize("From_text, To_text, User_id_text, Name_text, Age_text, Mobile_text, Email_text", data)
    def test_train_module(self, From_text, To_text, User_id_text, Name_text, Age_text, Mobile_text, Email_text, init_driver):
        driver = init_driver

        try:
            tm = TrainModule(driver)
            tm.enter_From_text(From_text)
            time.sleep(2)
            tm.click_From()
            tm.enter_To_text(To_text)
            time.sleep(2)
            tm.click_TO()
            time.sleep(2)
            tm.click_tomarrow()
            time.sleep(2)
            # driver.implicitly_wait(10)
            tm.click_Search_btn()
            tm.click_ticket()
            tm.click_Check_box()
            time.sleep(2)
            tm.enter_User_id(User_id_text)
            time.sleep(2)
            # tm.enter_User_id_text_field(User_id_text)
            tm.click_Valid_id()
            time.sleep(2)
            tm.click_AddTravel_btn()
            time.sleep(2)
            tm.click_Gen_female()
            time.sleep(2)
            tm.enter_Name_text(Name_text)
            time.sleep(2)
            # tm.enter_Name_text_field(Name_text)
            tm.enter_Age_text(Age_text)
            time.sleep(2)
            # tm.enter_Age_text_field(Age_text)
            tm.click_Breath_drop()
            time.sleep(2)
            tm.click_Upper_btn()
            time.sleep(2)
            tm.click_Save_btn()
            time.sleep(2)
            tm.enter_Mobile_text(Mobile_text)
            time.sleep(2)
            # tm.enter_Mobile_text_field(Mobile_text)
            # tm.click_Email_text_field()
            tm.enter_Email_text(Email_text)
            time.sleep(2)
            tm.click_label_text_field()
            time.sleep(2)
            tm.click_Booknow_button()
            time.sleep(2)
            tm.click_UPI_drop_button()
            time.sleep(2)
            tm.click_Barcode_button()
            # rp = RegisterPage(initdriver)
            # tm.enter_From_text_field(From_text)
            # tm.enter_To_text_field(To_text)
            # tm.click_To_text_field()
            # tm.click_Search_button()
            # tm.click_Check_box()
            # tm.click_User_id_text_field()
            # tm.enter_User_id_text_field(User_id_text)
            # tm.click_Valid_id_button()
            # tm.click_AddTravels_button()
            # tm.click_Gen_female_button()
            # tm.click_Name_text_field()
            # tm.enter_Name_text_field(Name_text)
            # tm.click_Age_text_field()
            # tm.enter_Age_text_field(Age_text)
            # tm.click_Breath_drop_button()
            # tm.click_Upper_button()
            # tm.click_Save_button()
            # tm.click_Mobile_text_field()
            # tm.enter_Mobile_text_field(Mobile_text)
            # tm.click_Email_text_field()
            # tm.enter_Email_text_field(Email_text)
            # tm.click_label_text_field()
            # tm.click_Booknow_button()
            # tm.click_UPI_drop_button()
            # tm.click_Barcode_button()

        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOTS_PATH + name)
            raise error_msg
