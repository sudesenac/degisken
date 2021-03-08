from selenium import webdriver

class Degisken() : 

        def __init__(self):
            self.driver = ""
            self.email = ""
            self.password = ""
            self.requirementName = ""
            
        def setDriver(self, driver):
            self.driver = webdriver.Chrome(driver)
            
        def setWebsite(self,website):
            self.driver.get(website)
            
        def goToAppGit(self):
            goToApp= self.driver.find_element_by_css_selector("body > section.hero > div > div > div.col-md-6.col-sm-12.text-md-left.text-sm-center.text-center > a")
            goToApp.click()
     
        def setEmail(self, email):
            self.email=self.driver.find_element_by_id("email")
            self.email.send_keys(email)
            
        def getEmail(self, email):
            return self.driver.find_element_by_id("email")
            
        def setPassword(self, password):
            self.password=self.driver.find_element_by_id("password")
            self.password.send_keys(password)
         
        def getPassword(self): 
            return self.driver.find_element_by_id("password")
            
        def loginKonum(self):
            login=self.driver.find_element_by_css_selector("body > div > div > div.col-lg-7.col-md-12.col-sm-12.col-xs-12.login-right > div.login-right-form > form > button")
            login.click()

        def requirementKonum(self):
            requirement=self.driver.find_element_by_css_selector("body > div > div > aside > div.nav-wrapper > ul > li:nth-child(2) > a")
            requirement.click()
        
        def newRequirementEkle(self):
            newRequirement=self.driver.find_element_by_id("returnList")
            newRequirement.click()
      
        def requirementNameYaz(self, requirementName):
            self.requirementName=self.driver.find_element_by_name("requirementName")
            self.requirementName.send_keys(requirementName)
       
        def requirementKayitOlustur(self):
            requirementKayit=self.driver.find_element_by_id("btnAddRequirement")
            requirementKayit.click()
            