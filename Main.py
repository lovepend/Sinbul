from tkinter import *
import pyautogui as pag
import win32con
import win32api
import win32gui
import keyboard
import clipboard
import pyperclip
import schedule
import time
import cv2
from kakao_01_api import *
from Sinbul_Mobile import *
from Sinbul_PC import *
from Sinbul import *
import tkinter
import sqlite3

#아이디 입력
#▶▶▶▶▶▶▶▶▶
global Sinbul_id
Sinbul_id = "pend"
global Sinbul_pw
Sinbul_pw = "*Zoavld4fkd" 
global Sinbul_date
Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[7]'
global Sinbul_live
Sinbul_live = 1 #1이 시간 / 2가 실시간
global Sinbul_mon
Sinbul_mon = 2 #1이 첫번째달 / 2가 둘쨋달
global Sinbul_camp
Sinbul_camp = '//*[@id="divAjaxTable"]/input[3]'

def Sinbul_Log_Id1():
  global Sinbul_id
  Sinbul_id = "pend"
  print(Sinbul_id)

def Sinbul_Log_Id2():
  global Sinbul_id
  Sinbul_id = "lovepend2"
  print(Sinbul_id)

def Sinbul_Log_Id3():
  global Sinbul_id
  Sinbul_id = "lovepend1"
  print(Sinbul_id)

def Sinbul_Log_Id4():
  global Sinbul_id
  Sinbul_id = "parkmc7"
  print(Sinbul_id)

def Sinbul_Log_Id5():
  global Sinbul_id
  Sinbul_id = "jhrep1201"
  global Sinbul_pw
  Sinbul_pw = "j1902217**"
  print(Sinbul_id, Sinbul_pw)

def Sinbul_Day11():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[6]'
  print('1F')

def Sinbul_Day12():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[1]/div[1]/table/tbody/tr/td[7]'
  print('1S')

def Sinbul_Day21():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[1]/table/tbody/tr/td[6]'
  print('2F')

def Sinbul_Day22():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/div[1]/table/tbody/tr/td[7]'
  print('2S')

def Sinbul_Day31():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[6]'
  print('3F')

def Sinbul_Day32():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/div[1]/table/tbody/tr/td[7]'
  print('3S')

def Sinbul_Day41():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[6]'
  print('4F')

def Sinbul_Day42():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[4]/div[1]/table/tbody/tr/td[7]'
  print('4S')

def Sinbul_Day51():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[6]'
  print('5F')

def Sinbul_Day52():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[5]/div[1]/table/tbody/tr/td[7]'
  print('5S')

def Sinbul_Day53():
  global Sinbul_date
  Sinbul_date = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[6]/div[1]/table/tbody/tr/td[1]'
  print('6S')
  
#캠핑장 입력
#▶▶▶▶▶▶▶▶▶                           
def Sinbul_작괘():
  global Sinbul_camp
  Sinbul_camp = '//*[@id="divAjaxTable"]/input[1]'
  print('작괘')

def Sinbul_등억():
  global Sinbul_camp
  Sinbul_camp = '//*[@id="divAjaxTable"]/input[2]'
  print('등억')

def Sinbul_달빛():
  global Sinbul_camp
  Sinbul_camp = '//*[@id="divAjaxTable"]/input[3]'
  print('달빛')

#순서 입력
#▶▶▶▶▶▶▶▶▶ 
def Sinbul_첫번쨰():
  global Sinbul_select
  Sinbul_select = '//*[@id="tableSite"]/tbody/tr[*]/td[*]/button'
  print('첫번째 검색')

def Sinbul_두번쨰():
  global Sinbul_select
  Sinbul_select = '//*[@id="tableSite"]/tbody/tr[2]/td[4]/button'
  print('두번째 검색')

def Sinbul_세번쨰():
  global Sinbul_select
  Sinbul_select = '//*[@id="tableSite"]/tbody/tr[*]/td[3]/button'
  print('세번째 검색')

#달력 선택
#▶▶▶▶▶▶▶▶▶
def Sinbul_첫째달():
  global Sinbul_mon
  Sinbul_mon = 1
  print('첫째달 선택')

def Sinbul_둘째달():
  global Sinbul_mon
  Sinbul_mon = 2  
  print('둘째달 선택')

#실시간 입력
#▶▶▶▶▶▶▶▶▶
def Sinbul_라이브():
  global Sinbul_live
  Sinbul_live = 2
  schedule_PC_start(Sinbul_id, Sinbul_pw, Sinbul_date, Sinbul_camp, Sinbul_select, Sinbul_mon, Sinbul_time_min, Sinbul_time_sec, Sinbul_live)

