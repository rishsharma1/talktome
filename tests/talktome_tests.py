from nose.tools import *
from talktome.transcriber import Transcript
from os import path

AUDIO_FILES_DIR = 'audio-files/'
HELLO_FILE     = 'hello-1.wav'
I_WANT_TO_DISCUSS_FILE = 'i-wanna-discuss.wav'

def test_hello_to_text():
    filename = path.join(path.dirname(path.realpath(__file__)),AUDIO_FILES_DIR+HELLO_FILE)
    hello_transcript = Transcript(filename)
    assert hello_transcript.text == 'hello'

def test_i_wanna_discuss_to_text():
    filename = path.join(path.dirname(path.realpath(__file__)),AUDIO_FILES_DIR+I_WANT_TO_DISCUSS_FILE)
    i_wanna_discuss_transcript = Transcript(filename)
    assert i_wanna_discuss_transcript.text == 'I want to discuss all this behaviour'