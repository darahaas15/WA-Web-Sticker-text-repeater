from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Listener
import time

driver = webdriver.Edge("msedgedriver.exe")
driver.get("https://web.whatsapp.com/")


def chatbot():
    #chat_name = 'Spam Cuck'
    chat_name = 'Spam Target'

    chat = driver.find_element_by_xpath('//span[@title="{}"]'.format(chat_name))
    chat.click()
    try:
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[1]/button[2]/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[1]/button[4]/span').click()
        time.sleep(5)
    except:
        pass

    count = 0
    for i in range(100):
        try:
            count += 1
            driver.find_element_by_xpath(
                '//*[@id="main"]/footer/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/div[' + str(count) + ']/div/span/img').click()

        except:
            count = 1

        print(count)

def on_press(key):
    key_press = key
    chatbot()


with Listener(on_press=on_press) as listener:
    listener.join()


print("Python sticker spammer made using selenium ")


