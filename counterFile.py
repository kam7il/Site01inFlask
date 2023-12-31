# moduł licznka wejść
# stan początkowy licznika
counterINT = 0
# ścieżka do pliku z stanem licznika
counterFilePath = "./saved_data/counter_file.txt"


# wczytanie stanu licznika z pliku
def load_counter_file():
    with open(counterFilePath, mode="r", encoding="utf-8") as file:
        return int(file.readline())


# zapisanie stanu licznika do pliku
def save_counter_file(counter):
    with open(counterFilePath, mode="w", encoding="utf-8") as file:
        file.write(str(counter))
