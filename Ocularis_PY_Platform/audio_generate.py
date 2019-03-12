from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
import playsound
import os

os.chdir(os.path.join(os.getcwd(),'tempaud'))
# The text that you want to convert to audio
mytext = 'may I please know which network you would like to connect to, use S to select and A to next'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed

boly = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']
bol = ['process finished']
for i in bol:
    myobj = gTTS(text=i, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save(i+".mp3")

    playsound.playsound(i+'.mp3')
