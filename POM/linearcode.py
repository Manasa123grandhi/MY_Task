import time
from telnetlib import EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver


# from selenium.webdriver.common.action_chains import ActionChains

path = r"C:\Users\DELL\PycharmProjects\HTD_project\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.implicitly_wait(30)
file_path = r"https://www.goibibo.com/trains/"
driver.get(file_path)
driver.maximize_window()

driver.find_element("xpath", '(//input[@type="text"])[1]').send_keys("SBC")
# # time.sleep(1)
driver.find_element("xpath", '//span[text()="SBC"]').click()
# # time.sleep(1)
driver.find_element("xpath", '(//input[@type="text"])[2]').send_keys("NDLS")
# # time.sleep(1)
driver.find_element("xpath", '//span[text()="NDLS"]').click()
driver.find_element("xpath", '//span[text()="Tomorrow"]').click()
# driver.find_element("xpath", '(//p[text()="Date"])[1]').click()
# ticket = driver.find_element("xpath", "(//span[@class='ico14 fb txtCenter width100 black']/../..//span[text()='GENERAL'])[1]").click()
# ticket.click()
driver.find_element("xpath", '//button[@class="searchBtn curPointer"]').click()

driver.execute_script("arguments[0].click()",driver.find_element("xpath", '//div[@class="trainClassHeader general"]//span[text()="2A"]/..'))
# driver.find_element("xpath",'//div[@class="trainClassHeader general"]//span[text()="2A"]/..').click()
# driver.find_element("xpath", '/html/body/div[2]/div/section[2]/section[2]/section/div[3]/ul/li[2]/div/div[2]/p[2]/span[1]').click()
# driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH, '//div[@class="trainClassHeader general"]//span[text()="2A"]/..'))


# driver.find_element("xpath", '//p[text()="24 Nov 22"]').click()
# # driver.find_element("xpath", '//div[@class="DayPicker-Day txtCenter DayPicker-Day--selected availabilityStatus"]').click()
# driver.find_element("xpath", '(//div[contains(text()=24)])[1]').click()
# driver.find_element("xpath", '(//p[text()="Date"])[1]').click()
# driver.find_element("xpath", '//div[text()="20"]').click()
# driver.find_element("xpath", '//div[@id="gi-special-theme-center"]').click()
# time.sleep(1)
# driver.find_element('class name', 'widgetInput.width100.textInput.width100').click()
# # driver.find_element("xpath", '//p[@class="widgetInput width100 textInput width100"]').click()0
# time.sleep(5)
# # driver.find_element("xpath", '''//div[@class="DayPicker-Body"]//div[text()='31']''').click()
# # # time.sleep(1)
# # driver.find_element("xpath", '//p[@class="widgetInput width100 textInput width100"]').click()
# driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()
# time.sleep(1)
# day_ = driver.find_element("xpath", '''//div[@class="DayPicker-Body"]//div[text()='3']''')
# day_obj = ActionChains(driver)
# day_obj.click().perform()
# time.sleep(2)
# driver.find_element("xpath", '(//input[@name="day"])[2]').click()
# driver.find_element("xpath", '//aside[@class="searchButtonWrap"]').click()
# driver.find_element('xpath', "//h3[text()='Rajdhani Exp']/../../..//span[text()='1A']").click()
# driver.find_element("xpath", '//div[@class="menu-wrapper"]/..//ul[@id="menu0"]').click()
# # time.sleep(4)
# # driver.find_element("xpath",'(//h3[contains(text(),"22691")]/../../..//li[@title="Tap to book"])[1]').click()
# # time.sleep(1)
# # driver.implicitly_wait(10)
# # driver.find_element("xpath", '(//div[@class="trainClassContent"])[1]').click()
# # time.sleep(1)
# time.sleep(3)
# driver.find_element("xpath", "(//span[@class='ico14 fb txtCenter width100 black']/../../..//div[@class='cardWrap '])[3]").click()
# WebDriverWait(driver, 20).until(expected_conditions.element_to_be_clickable(locator)).click()


#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='documentType-0']"))).click()
driver.find_element("xpath", '//p[text()="Yes, I am interested"]').click()
driver.find_element("xpath", '//input[@placeholder="Enter IRCTC User ID"]').send_keys("sai123")
driver.find_element("xpath", '//button[@class="irctcUsrIdVr__chkIdBtn null"]').click()
driver.find_element("xpath", '//button[@class="addTrvlrComp__addBtn"]').click()
driver.find_element("xpath",'//button[text()="Female"]').click()
driver.find_element("xpath", '//input[@placeholder="Enter Name"]').send_keys("Sai Charitha")
driver.find_element("xpath", '//input[@type="number"]').send_keys("23")
driver.find_element("xpath", '//span[@class="addTrvlrMdl__drpDwnIcnWrp"]').click()
driver.find_element("xpath", '//label[text()="UPPER BERTH"]').click()
driver.find_element("xpath", '//button[text()="Save"]').click()
# driver.find_element("xpath", '//input[@placeholder="Enter Mobile Number"]').click()
driver.find_element("xpath", '//input[@placeholder="Enter Mobile Number"]').send_keys("1234567890")
# driver.find_element("xpath", '//input[@placeholder="Enter Email Address"]').click()
driver.find_element("xpath", '//input[@placeholder="Enter Email Address"]').send_keys("sai@gmail.com")
driver.find_element("xpath", '(//label[@class="padT2"])[1]').click()
driver.find_element("xpath", '//button[text()="Book now"]').click()
# driver.find_element("xpath", '//button[@class="bkRvwPgWrap__arDwnBtn"]').click()
driver.find_element("xpath", '(//span[@class="fr"])[1]').click()
driver.find_element("xpath", '//img[@id="upiBarcode"]').click()
