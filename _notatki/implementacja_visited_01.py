from flask import Flask, session, render_template
from flask_session import Session

app = Flask(__name__)

# Konfiguracja sesji
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = 3

Session(app)

counter = 0


@app.route("/")
def start_page():
    global counter, visited
    visited = True
    print(session)

    if 'visited' not in session:
        session['visited'] = True
        visited = False
        counter += 1

    return render_template('start_page.html', visited=visited, counter=counter)


if __name__ == "__main__":
    app.run(debug=True)
