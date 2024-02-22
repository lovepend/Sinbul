from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui as pag
import pyperclip
import keyboard
import random
import time
import schedule
from kakao_01_api import *

#시간 
global tm
tm = time.localtime()
refresh_time_click = 1
refresh_time_page = 3

def schedule_PC_start(Sinbul_id, Sinbul_pw, Sinbul_date, Sinbul_camp, Sinbul_select, Sinbul_mon, Sinbul_time_min, Sinbul_time_sec, Sinbul_live):
  global Sinbul_select_change
  Sinbul_select_change = Sinbul_select
  global Sinbul_time_min_change
  Sinbul_time_min_change = Sinbul_time_min
  global Sinbul_time_sec_change
  Sinbul_time_sec_change = Sinbul_time_sec
  global Sinbul_camp_change
  Sinbul_camp_change = Sinbul_camp
  # Chrome 웹 드라이버 생성
  global driver
  driver = webdriver.Chrome()
  #크롬 사이즈 변경
  #driver.set_window_size(1920, 1080) 
  driver.maximize_window()
  driver.get("https://camping.ulju.ulsan.kr/")
  time.sleep(0.2)
  pag.keyDown('ctrl')
  j: int = 1
  for j in range(4):
      pag.press('-')
      time.sleep(0.05)
  #크롬 브라우저 꺼짐 방지
  #웹 페이지로 이동
  #driver.execute_script("document.body.style.zoom='zoom %'")
  #웹 페이지에서 작업 수행
  #예: 웹 페이지의 요소를 찾아 클릭하거나 데이터를 입력할 수 있음

  ###########################로그인 클릭
  print('로그인')
  button = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a')
  # 버튼 클릭
  button.click()
  time.sleep(refresh_time_page)

  ###########################로그인 클릭 1
  print('로그인 클릭')
  button = driver.find_element(By.XPATH, '//*[@id="login_ulsan"]/img')
  # 버튼 클릭
  button.click()
  time.sleep(refresh_time_page)

  ###########################로그인 ID입력
  print('로그인 ID')
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/fieldset/label/span/input')
  # 버튼 클릭
  button.click()
  pyperclip.copy(Sinbul_id)
  time.sleep(refresh_time_click)
  pag.hotkey('ctrl','v')

  ###########################로그인 PW입력
  print('로그인 PW')
  button = driver.find_element(By.XPATH, '//*[@id="password"]')
  # 버튼 클릭
  button.click()
  pyperclip.copy(Sinbul_pw)
  time.sleep(refresh_time_click)
  pag.hotkey('ctrl','v')

  ###########################로그인 클릭
  print('로그인 접속')
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/div/input')
  # 버튼 클릭
  button.click()
  time.sleep(refresh_time_page)

  ###########################온라인 예약 클릭
  print('온라인 예약')
  button = driver.find_element(By.XPATH, '//*[@id="main_menu"]/li[4]/a')
  # 버튼 클릭
  button.click()
  time.sleep(refresh_time_page)

  ###########################달력 클릭
  print('달력 클릭')
  if Sinbul_mon == 2 :
    button = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[1]/div[2]/button/span')
    # 버튼 클릭
    button.click()
    time.sleep(refresh_time_click)

  ###########################날짜 예약 클릭
  print('날짜 클릭')
  button = driver.find_element(By.XPATH, Sinbul_date)
  # 버튼 클릭
  button.click()
  time.sleep(refresh_time_page)

  ###########################캠핑장 선택
  print('캠핑장 클릭')
  button = driver.find_element(By.XPATH, Sinbul_camp)
  # 버튼 클릭
  button.click()
  time.sleep(refresh_time_page)

  ###########################예약하기
  print('예약하기')
  while True:
    tm = time.localtime()
    if keyboard.is_pressed("F2"):
      print("종료") 
      break  
    if (tm.tm_min == Sinbul_time_min and tm.tm_sec == Sinbul_time_sec ) : 
      ###########################날짜 예약 클릭
      print("시간에 맞추어 시작") 
      #button = driver.find_element(By.XPATH, Sinbul_date) #날짜 클릭
      button = driver.find_element(By.XPATH, '//*[@id="divAjaxTable"]/div/label') #예약가능 사이트만 보기 클릭
      # 버튼 클릭
      button.click()
      time.sleep(0.1)
      예약하기_신청()
    if (Sinbul_live == 2 ) :
      print("실시간 시작") 
      예약하기_신청()

def 예약하기_신청():
  try:
    while True:    
      try:
        tm = time.localtime()
        if (tm.tm_min == 35 ) : #9시 56분 및 15시 56분 시작
          print('35분 종료 ')
          time.sleep(3600)
        ########################### 우측 하단 예약신청 클릭 
        print('예약신청 클릭')                           
        button = driver.find_element(By.XPATH, Sinbul_select_change)
        button.click()
        ########################### 우측 하단 예약신청 클릭 
        print('예약신청 클릭')                            
        button = driver.find_element(By.XPATH, Sinbul_select_change)
        button.click()
        time.sleep(0.1)
        ###########################예약신청 클릭
        print('예약확인 클릭')
        button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
        button.click()
        print('예약확인 클릭')
        ###########################예약신청 클릭
        button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
        button.click()
        print(str(Sinbul_time_min_change) + '분' + str(Sinbul_time_sec_change) + '초' + str(Sinbul_camp_change))
      except:
        print('except1')
        예약하기_신청()
  except:
      print(str(Sinbul_time_min_change) + '분' + str(Sinbul_time_sec_change) + '초' + str(Sinbul_camp_change))
      print('except2')
      time.sleep(60)
      

