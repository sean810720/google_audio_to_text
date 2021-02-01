import speech_recognition as sr

filename = input("請輸入檔名: ")

# obtain audio
r = sr.Recognizer()

# obtain audio from the .wav
WAV = sr.AudioFile('audio/' + filename)

with WAV as source:
    audio = r.record(source)
    try:
        print("系統辨識語音檔內容:")
        print(r.recognize_google(audio, show_all=False, language="zh-TW"))

    except sr.UnknownValueError:
        print("系統無法理解這段語音")

    except sr.RequestError as e:
        print("服務無回應: {0}".format(e))
