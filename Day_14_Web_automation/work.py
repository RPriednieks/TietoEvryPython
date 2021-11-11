from selenium import webdriver
PATH = "/Users/rolands/PycharmProjects/PythonTietoEvry/Day_14_Web_automation/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://ss.lv/")
driver.close()