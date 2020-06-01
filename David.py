import pyttsx3  #pip install pyttsx3 [for audio]
from translate import Translator #pip install translate    
import datetime
import speech_recognition as sr
import wikipedia   #pip install wikipedia [to search on wikipedia]
import webbrowser
from gtts import gTTS   # google text to speech
import playsound
import os #used to interact with system directly
import random   #pip install random
import wolframalpha # to calculate strings into formula, its a website which provides api, 100 times per day
import smtplib #to send mail
import sys  #pip install sys
import cv2   #pip install opencv-python   [used to access camera]
import ctypes #to change desktop wallapaper
import pyautogui as pya #to control mouse, keyboard and other gui tasks
import pyperclip  # handy cross-platform clipboard text handler
import time
import psutil #to get cpu usage, battery remaining many more
from selenium import webdriver  # to control browser operations
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui #to take a screenshot

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    print("David : ", audio)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon")
    else :
        speak("Good Evening")


def takeCommand():
    #take microphones query from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Didn't recognize, please say that again.")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gborse3215@gmail.com','@gaurav@')
    server.sendmail('gborse3215@gmail.com', to, content)
    server.close()

#Command as : search on youtube carryminati 
def search_web(query):
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()
    wait = WebDriverWait(driver, 3)
    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located
    #Command as : search on youtube carryminati 
    if 'youtube' in query.lower():
        speak("Opening in youtube")
        indx = query.lower().split().index('youtube')
        query = query.split()[indx+1:]
        driver.get("https://www.youtube.com/results?search_query=" + str(query))
        # play the video
        wait.until(visible((By.ID, "video-title")))
        driver.find_element_by_id("video-title").click()
        return
    #Command as : search on wikipedia carryminati 
    elif 'wikipedia' in query.lower():
        speak("Opening Wikipedia")
        indx = query.lower().split().index('wikipedia')
        query = query.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
    
    else:
        if 'google' in query:
            indx = query.lower().split().index('google')
            query = query.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        elif 'search' in query:
            indx = query.lower().split().index('google')
            query = query.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
        else:
            driver.get("https://www.google.com/search?q=" + '+'.join(query.split()))
        return