def schedule_PC():
  global Sinbul_live
  Sinbul_live = 1
  schedule_PC_start(Sinbul_id, Sinbul_pw, Sinbul_date, Sinbul_camp, Sinbul_select, Sinbul_mon, Sinbul_time_min, Sinbul_time_sec, Sinbul_live)

def schedule_Mobile():
  global Sinbul_live
  Sinbul_live = 1
  schedule_Mobile_start(Sinbul_id, Sinbul_pw, Sinbul_date, Sinbul_camp, Sinbul_select, Sinbul_mon, Sinbul_time_min, Sinbul_time_sec, Sinbul_live)

#스케줄 입력
#▶▶▶▶▶▶▶▶▶ 
def schedule_job():    
  schedule.every().day.at("09:44:00").do(schedule_PC()) 
  schedule.every().day.at("13:44:00").do(schedule_PC()) 
  schedule.every().day.at("21:44:10").do(schedule_PC()) 
  while True:
    schedule.run_pending()


#UI 입력
#▶▶▶▶▶▶▶▶▶ 
window=tkinter.Tk()
window.title("캠핑장 예약하기")
window.geometry("250x190+1660+316")
window.wm_attributes("-topmost", 1)

notebook=tkinter.ttk.Notebook(window, width=460, height=165)
notebook.pack()

#크롤링 UI=============================================================================================================== 
frame1=tkinter.Frame(window)
notebook.add(frame1, text="1.임시") 

lable11=Label(frame1, text="분", font = ("", 7))
lable11.place(x=25, y=140)
    
entry11 = Entry(frame1, width=10, font = ("", 7))
entry11.place(x=50, y=140)
entry11.insert(0,"59")

lable12=Label(frame1, text="초", font = ("", 7))
lable12.place(x=125, y=140)
    
entry12 = Entry(frame1, width=10, font = ("", 7))
entry12.place(x=150, y=140)
entry12.insert(0,"50")

#시간 입력
#▶▶▶▶▶▶▶▶▶
def Sinbul_Time_변수():
  global Sinbul_time_min, Sinbul_time_sec
  Sinbul_min = entry11.get()
  Sinbul_sec = entry12.get()
  print(Sinbul_min,Sinbul_sec)    
  Sinbul_time_min = int(Sinbul_min)
  Sinbul_time_sec = int(Sinbul_sec)
  print(Sinbul_time_min,Sinbul_time_sec)



#로그
Sinbullog1 = Button(frame1, width=5, padx=10, pady=5, text="ID.1", command=Sinbul_Log_Id1, bg="orange", fg="black", font = ("", 7))
Sinbullog1.place(x=0, y=10)
Sinbullog2 = Button(frame1, width=5, padx=10, pady=5, text="ID.2", command=Sinbul_Log_Id2, bg="orange", fg="black", font = ("", 7))
Sinbullog2.place(x=50, y=10)
Sinbullog3 = Button(frame1, width=5, padx=10, pady=5, text="ID.3", command=Sinbul_Log_Id3, bg="orange", fg="black", font = ("", 7))
Sinbullog3.place(x=100, y=10)
Sinbullog4 = Button(frame1, width=5, padx=10, pady=5, text="ID.4", command=Sinbul_Log_Id4, bg="orange", fg="black", font = ("", 7))
Sinbullog4.place(x=150, y=10)
Sinbullog5 = Button(frame1, width=5, padx=10, pady=5, text="ID.5", command=Sinbul_Log_Id5, bg="orange", fg="black", font = ("", 7))
Sinbullog5.place(x=200, y=10)

