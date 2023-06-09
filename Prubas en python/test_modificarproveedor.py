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

class TestModificarproveedor():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_modificarproveedor(self):
    self.driver.get("http://localhost/Sistema_venta_basico-master/sistema/index.php")
    self.driver.set_window_size(1050, 708)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(8) span").click()
    self.driver.find_element(By.LINK_TEXT, "Proveedores").click()
    self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(3) > td > .btn").click()
    self.driver.find_element(By.ID, "telefono").click()
    self.driver.find_element(By.ID, "telefono").send_keys("829885674")
    self.driver.find_element(By.ID, "direccion").click()
    self.driver.find_element(By.ID, "direccion").send_keys("La caleta, Boca chica")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(6)").click()
  
