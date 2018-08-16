from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 创建Options对象
options = Options()
options.set_headless()
driver = webdriver.Chrome(options=options)
driver.get('http://www.sse.com.cn/assortment/stock/list/share/')
i = driver.execute_script('return  Math.floor(Math.random() * (100000 + 1))')

print(i)

