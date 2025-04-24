import pyttsx3
import speech_recognition as sr
import webbrowser
import otp
 
def speak(text):
   engine = pyttsx3.init()
   voices = engine.getProperty('voices')
   engine.setProperty('voice',voices[1].id)
   engine.say(text)
   engine.runAndWait() 
def takecommand():
     r = sr.Recognizer()
     with sr.Microphone() as source:
         print("Speak to recognize.....")
         r.pause_threshold = 1
         audio = r.listen(source)
         try:
             print("Recognizing......")
             query = r.recognize_google(audio,language="en-in")
             print(query)
         except:
             print("Speak Again")
             return False
         else:
             return query
def greet():
     greeting = "Hello,how can i help you?"
     speak(greeting)
greet()
while True:
     query = takecommand()
     if query == False: 
         pass
      
     elif "how are you" in query.lower():
         speak("I am doing good, how about you !")
     elif "open flipkart" in query.lower():
         speak("Opening flipkart Website !")
         webbrowser.open("https://www.flipkart.com/")
     elif "send otp" in query.lower():
         speak("Enter Email address: ")
         x = input("Enter email here: ")
         otp.otp(x)
         speak("otp sent successfully.")
     elif "shut down" in query.lower():
        speak(" Take care, bye !")
        break
     elif "open meesho" in query.lower():
         speak("Opening meesho Website !")
         webbrowser.open("https://www.meesho.com/")
     elif"open web page" in query:
        speak("Opening codegnan website!")
        webbrowser.open("https://codegnan.com/")
     elif "open amazon" in query.lower():
         speak("Opening amazon Website !")
         webbrowser.open("https://www.amazon.in")


if __name__ == "__main__":
   main()
   
         

   
         
    

         
         
