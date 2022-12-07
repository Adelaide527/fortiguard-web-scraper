from sys import flags
from bs4 import BeautifulSoup
import urllib.request as urllib
# import re
import time
# import smtplib
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

#Prep the browser
service = Service('C:/WebDriver/bin/geckodriver.exe') #Define the service. geckodriver=Firefox
browser = webdriver.Firefox(service=service) #Using FireFox browser

#Create file to save everything into
outfile = open("output.txt", 'w')

class Threat:
  #####
  # Variable list:
  # name, description, affected_products, impact, reccomended_actions
  #####
  def __init__(self):
    self.name = ""
    self.description = ""
    self.affected_products = ""
    self.impact = ""
    self.reccomended_actions = ""

  def set_name(self, name):
    self.name = name
  
  def set_description(self, description):
    self.description = description

  def set_affected_products(self, affected_products):
    self.affected_products = affected_products

  def set_impact(self, impact):
    self.impact = impact

  def set_reccomended_actions(self, reccomended_actions):
    self.reccomended_actions = reccomended_actions
  
  def print(self):
    return str(self.name + "\n")
    # return str(self.name + " | " + self.description + " | " + self.affected_products + " | " + self.impact + " | " + self.reccomended_actions)

browser.get('https://www.fortiguard.com/encyclopedia?type=ips') #Load page
time.sleep(3) #Wait for page to load (giving 3 seconds)

elements = browser.find_elements(By.CLASS_NAME, "title") #Find all titles
for x in range (0, len(elements)):
  time.sleep(1) #Wait for page to load (giving 3 seconds)
  elements[x].click() #Go to title
  time.sleep(3) #Wait for page to load (giving 3 seconds)
  threat = Threat() #Define our threat (create instance of Threat class)
  threat.set_name(browser.find_element(By.CLASS_NAME, "detail-item").text)
  threat.set_description(browser.find_element(By.XPATH, "//div[@class='detail-item'][2]/p").text)
  threat.set_affected_products(browser.find_element(By.XPATH, "//div[@class='detail-item'][3]/p").text)
  threat.set_impact(browser.find_element(By.XPATH, "//div[@class='detail-item'][4]/p").text)
  threat.set_reccomended_actions(browser.find_element(By.XPATH, "//div[@class='detail-item'][5]/p").text)

  outfile.write(threat.print())
  browser.back()
  
  
outfile.close()
browser.quit() #Done with Browser