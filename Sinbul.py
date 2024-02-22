from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui as pag
import pyperclip
import keyboard
import random
import time


#아이디 입력
#▶▶▶▶▶▶▶▶▶
global 크롤링_id
크롤링_id = "pend"
global 크롤링_pw
크롤링_pw = "*Zoavld4fkd" 


global 크롤링_사이트
크롤링_사이트 = 0  

def 크롤링_타임(크롤링_min,크롤링_sec):
  global 크롤링_타임_min, 크롤링_타임_sec
  크롤링_타임_min = int(크롤링_min)
  크롤링_타임_sec = int(크롤링_sec)

def 크롤링_조건():
  global 크롤링_실시간
  크롤링_실시간 = 1

def 크롤링_Log_Id1():
  global 크롤링_id
  크롤링_id = "pend"
  print(크롤링_id)

def 크롤링_Log_Id2():
  global 크롤링_id
  크롤링_id = "lovepend2"
  print(크롤링_id)

def 크롤링_Log_Id3():
  global 크롤링_id
  크롤링_id = "lovepend1"
  print(크롤링_id)

def 크롤링_Log_Id4():
  global 크롤링_id
  크롤링_id = "parkmc7"
  print(크롤링_id)

def 크롤링_Log_Guest():
  global 크롤링_id
  크롤링_id = "jhrep1201"
  global 크롤링_pw
  크롤링_pw = "j1902217**"
  print(크롤링_id)



#날짜 입력
#▶▶▶▶▶▶▶▶▶                                                몇주차                       6: 금요일 7 : 토요일
#       //*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[6]
#date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[7]'
  
def 크롤링_Day11():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[6]'
  print('1F')

def 크롤링_Day12():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[7]'
  print('1S')

def 크롤링_Day21():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[1]/table/tbody/tr/td[6]'
  print('2F')

def 크롤링_Day22():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[1]/table/tbody/tr/td[7]'
  print('2S')

def 크롤링_Day31():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[6]'
  print('3F')

def 크롤링_Day32():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[7]'
  print('3S')

def 크롤링_Day41():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[6]'
  print('4F')

def 크롤링_Day42():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[7]'
  print('4S')

def 크롤링_Day51():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[6]'
  print('5F')

def 크롤링_Day52():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[7]'
  print('5S')

def 크롤링_Day53():
  global date
  date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[6]/div[1]/table/tbody/tr/td[1]'
  print('6S')
  
#캠핑장 입력
#▶▶▶▶▶▶▶▶▶                           
#//*[@id="divAjaxTable"]/input[1] 작괘
#//*[@id="divAjaxTable"]/input[2] 등억
#//*[@id="divAjaxTable"]/input[3] 달빛

def 크롤링_작괘():
  global camp
  camp = '//*[@id="divAjaxTable"]/input[1]'
  print('작괘')

def 크롤링_등억():
  global camp
  camp = '//*[@id="divAjaxTable"]/input[2]'
  print('등억')

def 크롤링_달빛():
  global camp
  camp = '//*[@id="divAjaxTable"]/input[3]'
  print('달빛')

#순서 입력
#▶▶▶▶▶▶▶▶▶ 
def 크롤링_첫번쨰():
  global 크롤링_select
  크롤링_select = 1
  print('첫번째 검색')

def 크롤링_두번쨰():
  global 크롤링_select
  크롤링_select = 2
  print('두번째 검색')

def 크롤링_세번쨰():
  global 크롤링_select
  크롤링_select = 3
  print('세번째 검색')

def 크롤링_첫째달():
  global 크롤링_mon
  크롤링_mon = 1
  print('첫째달 선택')

def 크롤링_둘째달():
  global 크롤링_mon
  크롤링_mon = 2  
  print('둘째달 선택')

#사이트 입력
#▶▶▶▶▶▶▶▶▶ 
def 크롤링_사이트():
  global 크롤링_사이트
  크롤링_사이트 = 1  
  print('오토사이트 선택')

