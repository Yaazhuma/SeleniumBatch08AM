import time

import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.implicitly_wait(10)

srchbox = driver.find_element(By.NAME, 'q')
srchbox.send_keys("iphone")
keyboard.press("Enter")
keyboard.release("Enter")
time.sleep(5)
txtcnt = driver.find_element(By.XPATH,'//span[@class="BUOuZu"]')
cunt = txtcnt.text
print(cunt)
print(type(cunt))
print('Total search result count is: ',cunt[18:21:1])
srchresultitems=driver.find_elements(By.XPATH,'//div[@class="KzDlHZ"]')
print("==========================================")
print('Below are the list of items in page 1:')
print("==========================================")
for i in range(0,len(srchresultitems),1):
    item=srchresultitems[i]
    itm=item.text

    print(itm)

srcresultprices=driver.find_elements(By.XPATH,'//div[@class="Nx9bqj _4b5DiR"]')
print("==========================================")
print('Below is the price of items listed in page1:')
print("==========================================")
for j in range(0,len(srcresultprices),1):
    prices=srcresultprices[j]
    price=prices.text

    print(price)
print("==========================================")
print("Items with their pricing detail")
print("==========================================")
for i in range(0,len(srchresultitems),1):
    items=srchresultitems[i]
    item=items.text
    # print(item)
    for j in range(i,i+1,1):
        prices=srcresultprices[j]
        price=prices.text
        print('Item name:',item,'Item Price is:',price)

print("==========================================")
print("Min and max price")
print("==========================================")

prclist=[]
for j in range(0,len(srcresultprices),1):
    prices=srcresultprices[j]
    price=prices.text
    prc=price.replace("₹","")
    prcformatted=prc.replace(",","")
    prclist.append(int(prcformatted))
# print(prclist)
print("Lowest price in page is:₹",min(prclist))
print("Highest price in page is:₹",max(prclist))