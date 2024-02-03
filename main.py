from driver_config import driver
from selenium.webdriver.common.by import By
from logger import logger
from utils import save_in_viewed

driver.get("https://www.avito.ru/astrahan/avtomobili/do-300000-rubley-ASgCAgECAUXGmgwWeyJmcm9tIjowLCJ0byI6MzAwMDAwfQ?radius=200&s=104&searchRadius=200")

driver.implicitly_wait(0.5)
urls =  driver.find_elements(By.CSS_SELECTOR, '[data-marker="item-title"]')

#/Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11 

for el in urls:
    link = el.get_attribute("href")
    if 'astrahan' not in link or already_saved(link):
        continue
    logger.success(link)
    save_in_viewed(link)
    
    


driver.quit()

