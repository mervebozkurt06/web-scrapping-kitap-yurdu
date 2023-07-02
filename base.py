from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pymongo import MongoClient

#kitap yurdu mongo bağlantı
client = MongoClient()
db = client['smartmaple']
coll = db['kitapyurdu']

website_kitapyurdu = 'https://www.kitapyurdu.com/index.php?route=product/search&filter_name=python'
#path = 'C:/Users/Merve/Downloads/chromedriver/chromedriver.exe'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(website_kitapyurdu)



#web scraping işlemi
title = driver.find_elements(By.XPATH, '//div[@class="name"]')
publisher = driver.find_elements(By.XPATH, '//div[@class="publisher"]')
writers = driver.find_elements(By.XPATH, '//div[@class="author"]')
price = driver.find_elements(By.XPATH, '//div[@class="price"]')


books = []
for t, pub, w, pri in zip(title, publisher, writers, price):
    book = {}
    book['writer'] = w.text.removeprefix('Yazar: ')
    book['title'] = t.text
    book['publisher'] = pub.text
    book['price'] = pri.text
    books.append(book)



coll.insert_many(books)
client.close()



   

