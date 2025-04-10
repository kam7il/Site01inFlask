from flask import Flask, session, render_template
from flask_session import Session
from datetime import timedelta

# import my modules
import counterFile
from timeCalc import time_calc_to_midnight_utc

# -----------------------------------------------------------------------------------
# creating a Flask instance
app = Flask(__name__)
# -----------------------------------------------------------------------------------
# session configuration
# session saved in the file system on the server
app.config['SESSION_TYPE'] = 'filesystem'

# Make sure cookies are secure (HTTPS) | to samesite option
# https://developer.mozilla.org/docs/Web/HTTP/Headers/Set-Cookie/SameSite
app.config['SESSION_COOKIE_SECURE'] = True

# Set the SameSite attribute
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# time after which the session will expire
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
# app.config['PERMANENT_SESSION_LIFETIME'] = 1200

# initialization of the session mechanism based on the app object settings
Session(app)

# print current Flask-Session configuration
# for x, y in app.config.items():
#     print(x, "=", y)

# -----------------------------------------------------------------------------------
# loading the counter status from a file into a variable
counterFile.counterINT = counterFile.load_counter_file()
# -----------------------------------------------------------------------------------


# what has to be done before the request
@app.before_request
def before_request():
    # Set session expiration to midnight UTC
    seconds_to_midnight = time_calc_to_midnight_utc()
    session.permanent = True
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=seconds_to_midnight)


# home page
@app.route("/")
def start_page():
    # setting the visited variable to True or False when there is no visited key, defaults to False
    visited = session.get('visited', False)
    personal_counter = session.get('personal_counter', 0)
    # check if the dictionary contains the key visited
    if 'visited' not in session:
        # increasing the number of visits to the page when a person enters for the first time
        counterFile.counterINT += 1
        # calling the function that saves the counter status to a file
        counterFile.save_counter_file(counterFile.counterINT)
        # setting the visited key value to True
        session['visited'] = True
        # counter for session
        personal_counter += 1
        session['personal_counter'] = personal_counter
        personal_counter = session.get('personal_counter')
    else:
        personal_counter += 1
        session['personal_counter'] = personal_counter

    return render_template(
        'start_page.html',
        visited=visited,
        counter=counterFile.counterINT,
        personal_counter=personal_counter
    )


# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
if __name__ == "__main__":
    # -------------------------------------------------------------------------------
    # adding favicon to application if missing @app.route('/favicon.ico')
    # app.add_url_rule('/favicon.ico', 'favicon', favicon)
    # -------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------
    # app launch
    # with debug enabled, threads are started twice. Test with print("test") in save_counter_to_file()
    # app.run(debug=True)
    app.run()
    # -------------------------------------------------------------------------------