def 크롤링_시작():
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

  # 웹 페이지로 이동
  


  #driver.execute_script("document.body.style.zoom='zoom %'")

  # 웹 페이지에서 작업 수행
  # 예: 웹 페이지의 요소를 찾아 클릭하거나 데이터를 입력할 수 있음

  ###########################로그인 클릭
  print('로그인')
  button = driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a')
  # 버튼 클릭
  button.click()
  time.sleep(0.2)


  ###########################로그인 클릭 1
  print('로그인 클릭')
  button = driver.find_element(By.XPATH, '//*[@id="login_ulsan"]/img')
  # 버튼 클릭
  button.click()
  time.sleep(0.5)

  ###########################로그인 ID입력
  print('로그인 ID')
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/fieldset/label/span/input')
  # 버튼 클릭
  button.click()
  pyperclip.copy(크롤링_id)
  
  time.sleep(0.5)
  pag.hotkey('ctrl','v')

  ###########################로그인 PW입력
  print('로그인 PW')
  button = driver.find_element(By.XPATH, '//*[@id="password"]')
  # 버튼 클릭
  button.click()
  pyperclip.copy(크롤링_pw)
  time.sleep(0.5)
  pag.hotkey('ctrl','v')

  ###########################로그인 클릭
  print('로그인 접속')
  button = driver.find_element(By.XPATH, '//*[@id="loginfrm"]/div/input')
  # 버튼 클릭
  button.click()
  time.sleep(0.5)
  온라인예약()
  
def 온라인예약():
  print('온라인 예약')
  try:
    ###########################온라인 예약 클릭
    button = driver.find_element(By.XPATH, '//*[@id="main_menu"]/li[4]/a')
    # 버튼 클릭
    button.click()
    time.sleep(3)
    달력클릭()
  except:
    온라인예약()

def 달력클릭():
  print('달력 클릭')
  try:
    ###########################달력 클릭
    if 크롤링_mon == 2 :
      button = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[1]/div[2]/button/span')
      # 버튼 클릭
      button.click()
      time.sleep(3)
      날짜클릭()
    else :
      날짜클릭()
  except:
    달력클릭()

def 날짜클릭():
  print('날짜 클릭')
  try:
    ###########################날짜 예약 클릭
    button = driver.find_element(By.XPATH, date)
    # 버튼 클릭
    button.click()
    time.sleep(10)
    사이트클릭()
  except:
    날짜클릭()

def 사이트클릭():
  print('사이트 클릭')
  try:
    if 크롤링_사이트 == 1 :
      ###########################사이트종류 오토 클릭
      button = driver.find_element(By.XPATH, '//*[@id="priceCode"]')
      # 버튼 클릭
      button.click()
      time.sleep(0.5)
      pag.hotkey('down')
      time.sleep(0.5)
      pag.hotkey('enter')
      time.sleep(2)
      캠핑장클릭()
    else:
      캠핑장클릭()    
  except:
    사이트클릭()

def 캠핑장클릭():
  print('캠핑장 클릭')
  try:
    ###########################캠핑장 선택
    button = driver.find_element(By.XPATH, camp)
    # 버튼 클릭
    button.click()
    time.sleep(10)
    예약가능()
  except:
    캠핑장클릭()

def 예약가능():
  print('예약가능')
  try:
    if 크롤링_select == 2 or 크롤링_select == 3 :
      # ###########################예약가능 사이트만 보기 클릭
      button = driver.find_element(By.XPATH, '//*[@id="divAjaxTable"]/div/label')
      # 버튼 클릭
      button.click()
      time.sleep(0.2)
      예약하기()
    else : 
      예약하기()
  except:
    예약가능()


def 예약하기():
  print('예약하기')
  while True:
    global 크롤링_타임
    tm = time.localtime()
    if keyboard.is_pressed("F2"):
      print("종료") 
      break  
    if (tm.tm_min == 크롤링_타임 ) : #9시 56분 및 15시 56분 시작
      예약하기1()
    if (크롤링_실시간 == 1) :
      예약하기1()


def 예약하기1():
  try:
    while True:    
      ###########################날짜 예약 클릭
      button = driver.find_element(By.XPATH, date)
      # 버튼 클릭
      button.click()
      time.sleep(0.1)
      try:
        if 크롤링_select == 1 :
          ###########################예약신청 클릭                            *맨처음 [1] 두번째[2] 
          button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[*]/td[*]/button')
        if 크롤링_select == 2 :
          button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[2]/td[*]/button')
        if 크롤링_select == 3 :
          button = driver.find_element(By.XPATH, '//*[@id="tableSite"]/tbody/tr[3]/td[*]/button')
        # 버튼 클릭
        button.click()
        time.sleep(0.4)
        ###########################예약신청 클릭
        print('예약신청 클릭')
        button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
        # 버튼 클릭
        button.click()
        time.sleep(0.2)
        print('예약신청 클릭')
        ###########################예약신청 클릭
        button = driver.find_element(By.XPATH, '//*[@id="resModal"]/div[2]/div/div[3]/button[2]')
        # 버튼 클릭
        button.click()
        time.sleep(60)
      except:
        예약하기1()
  except:
      예약하기1()

