from selenium import webdriver
from degisken2.testpineDegisken import Degisken
import time


class TestRequirement():
    
    webdriver = Degisken()
    webdriver.setDriver("C:\\Users\\pc\\Desktop\\selenium\\chromedriver.exe")
    webdriver.driver.get("https://www.testpine.com/")
    print(webdriver.driver.title)
    webdriver.driver.maximize_window()
    webdriver.goToAppGit()
    webdriver.setEmail("sudesenacizmeci@gmail.com")
    webdriver.setPassword("sudeberkay1")
    webdriver.loginKonum()
    time.sleep(3)
    webdriver.driver.save_screenshot("C:\\Users\\pc\\Desktop\\selenium\\ss.png")
    time.sleep(0.5)
    webdriver.requirementKonum()
    webdriver.newRequirementEkle()
    webdriver.requirementNameYaz("practise")
    webdriver.requirementKayitOlustur()
    time.sleep(5)
    webdriver.driver.quit()
