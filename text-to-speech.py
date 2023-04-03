import PySimpleGUI as pi
import pyttsx3 as ps


engine= ps.init()


def speak(text):
    # Setting the voice based on the user's selection
    if values['-MALE-']:
        voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    else:
        voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', voice_id)


# Convert text to speech
    engine.say(text)
    engine.runAndWait()

 
# Define the GUI layout
layout = [[pi.Text("Enter text to convert to speech:",font=('copperplate'))],
          [pi.Input(key="-INPUT-",font=('copperplate')),pi.Button("Speak",font=('copperplate',14))],
          [pi.Text('Select a Voice:',font=('copperplate', 14)), pi.Radio('Male', "RADIO1", default=True, key='-MALE-',font=('copperplate', 14)), pi.Radio('Female', "RADIO1", key='-FEMALE-',font=('copperplate', 14))],
          [pi.Text("Select voice speed (default=200):", font=('copperplate', 14)),pi.Slider(range=(1, 500), default_value=200, orientation='horizontal', key="-SPEED-")],
          [pi.Text("To see the effect of speed adjustment, run the program twice.",font=('copperplate', 10))],
          [pi.Button("Exit",font=('copperplate',14))]]



# Create the GUI window
window = pi.Window("Text-to-Speech App", layout,background_color="teal")


# Event loop to process GUI events
while True:
    event, values = window.read()
    if event == pi.WIN_CLOSED or event == "Exit":
        break


    #Set the voice of the engine
    if event == "Speak":
        text = values["-INPUT-"]
        speak(text)
       

    # Set the speed of the voice
    speed_str = values["-SPEED-"]
    if speed_str:
        speed = int(speed_str)
        engine.setProperty('rate', speed)


# Close the GUI window and release the pyttsx3 engine resources
window.close()
engine.stop()
