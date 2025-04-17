# counter module
from pathlib import Path

# path for cross-platform scripts
THIS_FOLDER = Path(__file__).parent.resolve()
# path to the file with the counter status
counterFilePath = THIS_FOLDER / "saved_data/counter_file.txt"

# initial counter status
counterINT = 0


# loading the counter status from a file
def load_counter_file() -> int:
    with open(counterFilePath, mode="r", encoding="utf-8") as file:
        return int(file.readline())


# saving the counter status to a file
def save_counter_file(counter: int) -> None:
    with open(counterFilePath, mode="w", encoding="utf-8") as file:
        file.write(str(counter) + "\n")
