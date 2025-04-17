# I currently do not use this module because pythonanywhere does not support threads
# a module where tasks performed in the background are stored
import threading
import counterFile

event = threading.Event()
# time interval in which the task is to be performed
interval_seconds = 5


# function calling the function for writing the counter status to a file
def save_counter_to_file() -> None:
    while True:
        counterFile.save_counter_file(counterFile.counterINT)
        # suspension of execution for a specified period
        event.wait(interval_seconds)
        # print("test")
        # not needed in this case
        # event.clear()


# creating a new thread and running the save_counter_to_file() function in the background
bg1_thread = threading.Thread(target=save_counter_to_file)
# Setting the thread to a so-called "daemon" so that it ends together with the main application thread
bg1_thread.daemon = True
# background task start done in flask_app.py
# bg1_thread.start()