def open_application(query):
    if "chrome" in query:
        speak("Opening Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "firefox" in query or "mozilla" in query:
        speak("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return

    elif "word" in query:
        speak("Opening Microsoft Word")
        os.startfile('C:\Program Files\Microsoft Office\\root\\Office16\\WINWORD.EXE')
        return

    elif "excel" in query:
        speak("Opening Microsoft Excel")
        os.startfile('C:\Program Files\Microsoft Office\\root\\Office16\\EXCEL.EXE')
        return

    elif "notepad" in query:
        speak("Opening Notepad")
        os.startfile('C:\Windows\system32\\notepad.exe')
        return

    elif 'youtube' in query:
        speak("Opening youtube")
        webbrowser.get(chrome_path).open("youtube.com")
        return

    elif 'google' in query:
        speak("Opening google")
        webbrowser.get(chrome_path).open("google.com")
        return

    elif ( 'code' in query ) or ( 'visual studio code' in query ):
        #codePath = the target path of corresponding software u wnat to open 
        codePath = "C:\\Users\\gbors\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
        speak("Opening visual studio Code..")
        os.startfile(codePath)
        return
         
    elif ( 'sublime' in query ) or ( 'sublime text editor' in query ):
        codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        speak("Opening sublime Text Editor.")
        os.startfile(codePath)
        return

    elif ('pycharm' in query ):
        codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
        speak("Opening PyCharm")
        os.startfile(codePath)
        return

    elif 'explorer' in query:
        speak("Opening File Explorer")
        p = os.system('explorer.exe ')
        return

    elif ( 'documents' in query ) or ( 'documents' in query ):
        speak("Opening Documents")
        os.startfile("C:\\Users\\gbors\\Documents")
        return

    elif ( 'downloads' in query ) or ( 'download' in query ):
        speak("Opening Downloads")
        os.startfile("C:\\Users\\gbors\\Downloads")
        return

    elif 'desktop' in query:
        speak("Opening Dekstop")
        os.startfile("C:\\Users\\gbors\\Desktop")
        return

    elif 'my computer' in query:
        speak("Opening My Computer")
        os.system('This PC')
        return

    else:
        speak("Application not available")
        return

def closeApplication(query):

    if "chrome" in query:
        speak("Closing Google Chrome")
        os.system("taskkill /f /im chrome.exe")
        return

    elif "firefox" in query or "mozilla" in query:
        speak("Closing Mozilla Firefox")
        os.system("taskkill /f /im firefox.exe")
        return

    elif "word" in query:
        speak("Closing Microsoft Word")
        os.system("taskkill /f /im WINWORD.EXE")
        return

    elif "excel" in query:
        speak("Closing Microsoft Excel")
        os.system("taskkill /f /im EXCEL.EXE")
        return

    elif 'notepad' in query:
        speak("Closing Notepad")
        os.system('taskkill /f /im notepad.exe')
        return

    elif 'youtube' in query:
        speak("Closing youtube")
        os.system("taskkill /f /im chrome.exe")
        return

    elif 'google' in query:
        speak("Closing google")
        os.system("taskkill /f /im chrome.exe")
        return

    elif ('code' in query) or ('visual studio code' in query):
        speak("Closing visual studio Code..")
        os.system("taskkill /f /im pycharm64.exe")
        return

    elif ('sublime' in query) or ('sublime text editor' in query):
        speak("Closing sublime Text Editor.")
        os.system("taskkill /f /im sublime_text.exe")
        return

    elif ('pycharm' in query):
        speak("Closing PyCharm")
        os.system("taskkill /f /im pycharm64.exe")
        return

    # elif 'explorer' in query:
    #     speak("Closing File Explorer")
    #     os.system("taskkill /f /im explorer.exe")
    #     return
    #
    # elif ('documents' in query) or ('document' in query):
    #     speak("Closing Documents")
    #     os.system("taskkill /f /im C:\\Users\\gbors\\Documents")
    #     return
    #
    # elif ('downloads' in query) or ('download' in query):
    #     speak("Closing Downloads")
    #     os.system("taskkill /f /im Downloads")
    #     return
    #
    # elif 'desktop' in query:
    #     speak("Closing Dekstop")
    #     path = "Desktop"
    #     os.close(path)
    #     return

    else:
        speak("Application not available to close")
        return

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+usage)

def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def authentication():
    speak("Hello and Welcome sir, I am david. Your Digital Assistant.")
    speak("Sir, I need to authenticate you. Because, this program is only for authorized users.")
    speak("If you are authorized user then please authenticate yourself with your special word.")
    auth_key = "i am your boss"
    query = takeCommand().lower()
    if query == auth_key:
        speak("Yes, i recognized you, you are authorized user. and you are successfully logged in.")
    else:
        speak("ok, you are not a authorized user. so you can't use this program. i am sorry but i am going offline ")
        quit()

def gooffline():
    speak('Closing all system applications.')
    speak('Disconnecting to servers.')
    speak('Going offline.')
    image_file = "F:\\Wallpaper\\"
    files = os.listdir(image_file)
    d = random.choice(files)
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 1
    os.system("taskkill /f /im Rainmeter.exe")
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(image_file + d), SPIF_UPDATEINIFILE)
    quit()

def online():
    speak('Starting all system applications.')
    speak('Connecting to servers.')
    speak('Installing all drivers.')
    image_file = "IronMan_wall.jpg"
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 1
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(image_file), SPIF_UPDATEINIFILE)
    os.startfile("C:\Program Files\Rainmeter\Rainmeter.exe")
    #os.system('start C:\\Program Files\\Rainmeter')
    speak('Every driver is installed.')
    speak('All system applications have been started.')
    speak('Now i am online Sir .')
    wishMe()
    strDate = datetime.datetime.today().strftime("%d %B %y")
    speak(f"Sir, today's date is {strDate}.")
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"and the time is {strTime}.")
    speak("Now i am ready for your commands.")

def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)  # ctrl-c is usually very fast but your program may execute faster
    return pyperclip.paste()

