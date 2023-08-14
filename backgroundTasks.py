# moduł w którym przechowywane są zadania wykonwane w tle
import threading
import counterFile

# Tworzenie obiektu Event
event = threading.Event()
# interwał czasowy, w jakim ma być wykonywane zadanie
interval_seconds = 5


# funkcja wywołująca funkcję zapisu do pliku stanu licznika
def save_counter_to_file():
    while True:
        counterFile.save_counter_file(counterFile.counterINT)
        # zawieszenie wykonania na określony czas
        event.wait(interval_seconds)
        # print("test")
        # nie potzebne w tym case
        # event.clear()


# utworzenie nowego wątku i uruchomienie funkcji save_counter_to_file() w tle
bg1_thread = threading.Thread(target=save_counter_to_file)
# Ustawienie wątku na tzw. "daemon", aby zakończył się razem z głównym wątkiem aplikacji
bg1_thread.daemon = True
# start taska w tle zrobiony w flask_app.py
# bg1_thread.start()
