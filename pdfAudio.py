import PyPDF2
import pyttsx3
#import os
#from gtts import gTTS
#from tts_watson.TtsWatson import TtsWatson

#-----------------------------------------         EXTRACTING TEXT FROM PDF       --------------------------------------#
pdfFileObj = open("quotes.pdf", "rb") #Put your pdf file name here 

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
  pageObj = pdfReader.getPage(pageNum)

  mytext += pageObj.extractText()

pdfFileObj.close()
#print(mytext)

#------------------------------------------           READING PDF OFFLINE         --------------------------------------#
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'en+m5')
engine.say(mytext)
engine.runAndWait()


#ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice') # en-US_AllisonVoice is a voice from watson you can found more to: https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/doc/text-to-speech/using.shtml#voices 
#ttsWatson.play(mytext) 
#-----------------------------------------       CONVERTING PDF TO AUDIO FILE     --------------------------------------#
#tts = gTTS(text=mytext, lang='en')
#tts.save("quotes.mp3")

#----DELET AUDIO FILE AFTER LISTENING----#
#os.system("mpg321 quotes.mp3")
#os.remove("quotes.mp3")