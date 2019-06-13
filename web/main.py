# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return '<h2>Homepage</h2>'

# @app.route("/profile/<name>")
# def profile(name):
#     return render_template("profile.html", name=name)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my_form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = ""
    for i, c in enumerate(text):
        if i % 2 == 0:
            processed_text += c.upper()
        else:
            processed_text += c

    return processed_text


if __name__ == "__main__":
    app.run(debug=True)