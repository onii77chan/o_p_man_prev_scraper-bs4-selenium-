from time import sleep
import requests
import selenium.common
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.common import NoSuchElementException

tom = 1
chapter = 10


driver = webdriver.Firefox()

while True:
    url = f'https://readmanga.live/vanpanchmen/vol{tom}/{chapter}?mtr=true'
    try:
        driver.get(url)
        sleep(1.5)
        page_source = driver.page_source

        soup = bs(page_source, 'html.parser')
        target_ = soup.find('img', {'id': 'mangaPicture'})
        with open(f'o_p_man_tom{tom}chap{chapter}_bs-ver.jpg', 'wb') as file:
            file.write(requests.get(target_['src']).content)
        chapter += 1

    except NoSuchElementException:
        print(f'Не найдена глава или том: {tom}, глава: {chapter}')
        tom += 1
        page_source = driver.page_source
        soup = bs(page_source, 'html.parser')
        target_ = soup.find('img', {'id': 'mangaPicture'})
        with open(f'o_p_man_tom{tom}chap{chapter}_bs-ver.jpg', 'wb') as file:
            file.write(requests.get(target_['src']).content)

        try:
            soup = bs(page_source, 'html.parser')
            target_ = soup.find('img', {'id': 'mangaPicture'})
            with open(f'o_p_man_tom{tom}chap{chapter}_bs-ver.jpg', 'wb') as file:
                file.write(requests.get(target_['src']).content)
            chapter -= 1
        except NoSuchElementException:
            print('')

