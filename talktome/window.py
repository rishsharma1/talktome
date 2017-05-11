import pyglet
from transcriber import Transcript

AUDIO_FILES_DIR = '../tests/audio-files/'
I_WANT_TO_DISCUSS_FILE = 'i-wanna-discuss.wav'


class Window(pyglet.window.Window):

    def __init__(self,location):
        super(Window,self).__init__()
        self.set_size(750,750)
        self.label = pyglet.text.Label('hello',
                          font_name='Times New Roman',
                          font_size=36,
                          x=self.width/2, y=self.height/2,
                          anchor_x='center', anchor_y='center')

    def on_draw(self):
        self.clear()
        self.label.draw()




if __name__ == '__main__':
    window = Window()
    filename = AUDIO_FILES_DIR+I_WANT_TO_DISCUSS_FILE
    i_wanna_discuss_transcript = Transcript(filename)
    text = i_wanna_discuss_transcript.text




    pyglet.app.run()