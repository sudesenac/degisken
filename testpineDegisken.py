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
     
     
        def findIdAndClick(self, formId):
            self.formText=self.driver.find_element_by_id(formId)
            self.formText.click()
            
            
        def findCssAndClick(self,css):
            login=self.driver.find_element_by_css_selector(css)
            login.click()
        
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
        
        def requirementNameYaz(self, requirementName):
            self.requirementName=self.driver.find_element_by_name("requirementName")
            self.requirementName.send_keys(requirementName)
            
