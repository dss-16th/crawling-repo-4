from itemadapter import ItemAdapter
#from .mongodb import collection
import requests, json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import urllib.parse as urlparse
from urllib.parse import parse_qs
import random
from selenium.webdriver.chrome.options import Options
import time
import logging
from itemadapter import ItemAdapter


class Covid19TotalBackupPipeline:
    def process_item(self, item, spider):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        options.add_argument("window-size=1920x1080")
        options.add_argument('Mozilla/5.0')
        driver = webdriver.Chrome(options=options)

        REST_API_KEY = "REST_API_KEY"
        REDIRECT_URL = "REDIRECT_URL/oauth"

        url = "https://kauth.kakao.com/oauth/authorize?client_id={}&redirect_uri={}&response_type=code".format(REST_API_KEY, REDIRECT_URL)
        driver.get(url)
        time.sleep(2)

        elem_login = driver.find_element_by_id("id_email_2")
        elem_login.clear()
        elem_login.send_keys("id_email")
        time.sleep(0.3)
        elem_login.send_keys("id_email")
        time.sleep(0.6)
        elem_login.send_keys("id_email")
        time.sleep(0.5)
        elem_login.send_keys("id_email")
        time.sleep(0.7)
        elem_login.send_keys("id_email")
        time.sleep(2)

        elem_login = driver.find_element_by_id("id_password_3")
        elem_login.clear()
        elem_login.send_keys("password") 
        time.sleep(2.8)

        xpath = """//*[@id="login-form"]/fieldset/div[8]/button[1]"""
        driver.find_element_by_xpath(xpath).click()

        time.sleep(6)

        wait_time = 60

        driver.implicitly_wait(wait_time)
        url_current = driver.current_url

        parsed = urlparse.urlparse(url_current)
        access_token = parse_qs(parsed.query)

        driver.close()

        auth_code = access_token
        auth_code = auth_code['code'][0]
        url = "https://kauth.kakao.com/oauth/token" #post
        params ={
            "grant_type":"authorization_code",
            "client_id":REST_API_KEY,
            "redirect_uri":REDIRECT_URL,
            "code": auth_code,
        }

        response = requests.post(url, params)

        user_datas = response.json()

        ACCESS_TOKEN = user_datas["access_token"]

        url = "https://kapi.kakao.com/v2/user/me"

        headers = {"Authorization" : f'Bearer {ACCESS_TOKEN}'}

        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #post만 됨
        params = {
           "object_type":"text",
            #"text" : '날짜 : {0}\n국내 확진자 : {1}'.format(str(item['date']), str(item['country_in'])),
            "text" : '<코로나 알리미>\n\n{0}\n\n전체 확진자 : {1} 명\n국내 : {2} 명\n해외 유입 : {3} 명\n\n수도권 거리두기 : {4} 단계\n비수도권 거리두기 : {5} 단계\n\n백신 누적 현황 : {6} 명\n백신 전일 현황 : {7} 명\n\n수도권 전일 백신 현황\n서울 : {8} 명\n경기 : {9} 명\n인천 : {10} 명 '.format(str(item['date']), str(item['total_country']),str(item['country_in']),str(item['country_out']),str(item['capital_distance']),str(item['noncapital_distance']),str(item['total_1']),str(item['take_yesterday_1']),str(item['seoul_vaccine']),str(item['gyeonggi_vaccine']),str(item['incheon_vaccine'])), 
            "link":{
                "web_url":"http://15.164.101.134/",
                "mobile_web_url":"http://15.164.101.134/",
            },
            "button_title" : "관련 기사를 확인하세요!",    
        }

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        payload = "template_object=" + json.dumps(params)

        response = requests.post(url, payload, headers=headers) 
        
        return item
