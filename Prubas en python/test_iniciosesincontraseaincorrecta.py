# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestIniciosesincontraseaincorrecta():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_iniciosesincontraseaincorrecta(self):
    self.driver.get("http://localhost/Sistema_venta_basico-master/")
    self.driver.set_window_size(1050, 708)
    self.driver.find_element(By.NAME, "usuario").click()
    self.driver.find_element(By.NAME, "usuario").send_keys("admin")
    self.driver.find_element(By.NAME, "clave").send_keys("alofoke")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