def TakePhoto():
    if ('picture' in query):
        camera_port = 0
        speak("Checking for camera availability.")
        speak("Clicking your Picture. Sir smile please.")
        camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
        # Check if the webcam is opened correctly
        if not camera.isOpened():
            raise IOError("Cannot open webcam")
        grabbed, image = camera.read()
        speak("Your picture is clicked. it looks really nice.")
        speak("lets take a look.")
        print("Instuctions : please Press Q to quit")
        speak("please Press Q to quit")

        while (camera.isOpened()):
            if grabbed:
                # out.write(image)
                cv2.imshow('pic.jpg', image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    # cv2.waitKey(1) & 0xFF == ord('q') or stop recording' in c
                    out = cv2.imwrite('Image Clicked\\pic.jpg', image)
                    speak("Picture has been saved.")
                    break
            else:
                break
        camera.release()
        cv2.destroyAllWindows()

    elif 'screenshot' in query:
        speak("Taking a screenshot..")
        ss = pyautogui.screenshot()
        strDate = datetime.datetime.today().strftime("%d-%b-%y_")
        strTime = datetime.datetime.now().strftime("%H %M %S")
        ssName = "Screenshots\\"+strDate+strTime+".png"
        ss.save(ssName)
        speak("Screenshot captured. and saved to storage.")


    elif ('selfie' in query):
        camera_port = 0
        speak("Checking for camera availability.")
        speak("Clicking your Picture. Sir smile please.")
        camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
        # Check if the webcam is opened correctly
        if not camera.isOpened():
            raise IOError("Cannot open webcam")
        grabbed, image = camera.read()
        speak("Your picture is clicked. it looks really nice.")
        speak("lets take a look.")
        print("Instuctions : please Press Q to quit")
        speak("please Press Q to quit")

        while (camera.isOpened()):
            if grabbed:
                # out.write(image)
                cv2.imshow('pic.jpg', image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    # cv2.waitKey(1) & 0xFF == ord('q') or stop recording' in c
                    out = cv2.imwrite('Image Clicked\\pic.jpg', image)
                    speak("Picture has been saved.")
                    break
            else:
                break
        camera.release()
        cv2.destroyAllWindows()

    elif ('photo' in query):
        camera_port = 0
        speak("Checking for camera availability.")
        speak("Clicking your Picture. Sir smile please.")
        camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
        # Check if the webcam is opened correctly
        if not camera.isOpened():
            raise IOError("Cannot open webcam")
        grabbed, image = camera.read()
        speak("Your picture is clicked. it looks really nice.")
        speak("lets take a look.")
        print("Instuctions : please Press Q to quit")
        speak("please Press Q to quit")

        while (camera.isOpened()):
            if grabbed:
                # out.write(image)
                cv2.imshow('pic.jpg', image)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    # cv2.waitKey(1) & 0xFF == ord('q') or stop recording' in c
                    out = cv2.imwrite('Image Clicked\\pic.jpg', image)
                    speak("Picture has been saved.")
                    break
            else:
                break
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # authentication()
    # online()
    #speak("Hello sir, this program is only for authenticate user. Unauthorised person cannot use me. If you are authorised user then please authenticate yourself with your speacial word")
    while True:
        # Logic for executing tasks based on query
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        query = takeCommand().lower()
        # if 'authenticate' in query:
        #     speak("ok you are successfully logged in")
        # elif 'no i am not a root user' in query:
        #     speak("ok, you are not a authenticate user. so you can't use me. i am sorry. I am going offline ")
        #     break

    #Open Application
        if 'open' in query:
            open_application(query.lower())
    #//Open Application

    #CPU and Battery Usage
        elif 'cpu' in query:
            cpu()

        elif 'battery' in query:
            battery()
    #//CPU and Battery Usage

    #Change Wallpaper
        elif 'change desktop wallpaper' in query or 'change wallpaper' in query:
            speak("Changing Desktop wallpaper..")
            image_file = "F:\\Wallpaper\\"
            files = os.listdir(image_file)
            d = random.choice(files)
            SPI_SETDESKWALLPAPER = 20
            SPIF_UPDATEINIFILE = 1
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, os.path.abspath(image_file + d),SPIF_UPDATEINIFILE)
            speak("Wallpaper Changed. it looks nice. i hope you like it.")

    #Close Application
        elif 'close' in query:
            closeApplication(query.lower())
    #//Close Application

    #search
        elif 'search' in query: #or 'play' in query
            search_web(query.lower())
    #//search

    #Folder Management
        elif ('create folder' in query) or ('create a folder' in query) or ('create directory' in query) or ('create a directory' in query):
            print("Instructions : Please answer in Yes or NO ")
            speak("Sir, i need your confirmation. Do you wish to create a directory..?")
            creatDir = takeCommand()
            if 'yes' in creatDir:
                rmDir = "Creating a directory.","Creating a folder."
                speak(random.choice(rmDir))
                speak("Whats to name the folder.")
                creatDir2 = takeCommand()
                os.mkdir("D:\\Python AI Assistant\\" + creatDir2)
                is_temp2 = os.access("D:\\Python AI Assistant\\",os.F_OK)
                if is_temp2 == True:
                    speak("Directory is successfully created.")
                elif is_temp2 == False:
                    speak("There is an error while creating a directory.")
            elif 'no' in creatDir:
                speak("Ok sir, Let it be sir. Give me next command")
            
            else:
                speak("Sir, please provide a valid response")

        elif ('remove folder' in query) or ('remove a folder' in query) or ('remove directory' in query) or ('remove a directory' in query):
            rmDir2 = "Removing a directory.","Deleting a folder."
            speak(random.choice(rmDir2))
            speak("Which folder or directory do you wish to remove")
            rmFolder = takeCommand()
            os.rmdir("D:\\Python AI Assistant\\" + rmFolder )
            is_temp = os.access("D:\\Python AI Assistant\\",os.F_OK)
            # print(os.listdir)
            #print(is_temp)
            if is_temp == True:
                speak("Directory is removed successfully.")
            elif is_temp == False:
                speak("Sorry sir, Directory is not removed.")
            else:
                speak("Sorry sir i can't remove directory right now. please try again later.")
    #//Folder Management   
    
    #Trasnlator
        elif 'translate' in query:
            speak("Whats should i translate?")
            trans_content = takeCommand()
            speak("In which language you wish to translate?")
            trans_Lang = takeCommand()
            translator= Translator(to_lang=trans_Lang)
            translation = translator.translate(trans_content)
            speak("Translation of  : " + trans_content + " is " + translation)
    #//Trasnlator

    #Logout, shutdown and restart
        elif 'logout' in query: #logout
            speak("Sir, Do you really wish to logout from your system.")
            data = "yes"
            query = takeCommand().lower()
            if query == data:
                speak("Closing all running programs. All programs are successfully closed. Logging out.")
                os.system("shutdown -l")
            else:
                speak("Ok sir, no problem.")

        elif 'shutdown' in query: #shutdown
            speak("Sir, Do you really wish to shutdown your system.")
            data = "yes"
            query = takeCommand().lower()
            if query == data:
                speak("Closing all running programs. All programs are successfully closed. Shutting down.")
                os.system("shutdown /s /t 1")
            else:
                speak("Ok sir, no problem.")

        elif 'restart' in query: #restart
            speak("Sir, Do you really wish to restart your system.")
            data = "yes"
            query = takeCommand().lower()
            if query == data:
                speak("Closing all running programs. All programs are successfully closed. Restarting.")
                os.system("shutdown /r /t 1")
            else:
                speak("Ok sir, no problem.")
    #//Logout, shutdown and restart

    #Remember
        elif 'remember that' in query:
            speak("What should i remember?")
            query = takeCommand()
            speak("You said to remember that "'"'+query+'"')
            fileName = "Reminders\\Reminder.txt"
            remember = open(fileName, 'a+')
            strDate = datetime.datetime.today().strftime("%d-%b-%y")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            remember.write(strDate+" "+strTime+" -> "+ query+"\n")
            remember.close()

        elif ('reminder' in query) or ('reminders' in query):
            fileName = "Reminders\\Reminder.txt"
            remember = open(fileName, 'r')
            speak("Ok, wait a movement, i am trying to get your reminders.")
            speak("You told me to remember that "+remember.read())
    #//Remember

    #simpe quetions
        elif ( 'Hey' in query ) or ( 'hello' in query ) or ( 'hi' in query ):
            iamhere = "Yes Sir, i am hearing you. please tell what can i do for you.","Ya sir, i am here. give me command sir"
            speak(random.choice(iamhere))
            
        elif ( 'about yourself' in query ) or ( 'about you' in query ):
            speak("Hii sir, I am David 2 point o, I am your personal assistant. and I am here to help you and make your life easier sir. ohh sorry i forgot to tell you, i am made by Gaurav.")

        elif 'features' in query  or 'what can you do' in query:
            speak("I have lots of features like, i can search any information on wikipedia. can open youtube, google, code, sublime on your one command. can play music for you. and can also send email for u. thats it.")

        elif ( 'thank you' in query ) or ( 'thanks' in query ) :
            great = "Welcome sir","No mention sir","This is my job sir, Dont need to thank me"
            greatLast = ", give me a next command. i am waiting."
            speak(random.choice(great) + greatLast )

        elif 'how are you' in query:
            speak("I am fine sir. Thanks for asking. and what about you sir.")
            great = takeCommand()
            speak("Ohh thats really nice sir.")
    #//simpe quetions 

    #copy text
        elif 'copy text' in query:
            # double clicks on a position of the cursor
            pya.doubleClick(pya.position())
            list = []
            var = copy_clipboard()
            list.append(var)
            print(list)
    #//copy text


    #playing audio music ( randomly selects a song to play from specified directory )
        elif ( 'play music' in query ) or ( 'play musics' in query )or ( 'play song' in query )or ( 'play songs' in query):
            path="F:\\Songs\\" 
            files=os.listdir(path)
            d=random.choice(files)
            speak("Opening Groove Music. Enjoy ur music sir")
            os.startfile(path + d)
    #//playing audio music ( randomly selects a song to play from specified directory )

    #time and data
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        
        elif 'date' in query:
            strDate = datetime.datetime.today().strftime("%d %B %y")
            print(strDate)
            speak(f"Sir, today's date is {strDate}")
    #//time and data    
        
    #take picture    
        elif ( 'click' in query ) or ( 'take' in query ):
            TakePhoto()
    #//take picture

    #records video
        elif ( 'record video' in query ) or ( 'record a video' in query ):
            speak("Recording a video.")
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('Recorded Video\\output.mp4', -1, 20.0, (640,480))
            print("Instuctions : please Press Q to stop recording")
            speak("please Press Q to stop recording")
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:
                    out.write(frame)
                    cv2.imshow('Recording Video..',frame)
                    #c = takeCommand()
                    if cv2.waitKey(1) & 0xFF == ord('q'): 
                        #cv2.waitKey(1) & 0xFF == ord('q') or stop recording' in c
                        speak("Video has been saved.")
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()
    #//records video

    #calculations
        elif "calculate" in query.lower():
            app_id= "YYGX8P-UY3E49LV53"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
    #//calculations

    #send email to anyone
        elif ( 'send email' in query ) or ( 'email' in query ):
            Gaurav = "gborse108@gmail.com"
            Suraj = "sheteshaurya8@gmail.com"
            reply = "ya sure sir, i'll definetly do it for you."
            try:
                if 'gaurav' in query:
                    speak(reply)
                    speak("What should I say?")
                    content = takeCommand()
                    to = Gaurav    
                    sendEmail(to, content)
                    speak("Email has been sent to gaurav.")

                elif ('suraj' in query ) or ('Suraj' in query ):
                    speak(reply)
                    speak("What should I say?")
                    content = takeCommand()
                    to = Suraj   
                    sendEmail(to, content)
                    speak("Email has been sent to suraj.")
            
                elif 'email' in query:
                    speak("Whom should you wish to send email.?")
                    to = takeCommand()
                    if ('Gaurav' in to ) or ('gaurav' in to):
                        speak(reply)
                        speak("What should I say?")
                        content = takeCommand()
                        to = Gaurav    
                        sendEmail(to, content)
                        speak("Email has been sent to gaurav.")
                    elif ('suraj' in to ) or ('Suraj' in to ):
                        speak(reply)
                        speak("What should I say?")
                        content = takeCommand()
                        to = Suraj   
                        sendEmail(to, content)
                        speak("Email has been sent to suraj.")
                    else:
                        speak("Please provide a valid recipient")
                   
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
    #//send email to anyone

    #close program
        elif ( 'offline' in query ) or ( 'turn off' in query ) or ( 'quit' in query ) or ( 'bye' in query ) or ( 'meet you soon' in query )  or ( 'goodbye' in query ):
            extPro = "I am going offline, Take care sir","i am quiting","Bye","Bye. meet you soon.","I am shutting down, Have a nice day","Goodbye. meet u soon"
            speak("Ok sir, " + random.choice(extPro))
            gooffline()
            #sys.exit(0)
    #//close program