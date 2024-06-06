from app.app_init import create_app

app = create_app()


@app.route('/')
def home():
    return '<h1>Hello</h1>'


if __name__ == '__main__':
    app.run(debug=True)