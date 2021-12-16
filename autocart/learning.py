from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.gobilda.com/bulk-order/')

for i in range(3):
    sku_field = driver.find_element(By.CLASS_NAME, 'skuField')
    qty_field = driver.find_element(By.CLASS_NAME, 'qtyField')
    bulk_order_table = driver.find_element(By.ID, 'bulkOrderTable') #.children[1].children[0].children[2].children[1]

    add_button = bulk_order_table.find_elements(By.XPATH, "./child::*")[1]
    add_button = add_button.find_elements(By.XPATH, "./child::*")[0]
    add_button = add_button.find_elements(By.XPATH, "./child::*")[2]
    add_button = add_button.find_elements(By.XPATH, "./child::*")[1]

    add_action = ActionChains(driver)
    add_action.click(on_element = add_button)

    skus = ['1120-0002-0072', '1120-0003-0096', '1120-0004-0120']

    sku_field.clear()
    sku_field.send_keys(skus[i])
    # sku_field.send_keys(Keys.RETURN)
    qty_field.clear()
    qty_field.send_keys('1')

    add_action.perform()