#날짜
Sinbulday1 = Button(frame1, width=2, padx=5, pady=5, text="1F", command=Sinbul_Day11, bg="white", fg="black", font = ("", 7))
Sinbulday1.place(x=0, y=35)
Sinbulday2 = Button(frame1, width=2, padx=5, pady=5, text="1S", command=Sinbul_Day12, bg="white", fg="black", font = ("", 7))
Sinbulday2.place(x=25, y=35)
Sinbulday3 = Button(frame1, width=2, padx=5, pady=5, text="2F", command=Sinbul_Day21, bg="white", fg="black", font = ("", 7))
Sinbulday3.place(x=50, y=35)
Sinbulday4 = Button(frame1, width=2, padx=5, pady=5, text="2S", command=Sinbul_Day22, bg="white", fg="black", font = ("", 7))
Sinbulday4.place(x=75, y=35)
Sinbulday5 = Button(frame1, width=2, padx=5, pady=5, text="3F", command=Sinbul_Day31, bg="white", fg="black", font = ("", 7))
Sinbulday5.place(x=100, y=35)
Sinbulday6 = Button(frame1, width=2, padx=5, pady=5, text="3S", command=Sinbul_Day32, bg="white", fg="black", font = ("", 7))
Sinbulday6.place(x=125, y=35)
Sinbulday7 = Button(frame1, width=2, padx=5, pady=5, text="4F", command=Sinbul_Day41, bg="white", fg="black", font = ("", 7))
Sinbulday7.place(x=150, y=35)
Sinbulday8 = Button(frame1, width=2, padx=5, pady=5, text="4S", command=Sinbul_Day42, bg="white", fg="black", font = ("", 7))
Sinbulday8.place(x=175, y=35)
Sinbulday9 = Button(frame1, width=2, padx=5, pady=5, text="5S", command=Sinbul_Day51, bg="white", fg="black", font = ("", 7))
Sinbulday9.place(x=200, y=35)
Sinbulday10 = Button(frame1, width=2, padx=5, pady=5, text="5S", command=Sinbul_Day52, bg="white", fg="black", font = ("", 7))
Sinbulday10.place(x=225, y=35)

#선택
Sinbulsel1 = Button(frame1, width=5, padx=10, pady=5, text="첫째달", command=Sinbul_첫째달, bg="green", fg="white", font = ("", 7))
Sinbulsel1.place(x=0, y=59)
Sinbulsel2 = Button(frame1, width=5, padx=10, pady=5, text="둘째달", command=Sinbul_둘째달, bg="white", fg="black", font = ("", 7))
Sinbulsel2.place(x=50, y=59)
Sinbulsel3 = Button(frame1, width=5, padx=10, pady=5, text="첫번째", command=Sinbul_첫번쨰, bg="green", fg="white", font = ("", 7))
Sinbulsel3.place(x=100, y=59)
Sinbulsel4 = Button(frame1, width=5, padx=10, pady=5, text="두번째", command=Sinbul_두번쨰, bg="white", fg="black", font = ("", 7))
Sinbulsel4.place(x=150, y=59)
Sinbulsel5 = Button(frame1, width=5, padx=10, pady=5, text="세번째", command=Sinbul_세번쨰, bg="white", fg="black", font = ("", 7))
Sinbulsel5.place(x=200, y=59)

#함수
Sinbulbtn1 = Button(frame1, width=5, padx=10, pady=5, text="작괘", command=Sinbul_작괘, bg="green", fg="white", font = ("", 7))
Sinbulbtn1.place(x=0, y=83)
Sinbulbtn2 = Button(frame1, width=5, padx=10, pady=5, text="등억", command=Sinbul_등억, bg="white", fg="black", font = ("", 7))
Sinbulbtn2.place(x=50, y=83)
Sinbulbtn3 = Button(frame1, width=5, padx=10, pady=5, text="달빛", command=Sinbul_달빛, bg="white", fg="black", font = ("", 7))
Sinbulbtn3.place(x=100, y=83)
Sinbulbtn4 = Button(frame1, width=5, padx=10, pady=5, text="", command=' ', bg="white", fg="black", font = ("", 7))
Sinbulbtn4.place(x=150, y=83)
Sinbulbtn5 = Button(frame1, width=5, padx=10, pady=5, text=" ", command=' ', bg="white", fg="black", font = ("", 7))
Sinbulbtn5.place(x=200, y=83)

Sinbulbtn6 = Button(frame1, width=5, padx=10, pady=5, text="Time", command=Sinbul_Time_변수, bg="blue", fg="white", font = ("", 7))
Sinbulbtn6.place(x=0, y=110)
Sinbulbtn7 = Button(frame1, width=5, padx=10, pady=5, text="31일", command=Sinbul_Day53, bg="white", fg="black", font = ("", 7))
Sinbulbtn7.place(x=50, y=110)
Sinbulbtn8 = Button(frame1, width=5, padx=10, pady=5, text="실시간", command=Sinbul_라이브, bg="blue", fg="white", font = ("", 7))
Sinbulbtn8.place(x=100, y=110)
Sinbulbtn9 = Button(frame1, width=5, padx=10, pady=5, text="PC시작", command=schedule_job, bg="white", fg="black", font = ("", 7))
Sinbulbtn9.place(x=150, y=110)
Sinbulbtn9 = Button(frame1, width=5, padx=10, pady=5, text="M시작", command=schedule_job, bg="blue", fg="white", font = ("", 7))
Sinbulbtn9.place(x=200, y=110)

window.mainloop()
