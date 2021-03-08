from selenium import webdriver
from degisken3.testpineDegisken import Degisken
import time


class TestRequirement():
    
    webdriver = Degisken()
    webdriver.setDriver("C:\\Users\\pc\\Desktop\\selenium\\chromedriver.exe")
    webdriver.driver.get("https://www.testpine.com/")  #testpinecom'a gidiþ
    print(webdriver.driver.title)
    webdriver.driver.maximize_window()
    
    webdriver.findCssAndClick("body > section.hero > div > div > div.col-md-6.col-sm-12.text-md-left.text-sm-center.text-center > a") #go To App'i týklýyoruz
    webdriver.setEmail("sudesenacizmeci@gmail.com")  #geçerli mail adresi girilir
    webdriver.setPassword("sudeberkay1")  #geçerli þifre girilir.
    webdriver.findCssAndClick("body > div > div > div.col-lg-7.col-md-12.col-sm-12.col-xs-12.login-right > div.login-right-form > form > button") #login butonuna týklanýr.
    time.sleep(3)
    webdriver.driver.save_screenshot("C:\\Users\\pc\\Desktop\\selenium\\ss.png") #sayfanýn ekran görüntüsünü alýr.
    time.sleep(0.5)
    
    webdriver.findCssAndClick("body > div > div > aside > div.nav-wrapper > ul > li:nth-child(2) > a") #requirement'e týklanýr, sayfaya gidilir
    webdriver.findIdAndClick("returnList")  #yeni requirement'e týklanýr.
    webdriver.findIdAndClick("requirementName")  #requirement name alanýna gidilir.
    webdriver.requirementNameYaz("practise")  #istenilen requirement adý yazýlýr, burada 'practise' yazýldý
    webdriver.findIdAndClick("btnAddRequirement") # yeni requirementi ekle butonuna basýlýr.

    time.sleep(5)
    webdriver.driver.quit()
