from selenium import webdriver
from PIL import Image
import time


url='https://www.wenku8.net/book/2331.htm'
option=webdriver.ChromeOptions()
# option.add_argument(binary_location='C:/Program Files/Google/Chrome/Application/chrome.exe')
option.add_argument('headless')
driver=webdriver.Chrome(options=option)

driver.get(url)
width = driver.execute_script("return document.documentElement.scrollWidth")
height = driver.execute_script("return document.documentElement.scrollHeight")
driver.set_window_size(width,height) #修改浏览器窗口大小

#获取整个网页截图
driver.get_screenshot_as_file('../imgs/webpage.png')
print("整个网页尺寸:height={},width={}".format(height,width))
im=Image.open('../imgs/webpage.png')
print("截图尺寸:height={},width={}".format(im.size[1],im.size[0]))
