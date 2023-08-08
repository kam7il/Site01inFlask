import os
import threading
from flask import Flask, send_from_directory, session
from flask_session import Session
import counterFile, backgroundTasks

# -----------------------------------------------------------------------------------
# stworzenie instancji Flask
app = Flask(__name__)
# -----------------------------------------------------------------------------------
# konfiguracja sesji
# sesja zapisana w systemie plików na serwerze
app.config['SESSION_TYPE'] = 'filesystem'
# czas po którym sesja wygaśnie
app.config['PERMANENT_SESSION_LIFETIME'] = 1200
# inicjalizacja mechanizmu sesji w oparciu o ustawienia obiektu app
Session(app)
# print obecnej konfiguracji Flask-Session
for x, y in app.config.items():
    print(x, "=", y)
# -----------------------------------------------------------------------------------
# załadowanie stanu licznika z pliku do zmiennej
counterFile.counterINT = counterFile.load_counter_file()
# -----------------------------------------------------------------------------------


@app.route('/favicon.ico')
# dodanie favicon
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/pacman_icon.png', mimetype='image/vnd.microsoft.icon')


@app.route("/")
# strona startowa
def start_page():
    # sprawdzenie czy w słowniku jest klucz visited
    if 'visited' not in session:
        counterFile.counterINT += 1
        # ustawienie wartości klucza visited na True
        session['visited'] = True
    return f"""
    <p>Witaj na stronie pierwszy raz</p>
    Licznik: {counterFile.counterINT}
    """


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
if __name__ == "__main__":
    # -------------------------------------------------------------------------------
    # dodanie favicon do aplikacji przy braku @app.route('/favicon.ico')
    # app.add_url_rule('/favicon.ico', 'favicon', favicon)
    # -------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------
    # utworzenie nowego wątku i uruchomienie funkcji save_counter_to_file() w tle
    bg1_thread = threading.Thread(target=backgroundTasks.save_counter_to_file)

    # Ustawienie wątku na tzw. "daemon", aby zakończył się razem z głównym wątkiem aplikacji
    bg1_thread.daemon = True
    bg1_thread.start()
    # -------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------
    # uruchomienie app
    app.run(debug=True)
    # -------------------------------------------------------------------------------
