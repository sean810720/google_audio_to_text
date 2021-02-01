import speech_recognition as sr

# obtain audio
r = sr.Recognizer()

with sr.Microphone() as source:

    # listen for 5 seconds and create the ambient noise energy level
    print("麥克風準備中, 請稍等...")
    r.adjust_for_ambient_noise(source, duration=5)

    print("開始說話")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    print("系統辨識出您剛剛說:")
    print(r.recognize_google(audio, language="zh-TW"))

except sr.UnknownValueError:
    print("系統無法理解這段語音")

except sr.RequestError as e:
    print("服務無回應: {0}".format(e))
