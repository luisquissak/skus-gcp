from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

with open(r"files/skus.txt", 'r') as f:
    skus = [line.rstrip() for line in f]

outf = open(r"files/sku-pricing.txt", 'w')

for sku in skus:
    driver = webdriver.Firefox()
    print("sku: ", sku)
    driver.get("https://cloud.google.com/skus/?hl=en&filter="+sku+"&currency=BRL")
    time.sleep(3)
    assert 'SKU' in driver.title

    price = ""
    try:
        table = driver.find_element(by=By.TAG_NAME, value=("table"))
        tableRow = table.find_element(by=By.XPATH, value=("//tr[1]"))
        price = tableRow.find_element(by=By.XPATH, value=("//td[2]")).text
        print(sku, price)
    except:
        print(sku, "erro !")
    outf.write(sku + ";" + price)
    outf.write("\n")
    driver.quit()
    time.sleep(3)
outf.close()