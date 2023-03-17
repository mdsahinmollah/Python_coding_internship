import pyttsx3
text_speech = pyttsx3.init()

name = input("Enter your name : ")

while True:
    qun = input("Enter your question : ")
    if qun == "":
        qun = f"Thank you {name}!"
        text_speech.say(qun)
        text_speech.runAndWait()
        break
    text_speech.say(qun)
    text_speech.runAndWait()
'''
 hello shahin good morning how are you you are too 
 lazy man if you you are not work hard your enemy 
 will successfull and you will fail so work hard 
 and enjoy your life
 '''