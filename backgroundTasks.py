# moduł w którym przechowywane są zadania wykonwane w tle
import threading
import counterFile

# Tworzenie wspólnego obiektu Event
event = threading.Event()


# funkcja wywołująca funkcję zapisu do pliku stanu licznika
def save_counter_to_file(event_):
    while True:
        counterFile.save_counter_file(counterFile.counterINT)

        # interwał czasowy, w jakim ma być wykonywane zadanie
        interval_seconds = 10

        # zawieszenie wykonania na określony czas
        event_.wait(interval_seconds)
        print("test")


# start taska w tle
def bg1_thread_start():
    # utworzenie nowego wątku i uruchomienie funkcji save_counter_to_file() w tle
    bg1_thread = threading.Thread(target=save_counter_to_file, args=(event,))
    # Ustawienie wątku na tzw. "daemon", aby zakończył się razem z głównym wątkiem aplikacji
    bg1_thread.daemon = True
    bg1_thread.start()
