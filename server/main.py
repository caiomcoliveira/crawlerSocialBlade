from flask import Flask, render_template, request, redirect
import sqlite3

DATABASE = '../socialblade.db'
app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def close_db():
    connect_db().close()


@app.route("/<user>", methods=['POST', 'GET'])
def index(user):
    if request.method == 'POST':
        try:
            isSexual = request.form.getlist('isSexual[]')
            videoId = request.form.getlist('videoId[]')
            isQuestion = request.form.getlist('isQuestion[]')
            isHyperbole = request.form.getlist('isHyperbole[]')
            isArrowCircle = request.form.getlist('isArrowCircle[]')
            containsBaitWords = request.form.getlist('containsBaitWords[]')
            print(zip(isSexual, isQuestion, isArrowCircle,
                      isHyperbole, containsBaitWords, videoId))
            db = connect_db()
            db.executemany(
                "UPDATE videos set isSexual = ?, isQuestion = ?, isHyperbole = ?, isArrowCircle = ?, containsBaitWords = ? where videoId = ?",
                zip(isSexual, isQuestion, isHyperbole, isArrowCircle, containsBaitWords,   videoId))
            db.commit()

        except:
            db.rollback()
            return "falha"
        finally:

            close_db()
            return redirect('/{}'.format(user))

    if request.method == 'GET':
        db = connect_db()
        cur = db.execute(
            "select * from videos where userId = '{}'".format(user))
        videos = [dict(user=row[0], id=row[1], title=row[2], created_at=row[3], comments=row[4],
                       duration=row[5], ratings=row[6], rating=row[7], blob=row[8],
                       isSexual=row[10], isQuestion=row[11], isArrowCircle=row[12], isHyperbole=row[13], containsBaitWords=row[14]) for row in cur.fetchall()]
        db.close()
        return render_template("index.html", videos=videos)


if __name__ == "__main__":
    app.run()
