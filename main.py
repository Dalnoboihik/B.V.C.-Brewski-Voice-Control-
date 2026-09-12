import threading
import webbrowser
import speech_recognition as sr
import interface

r = sr.Recognizer()
print("Ассистент успешно запущен")


def listen_loop():
    while True:
        with sr.Microphone() as src:
            try:
                cmd = r.recognize_google(r.listen(src), language='RU')
                print(f"Вы: {cmd}")

                # показываем в окне
                interface.set_text(f"Вы: {cmd}")

                if "браузер" in cmd:
                    webbrowser.open("https://ya.ru/?npr=1")
                elif "погода" in cmd:
                    webbrowser.open("https://yandex.ru/pogoda/ru/10723")

            except Exception as e:
                print(f"Ошибка: {e}")


threading.Thread(target=listen_loop, daemon=True).start()

interface.root.mainloop()