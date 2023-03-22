from flask import Flask

app = Flask(__name__)
print(__name__)


@app.route("/")
def guess_number():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media2.giphy.com/media/l378khQxt68syiWJy/giphy.gif?cid=ecf05e47spuqnyvvbavzaibzmxs7qd54ueaol2kgpn4z6ats&rid=giphy.gif&ct=g'>"


if __name__ == "__main__":
    app.run(debug=True)