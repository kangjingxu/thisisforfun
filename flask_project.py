from flask import Flask, render_template
app = Flask(__name__)


guns = [
    {
        'name': 'Pump Shotgun',
        'damage': '85',
        'firerate': '0.8',
        'rarity': 'blue'
    },
    {
        'name': 'Assualt Riffle',
        'damage': '32',
        'firerate': '1.2',
        'rarity': 'green'
    }
]


@app.route("/")
def welcome():
    return render_template('welcome.html')


@app.route("/home")
def home():
    return render_template('home.html', guns=guns, title='')


@app.route("/about")
def about():
    return render_template('about.html')


# @app.route("/page2")
# def page2():
#     return "Hello Page Two!"


if __name__ == '__main__':
    app.run(debug=True)  # , host='0.0.0.0')
