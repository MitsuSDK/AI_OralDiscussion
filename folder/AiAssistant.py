# accept voice input and turn it into text

import speech_recognition as sr



def speech_to_text():

    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 2.0  # wait 2 seconds of silence

    ''' recording the sound '''

    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Done recording")

    ''' Recorgnizing the Audio '''
    try:
        print("Recognizing the text")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="en-US"
            )
        #print("Decoded Text : {}".format(text))

        return text
    
    except Exception as ex:
        print(ex)

output_of_speech = speech_to_text()
print("This is what I said: ", output_of_speech)