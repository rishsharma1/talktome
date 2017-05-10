import speech_recognition as sr


class Transcript:

    def __init__(self,filename):
        self.audio_file = filename
        self.recogniser = sr.Recognizer()
        self.text = self.convert_to_text()


    def convert_to_text(self):
        with sr.AudioFile(self.audio_file) as source:
            audio = self.recogniser.record(source)
        try:
            return self.recogniser.recognize_google(audio)
        except sr.UnknownValueError:
            print "Error: Could not understand the audio."
        except sr.RequestError as e:
            print "Error: Could not request results; {0}".format(e) 