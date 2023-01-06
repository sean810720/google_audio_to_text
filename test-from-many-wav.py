import speech_recognition as sr
import os

# obtain audio
r = sr.Recognizer()
r.energy_threshold = 300

# 所有辨識出來的資料
result = []

# 取得 audio/batch 資料夾內所有檔名
all_file_names = os.listdir(os.path.dirname(
    os.path.realpath(__file__)) + "/audio/batch")

# 批次辨識解析
for file_name in all_file_names:
    WAV = sr.AudioFile('audio/batch/' + file_name)

    try:
        with WAV as source:

            # 降噪處理
            r.adjust_for_ambient_noise(source, duration=0.5)

            # 降噪後音檔
            audio = r.record(source)

            try:
                # 目前使用預設的 API key
                # 使用其他 KEY: r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
                result.append(r.recognize_google(
                    audio, show_all=False, language="zh-TW"))
                # result.append(r.recognize_google(audio, show_all=False, language="en-US"))

            except sr.UnknownValueError:
                pass

            except sr.RequestError:
                pass
    except:
        pass

print("\n語音辨識內容:\n")
print(result)
