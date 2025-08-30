import speech_recognition as sr
import pyttsx3
import pyautogui
import subprocess
import os
# from openai import OpenAI


# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )
# Initialize the TTS engine
engine = pyttsx3.init()

# Adjust volume and rate
engine.setProperty('volume', 0.6)  # Set volume (0.0 to 1.0)
engine.setProperty('rate', 150)   # Set speech rate

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("I'm listening.")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""
        except OSError as e:
            speak("Microphone is not working. Please check your device.")
            print(f"Microphone error: {e}")
            return ""

def perform_action(command):
    if "open browser" in command:
        speak("Opening your web browser.")
        subprocess.run(["vivaldi"])  # Opens Vivaldi
    elif "open firefox" in command:
        speak("opening firefox")
        subprocess.run(["firefox"])
    elif "open terminal" in command:
        speak("Opening terminal.")
        subprocess.run(["gnome-terminal"])
    elif "open file manager" in command:
        speak("Opening file manager.")
        subprocess.run(["nautilus"])
    elif "close file manager" in command:
        speak("closing file manager.")
        subprocess.run(["pkill", "nautilus"])
    elif "close browser" in command:
        speak("Closing Your web browser")
        subprocess.run(["pkill", "vivaldi"])
        subprocess.run(["pkill", "firefox"])
    elif"close terminal" in command:
        speak("closing terminal")
        subprocess.run(["pkill", "gnome-terminal"])

    elif "shutdown now" in command:
        
        speak("shutting down now")
        subprocess.run(["shutdown", "now"])
       
    elif "shutdown" in command:
         
         hey = pyautogui.confirm(text="Are you sure you want to shutdown?", title="Shutdown Confirmation", buttons=["Yes", "No"])
         if hey == "Yes":
             speak("BYE bye! shutting down")
             subprocess.run(["shutdown", "now"])
         elif hey == "No":
             speak("shutting down cancelled")
         else:
                print("no valid response received")
    elif "exit" in command:
        speak("Goodbye!")
        engine.stop()  # Stop the TTS engine
        exit()
    else:
        speak("Sorry, I don't know how to do that.")


def wake_word_detected():
    recognizer  =sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for Magical Word Key....")
        try:
            
            command = pyautogui.confirm(text="waiting for magical word key", title = "Agent is stop confirm to start", buttons=['Start', 'exit'])
            if command == "Start":
                command = listen()
                if "hello jarvis" or "mayank" in command:
                    speak("hello mayank, how can i help you?")
                    return command.lower()
            elif command == "exit":
                return command.lower()
        except:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                return command.lower()
            except:
                return ""
                


# Main loop
if __name__ == "__main__":
    speak("Hello! I am your assistant.")
    Start = True
    if Start:
        command = wake_word_detected()
        if "exit" in command:
            speak("Goodbye!")
            perform_action(command)
        
        elif "Hey Jarvis" in command or "hey jarvis" in command or "Start" in command:
            speak("how can i help you?")
            

            while Start:
                command = listen()
                if not command:
                    print("no command recieved")
                    continue                   
                elif command:
                    # pyautogui.alert(text=f"You said: {command}", title="Command Received", button="OK")
                    if Start:
                        perform_action(command)
             

          

# if command in ["no command", "network error", "microphone error"]:
#     result = pyautogui.alert(text="No valid command received. What would you like to do?",
#                              title="Command Error",
#                              button=["Retry", "Stop Listening"])
#     if result == "Retry":
#         continue
#     elif result == "Stop Listening":
#         Start = False
