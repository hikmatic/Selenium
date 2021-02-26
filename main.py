from selenium import webdriver

chrome_driver_path="c:\development\chromedriver.exe"



driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.empireonline.com/movies/features/best-movies-2/")

price = driver.find_elements_by_css_selector(".listicle-item h3")
#
# print(price.text)


for x in price:
    print(x.text)









#driver.quit()