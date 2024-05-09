from flask import Flask, redirect, url_for, render_template
from markupsafe import escape

app = Flask(__name__)
app.counter = 0

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Hellohello", name="Rita")

@app.route("/articles")
def articles():
    posts = [
        {
            'author': {'nickname': 'John'},
            'title': 'Inception is mind-bending!',
            'body': 'Thought-provoking narrative about dreams!'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'The Shawshank Redemption is a masterpiece!',
            'body': 'Deep exploration of hope and friendship in prison!'
        },
        {
            'author': {'nickname': 'Michael'},
            'title': 'The Godfather is a timeless classic!',
            'body': 'Gripping tale of power, family, and loyalty!'
        },
        {
            'author': {'nickname': 'Emily'},
            'title': 'Interstellar takes you on a cosmic journey!',
            'body': 'Astounding visuals and a profound story about love and time!'
        },
        {
            'author': {'nickname': 'Alex'},
            'title': 'Fight Club challenges your perception!',
            'body': 'Raw and gritty exploration of identity and consumerism!'
        }
    ]

    return render_template("articles.html", title="Awesome Blog", articles=posts)


@app.route('/<name>')
def welcome(name):
    return f"Hello, {escape(name)}!"

@app.route('/anonim')
def anonim():
    return redirect(url_for("welcome", name="Guest"))

@app.route('/counter')
def counter():
    app.counter +=1
    return app.counter

if __name__ == '__main__':
    app.run(debug=True)