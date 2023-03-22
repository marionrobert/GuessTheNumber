from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 10)
print(random_number)

@app.route("/")
def guess_number():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media2.giphy.com/media/l378khQxt68syiWJy/giphy.gif?cid=ecf05e47spuqnyvvbavzaibzmxs7qd54ueaol2kgpn4z6ats&rid=giphy.gif&ct=g'>"


@app.route("/<int:number>")
def result(number):
    if number == random_number:
        return f"<h1 style='color:green'>Congratulations, the number was: {number}</h1>" \
               f"<img src='https://media4.giphy.com/media/xT8qBepJQzUjXpeWU8/200w.webp?cid=ecf05e478z6zj4t30rdc5zqenx95jmtfz4v09mj659dyutz7&rid=200w.webp&ct=g'>"
    elif number > random_number:
        return "<h1 style='color:red'>Too high, try again!</h1>" \
               "<img src='https://media3.giphy.com/media/L379T6X2fMlsEB8WEb/200w.webp?cid=ecf05e47hg2zd041wo7yizw6mtc0h7hxidbe7o5r83tyj58b&rid=200w.webp&ct=g'>"
    else:
        return "<h1 style='color:red'>Too low, try again!</h1>" \
               "<img src='https://media0.giphy.com/media/l09YFmpE61GC0PcoG5/giphy.webp?cid=ecf05e47hg2zd041wo7yizw6mtc0h7hxidbe7o5r83tyj58b&rid=giphy.webp&ct=g'>"


if __name__ == "__main__":
    app.run(debug=True)