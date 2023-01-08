#Добавление комментария


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(15)
driver.execute_script("window.scrollBy(0,600);")
read_more_btn = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.button.product_type_simple.ajax_add_to_cart")
read_more_btn.click()
reviews_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab")))
reviews_btn.click()
five_stars_btn = driver.find_element_by_css_selector(" p > span > a.star-5")
five_stars_btn.click()
comment_area = driver.find_element_by_id("comment")
comment_area.send_keys("Nice book!")
author_area = driver.find_element_by_id("author")
author_area.send_keys("Igor")
email_area = driver.find_element_by_id("email")
email_area.send_keys("asda21@meme.com")
submit_btn = driver.find_element_by_css_selector("p > input:nth-child(1).submit")
submit_btn.click()

driver.quit()