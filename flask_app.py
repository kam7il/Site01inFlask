import os

from flask import Flask, send_from_directory, session, render_template
from flask_session import Session

# importy moich modułów
import backgroundTasks
import counterFile
import timeCalc

# -----------------------------------------------------------------------------------
# stworzenie instancji Flask
app = Flask(__name__)
# -----------------------------------------------------------------------------------
# konfiguracja sesji
# sesja zapisana w systemie plików na serwerze
app.config['SESSION_TYPE'] = 'filesystem'
# czas po którym sesja wygaśnie
# app.config['PERMANENT_SESSION_LIFETIME'] = 1200
# inicjalizacja mechanizmu sesji w oparciu o ustawienia obiektu app
Session(app)
# print obecnej konfiguracji Flask-Session
# for x, y in app.config.items():
#     print(x, "=", y)
# -----------------------------------------------------------------------------------
# załadowanie stanu licznika z pliku do zmiennej
counterFile.counterINT = counterFile.load_counter_file()
# start taska w tle do zapisu stanu licznika wejść
backgroundTasks.bg1_thread.start()
# -----------------------------------------------------------------------------------


# co ma być zrobione przed requestem
@app.before_request
def before_request():
    # ustawienie wygaśnięcia sesji na północ
    app.permanent_session_lifetime = timeCalc.time_calc_to_midnight()


# dodanie favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'images/pacman_icon.png', mimetype='image/vnd.microsoft.icon')


# strona startowa
@app.route("/")
def start_page():
    # ustawienie zmiennej visited na True lub False, gdy nie ma klucza visited, domyślnie False
    visited = session.get('visited', False)
    # sprawdzenie czy w słowniku jest klucz visited
    if 'visited' not in session:
        # zwiększenie licznka wejść na stronę, gdy osoba wchodzi pierwszy raz
        counterFile.counterINT += 1
        # ustawienie wartości klucza visited na True
        session['visited'] = True

    return render_template('start_page.html', visited=visited, counter=counterFile.counterINT)


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
if __name__ == "__main__":
    # -------------------------------------------------------------------------------
    # dodanie favicon do aplikacji przy braku @app.route('/favicon.ico')
    # app.add_url_rule('/favicon.ico', 'favicon', favicon)
    # -------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------
    # uruchomienie app
    # przy włączonym debug, wątki są uruchamiane podwójnie. Test z print("test") w save_counter_to_file()
    # app.run(debug=True)
    app.run()
    # -------------------------------------------------------------------------------
