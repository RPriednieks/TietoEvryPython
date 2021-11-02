# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# #driver.maximize_window()
# driver.get("https://www.neste.lv/lv/content/degvielas-cenas")
# #driver.find_element(By.NAME, 'q').send_keys('Yasser Khalil')
#
# price2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/article/div/div[1]/div[1]/div/div/table/tbody/tr[2]/td[2]/p/span/strong")
# print(price2.text)
# #disel_price = driver.find_elements()
# # print(driver.title)
# driver.close()
#
# #driver.quit()

zz = {'95': 1.487, '95 Premium': None, '98': 1.527, 'DD': 1.387, 'DD Premium': 1.477, 'LPG': None, 'CNG': None, '85': None}

for key, value in zz:
    print(value)