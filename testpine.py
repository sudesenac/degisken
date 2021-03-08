from selenium import webdriver
from degisken3.testpineDegisken import Degisken
import time


class TestRequirement():
    
    webdriver = Degisken()
    webdriver.setDriver("C:\\Users\\pc\\Desktop\\selenium\\chromedriver.exe")
    webdriver.driver.get("https://www.testpine.com/")  #testpinecom'a gidi�
    print(webdriver.driver.title)
    webdriver.driver.maximize_window()
    
    webdriver.findCssAndClick("body > section.hero > div > div > div.col-md-6.col-sm-12.text-md-left.text-sm-center.text-center > a") #go To App'i t�kl�yoruz
    webdriver.setEmail("sudesenacizmeci@gmail.com")  #ge�erli mail adresi girilir
    webdriver.setPassword("sudeberkay1")  #ge�erli �ifre girilir.
    webdriver.findCssAndClick("body > div > div > div.col-lg-7.col-md-12.col-sm-12.col-xs-12.login-right > div.login-right-form > form > button") #login butonuna t�klan�r.
    time.sleep(3)
    webdriver.driver.save_screenshot("C:\\Users\\pc\\Desktop\\selenium\\ss.png") #sayfan�n ekran g�r�nt�s�n� al�r.
    time.sleep(0.5)
    
    webdriver.findCssAndClick("body > div > div > aside > div.nav-wrapper > ul > li:nth-child(2) > a") #requirement'e t�klan�r, sayfaya gidilir
    webdriver.findIdAndClick("returnList")  #yeni requirement'e t�klan�r.
    webdriver.findIdAndClick("requirementName")  #requirement name alan�na gidilir.
    webdriver.requirementNameYaz("practise")  #istenilen requirement ad� yaz�l�r, burada 'practise' yaz�ld�
    webdriver.findIdAndClick("btnAddRequirement") # yeni requirementi ekle butonuna bas�l�r.

    time.sleep(5)
    webdriver.driver.quit()
