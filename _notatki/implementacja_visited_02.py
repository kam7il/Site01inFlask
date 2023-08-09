from flask import Flask, session, render_template, after_this_request
from flask_session import Session

app = Flask(__name__)

# Konfiguracja sesji
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = 10

Session(app)

counter = 0


@app.route("/")
def start_page():
    global counter
    if 'visited' not in session:
        session['visited'] = False
        counter += 1

    @after_this_request
    def set_visited(response):
        session['visited'] = True
        return response

    return render_template('start_page.html', visited=session.get('visited'), counter=counter)


if __name__ == "__main__":
    app.run(debug=True)
