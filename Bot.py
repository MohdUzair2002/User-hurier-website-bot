from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
from bs4 import BeautifulSoup as bs
import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    dates=(input("Select the date you wnat to search"))
    no_of_shifts=int(input("How many shifts you want to search?"))
    uu=0
    no_of_shifts_list_time=[]
    while( uu < no_of_shifts):
        input_shifts=(input(f"Input your {uu+1} shift time"))
        no_of_shifts_list_time.append(input_shifts)
        uu+=1
    chrome_options = Options()
    s=Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s,options=chrome_options)
    url='https://fi.usehurrier.com/app/rooster/web/login'
    chrome.get(url)
    time.sleep(6)
    email = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@name='email']")))
    email=chrome.find_element(By.XPATH,"//*[@name='email']")
    email.send_keys("joni.makela1337@gmail.com")
    password=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@name='password']")))
    password=chrome.find_element(By.XPATH,"//*[@name='password']")
    password.send_keys("M0h@mmad")
    login=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@type='submit']")))
    login=chrome.find_element(By.XPATH,"//*[@type='submit']")
    chrome.execute_script("arguments[0].click();", login)
    main=0
    dates_list=[]
    else_dates1=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='_3buppnakfM1yJmLufgPz4r _1n1m4lUDeW80P1aEDz0c5W']")))
    else_dates=chrome.find_elements(By.XPATH,"//*[@class='_3buppnakfM1yJmLufgPz4r _1n1m4lUDeW80P1aEDz0c5W']")
    for date in  else_dates:
        dates_list.append(date.text)
    index12=dates_list.index(dates)
    main_index=int(index12)
    chrome.execute_script("arguments[0].click();", else_dates[main_index])
    try:
        k=0
        hh=0
        while(k <no_of_shifts):

            no_of_shifts1=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='_1KsfJ6FtsMi_TEpAVW2Acu _2WQiUC_efpX1jq1Z4e4Elf _2zD8RSltSULvG1oBFUuNgA _2Mdkc-JYfhYSx7OeQp1gnE _19A7ZA9QZsOiamOlmxEUOV _1K3Tay924QS-JVMY7VF-CE']")))
            no_of_shifts1=chrome.find_elements(By.XPATH,"//div[@class='_2T4RT8wt2J1ss8cnHPmSfz']")
            print(f"No of shifts on date {dates} is {len(no_of_shifts1)}")
            i=0
            shift_text=[]
            indexes=[]

            for shift in no_of_shifts1:
                print(i+1)
                print('--------------------------------------------------------')
                print(shift.text) 
                shift_text.append((shift.text))
                i+=1
            
            i=0
            ll=[]
            while(i<len(no_of_shifts_list_time)):
                j=0
                while(j< len(shift_text)):
                    indexes1=(shift_text[j][5:20]).replace('–', "-").strip()
                    if indexes1 in (( no_of_shifts_list_time[i]).strip()):
                        ll.append(j)
                    j+=1
                i+=1
            if (len(ll)>=1) :
            # c=int('what shifts u want to select,enter the serial no of that shift')


                book_index=int(ll[0])
                bookshift=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='_1KsfJ6FtsMi_TEpAVW2Acu _2WQiUC_efpX1jq1Z4e4Elf _2zD8RSltSULvG1oBFUuNgA _2Mdkc-JYfhYSx7OeQp1gnE _19A7ZA9QZsOiamOlmxEUOV _1K3Tay924QS-JVMY7VF-CE']")))
                bookshift=chrome.find_elements(By.XPATH," //*[@class='_1KsfJ6FtsMi_TEpAVW2Acu _2WQiUC_efpX1jq1Z4e4Elf _2zD8RSltSULvG1oBFUuNgA _2Mdkc-JYfhYSx7OeQp1gnE _19A7ZA9QZsOiamOlmxEUOV _1K3Tay924QS-JVMY7VF-CE']")
                chrome.execute_script("arguments[0].click();", bookshift[book_index])
                confirm_book=WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='_1KsfJ6FtsMi_TEpAVW2Acu a0ikhwNqDK6lyThHjuySS Bp4SrA_22QBVQ-dJ2s1wg _1-zgIC9QCHV80ib9rVy6qR _18xc4kjG26Y6fYRL1KxqLm _31RWXb80r--0C_2J4Czl9g']")))
                confirm_book=chrome.find_elements(By.XPATH,"//*[@class='_1KsfJ6FtsMi_TEpAVW2Acu a0ikhwNqDK6lyThHjuySS Bp4SrA_22QBVQ-dJ2s1wg _1-zgIC9QCHV80ib9rVy6qR _18xc4kjG26Y6fYRL1KxqLm _31RWXb80r--0C_2J4Czl9g']")
                chrome.execute_script("arguments[0].click();", confirm_book[hh])
                print(f"The shift for {dates} of details {shift_text[book_index]} is booked")
                time.sleep(8)
            else:
                print(f"the current shift  not available for time {no_of_shifts_list_time[main]} on date {dates}")
            
            k+=1
            main+=1
    except:
     print(f"NO shifts avalable on {dates} ")
except:
    print("Please check your ingternet connectivity and your input information and try again ,otherwise contact the programmer")
        # bookshift=//*[@class='_1KsfJ6FtsMi_TEpAVW2Acu _2WQiUC_efpX1jq1Z4e4Elf _2zD8RSltSULvG1oBFUuNgA _2Mdkc-JYfhYSx7OeQp1gnE _19A7ZA9QZsOiamOlmxEUOV _1K3Tay924QS-JVMY7VF-CE']
        # confirm_book=//*[@class="_1KsfJ6FtsMi_TEpAVW2Acu a0ikhwNqDK6lyThHjuySS Bp4SrA_22QBVQ-dJ2s1wg _1-zgIC9QCHV80ib9rVy6qR _18xc4kjG26Y6fYRL1KxqLm _31RWXb80r--0C_2J4Czl9g"]