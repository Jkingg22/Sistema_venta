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

class TestGeneracinfactura():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_generacinfactura(self):
    self.driver.get("http://localhost/Sistema_venta_basico-master/sistema/")
    self.driver.set_window_size(1050, 708)
    self.driver.find_element(By.LINK_TEXT, "Ventas").click()
    self.driver.find_element(By.LINK_TEXT, "Nueva venta").click()
    self.driver.find_element(By.ID, "dni_cliente").click()
    self.driver.find_element(By.ID, "dni_cliente").send_keys("123545")
    self.driver.find_element(By.ID, "txt_cod_producto").click()
    self.driver.find_element(By.ID, "txt_cod_producto").send_keys("6")
    self.driver.find_element(By.ID, "txt_cod_producto").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "txt_cant_producto").click()
    self.driver.find_element(By.ID, "txt_cant_producto").send_keys(Keys.ENTER)
    self.driver.find_element(By.ID, "txt_cant_producto").send_keys("1")
    self.driver.find_element(By.ID, "add_product_venta").click()
    self.driver.execute_script("window.scrollTo(0,155)")
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.ID, "btn_facturar_venta").click()
    self.vars["win3352"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win3352"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.execute_script("window.scrollTo(0,155)")
  
