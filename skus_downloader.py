from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

today = datetime.today().strftime('%Y%m%d') + "-"

with open(r"files/"+today+"skus.txt", 'r') as f:
    skus = [line.rstrip() for line in f]

outf = open(r"files/"+today+"sku-pricing.csv", 'w')
outf.write("sku,price,metric,region")
outf.write("\n")

for sku in skus:
    driver = webdriver.Firefox()
    print("sku: ", sku)
    driver.get("https://cloud.google.com/skus/?hl=en&filter=" +
               sku+"&currency=BRL")
    time.sleep(3)
    assert 'SKU' in driver.title

    price = ""
    try:
        table = driver.find_element(by=By.TAG_NAME, value=("table"))
        tableRow = table.find_element(by=By.XPATH, value=("//tr[1]"))
        price = tableRow.find_element(by=By.XPATH, value=("//td[2]")).text
        region = tableRow.find_element(by=By.XPATH, value=("//td[3]")).text
        print(sku, price, region)
    except:
        print(sku, "erro !")
    outf.write(sku + "," + price.replace(" per ", ",") + "," + region)
    outf.write("\n")
    driver.quit()
    time.sleep(3)
outf.close()
