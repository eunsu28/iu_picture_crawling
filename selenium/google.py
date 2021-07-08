from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib.request 

url = "https://www.google.co.kr/search?q=%EC%95%84%EC%9D%B4%EC%9C%A0&newwindow=1&safe=strict&sxsrf=ALeKk03R_ZtjrhJ9cMzFrU4R0GNcPumhEg:1625477676020&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiG49-b0MvxAhUMWX0KHcpfA7sQ_AUoAXoECAEQAw"


driver = webdriver.Chrome("/Users/kim-eunsu/Desktop/selenium/chromedriver")
driver.get(url)

num = 1

imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[1:21]
for img in imgs:
    img.click()
    sleep(5)
    img_url = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img").get_attribute('src') #그 f12 누르고 거기서 뭐 x_path 커피 있음 그걸로 따오삼
    urllib.request.urlretrieve(img_url, f"img/iu{num}.jpg")
    num += 1 


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()
print("finish")