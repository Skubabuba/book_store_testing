# Отображение товара


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
#
# driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(15)
# my_account_btn = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account_btn.click()
# username = driver.find_element_by_id("username")
# username.send_keys("garrystif@mail.com")
# pas = driver.find_element_by_id("password")
# pas.send_keys("Aa123A!qwert123")
# login_btn = driver.find_element_by_css_selector("p:nth-child(3) > input.woocommerce-Button.button")
# login_btn.click()
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_btn.click()
# html5_book = driver.find_element_by_css_selector(".post-181 h3")
# html5_book.click()
# book_name = driver.find_element_by_css_selector("#product-181 > div.summary.entry-summary > h1")
# book_name_text = book_name.text
# assert book_name_text == "HTML5 Forms"
#
# driver.quit()

#Количество товаров в категории


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(15)
# my_account_btn = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account_btn.click()
# username = driver.find_element_by_id("username")
# username.send_keys("garrystif@mail.com")
# pas = driver.find_element_by_id("password")
# pas.send_keys("Aa123A!qwert123")
# login_btn = driver.find_element_by_css_selector("p:nth-child(3) > input.woocommerce-Button.button")
# login_btn.click()
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_btn.click()
# html_category = driver.find_element_by_css_selector("ul > li.cat-item.cat-item-19 > a")
# html_category.click()
# items_count = driver.find_elements_by_css_selector(".shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link")
# if len(items_count) == 3:
#     print("На странице 3 товара")
# else:
#     print("Ошибка")
# driver.quit()



#Сортировка товаров


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(15)
# my_account_btn = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account_btn.click()
# username = driver.find_element_by_id("username")
# username.send_keys("garrystif@mail.com")
# pas = driver.find_element_by_id("password")
# pas.send_keys("Aa123A!qwert123")
# login_btn = driver.find_element_by_css_selector("p:nth-child(3) > input.woocommerce-Button.button")
# login_btn.click()
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_btn.click()
# default_sorting = driver.find_element_by_css_selector("#content > form > select > option:nth-child(1)")
# default_sorting_now = default_sorting.get_attribute("selected")
# if default_sorting_now == "selected":
#     print("Статус не совпадает")
# else:
#     print("Статус совпадает")
# status_selector = driver.find_element_by_css_selector("#content > form > select")
# select = Select(status_selector)
# select.select_by_value("price-desc")
# chosen_selector = driver.find_element_by_css_selector("#content > form > select > option:nth-child(6)")
# chosen_selector_now = chosen_selector.get_attribute("price-desc")
# if chosen_selector_now == "price-desc":
#     print("Статус не совпадает")
# else:
#     print("Статус совпадает")
# driver.quit


#Отображение, скидка товара


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(15)
# my_account_btn = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account_btn.click()
# username = driver.find_element_by_id("username")
# username.send_keys("garrystif@mail.com")
# pas = driver.find_element_by_id("password")
# pas.send_keys("Aa123A!qwert123")
# login_btn = driver.find_element_by_css_selector("p:nth-child(3) > input.woocommerce-Button.button")
# login_btn.click()
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_btn.click()
# android_book = driver.find_element_by_css_selector(".post-169 h3")
# android_book.click()
# old_price = driver.find_element_by_css_selector(".price > del > span")
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector(".price > ins > span")
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# close_book_cover = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, " div.pp_details > a")))
# close_book_cover.click()
# driver.quit()



# #Проверка цены в корзине


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(15)
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_btn.click()
# add_to_cart = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)")
# add_to_cart.click()
# time.sleep(5)
# cart_item_count = driver.find_element_by_css_selector("#wpmenucartli > a > span.cartcontents")
# cart_item_count_text = cart_item_count.text
# assert cart_item_count_text == "1 Item"
# cart_item_price = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount")
# cart_item_price_text = cart_item_price.text
# assert cart_item_price_text == "₹180.00"
# cart_btn = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
# cart_btn.click()
# total_price = WebDriverWait(driver, 15).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, " tr.order-total > td > strong > span"), "183.60"))
# subtotal_price = WebDriverWait(driver, 15).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr.cart-subtotal > td > span"), "180.00"))
# driver.quit()


#Работа в корзине
#
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(15)
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0,300);")
# html_5_dev = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)")
# html_5_dev.click()
# time.sleep(5)
# js_book = driver.find_element_by_css_selector(".post-165 > a:nth-child(2)")
# js_book.click()
# time.sleep(5)
# cart_btn = driver.find_element_by_css_selector("#wpmenucartli > a")
# cart_btn.click()
# time.sleep(5)
# remove_btn = driver.find_element_by_css_selector(" tr:nth-child(1) > td.product-remove > a")
# remove_btn.click()
# undo_btn = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, " div.woocommerce-message > a")))
# undo_btn.click()
# quantity_area = driver.find_element_by_css_selector(" tr:nth-child(1) > td.product-quantity > div > input")
# quantity_area.clear()
# quantity_area.send_keys(3)
# update_basket_btn = driver.find_element_by_css_selector("tr:nth-child(3) > td > input.button")
# update_basket_btn.click()
# time.sleep(5)
# quantity_area_1 = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
# quantity_area_2 = quantity_area_1.get_attribute("value")
# assert quantity_area_2 == "3"
# time.sleep(5)
# apply_coupon_btn = driver.find_element_by_css_selector("tr:nth-child(3) > td > div > input.button")
# apply_coupon_btn.click()
# new_alert = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > ul")
# new_alert_text = new_alert.text
# assert new_alert_text == "Please enter a coupon code."
#
# driver.quit()


#Работа в корзине


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome(executable_path="c:/chromedriver.exe")
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(15)
# shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0,300);")
# html_5_dev = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)")
# html_5_dev.click()
# time.sleep(5)
# cart_btn = driver.find_element_by_css_selector("#wpmenucartli > a")
# cart_btn.click()
# time.sleep(5)
# proceed_to_checkout = WebDriverWait(driver, 20).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "div.woocommerce > div > div > div > a")))
# proceed_to_checkout.click()
# first_name = WebDriverWait(driver, 15).until(
#     EC.element_to_be_clickable((By.ID, "billing_first_name")))
# first_name.send_keys("Igor")
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Igor")
# email_area = driver.find_element_by_id("billing_email")
# email_area.send_keys("garrystif@mail.com")
# phone_area = driver.find_element_by_id("billing_phone")
# phone_area.send_keys("89111234567")
# country_selector = driver.find_element_by_id("s2id_billing_country")
#
# country_selector.click()
# country_area = driver.find_element_by_id("s2id_autogen1_search")
# country_area.send_keys("Russia")
# country_russia = driver.find_element_by_id("select2-results-1")
# country_russia.click()
# adress_area = driver.find_element_by_id("billing_address_1")
# adress_area.send_keys("Nevsky")
# town_area = driver.find_element_by_id("billing_city")
# town_area.send_keys("Yerevan")
# state_area = driver.find_element_by_id("billing_state")
# state_area.send_keys("Zeityn")
# zip_area = driver.find_element_by_id("billing_postcode")
# zip_area.send_keys("123432")
# driver.execute_script("window.scrollBy(0,600);")
# time.sleep(5)
# payment = driver.find_element_by_id("payment_method_cheque")
# payment.click()
# place_order = driver.find_element_by_id("place_order")
# place_order.click()
# thnx = WebDriverWait(driver, 15).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce"), "Thank you. Your order has been received."))
# pay_check = WebDriverWait(driver, 15).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.woocommerce > table > tfoot > tr:nth-child(3) > td"), "Check Payments"))
# driver.quit()
