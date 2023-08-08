# moduł w którym przechowywane są zadania wykonwane w tle
import threading
import counterFile


# funkcja wywołująca funkcję zapisu do pliku stanu licznika
def save_counter_to_file():
    while True:
        counterFile.save_counter_file(counterFile.counterINT)

        # interwał czasowy, w jakim ma być wykonywane zadanie
        interval_seconds = 10

        threading.Event().wait(interval_seconds)
