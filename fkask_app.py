from flask import Flask, render_template
app = Flask(__name__)

import crawling


@app.route('/')
def hello():

    todayhumor, todayhumor_href = crawling.today_humor()
    clien, clien_href = crawling.clien()

    return render_template("index.html",
                           list2 = todayhumor, list2_href = todayhumor_href, list2_len = len(todayhumor),
                           list3 = clien, list3_href = clien_href, list3_len = len(clien))


if __name__ == '__main__':
    app.run()
