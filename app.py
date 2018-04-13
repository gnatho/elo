from flask import Flask, render_template, request
from data import Articles
from flask_sqlalchemy import SQLAlchemy


#teste teess



Articles = Articles()


app = Flask(__name__)
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Owocki(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owocek = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.owocek


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    # colours = ['Red', 'Blue', 'Orange']
    colours = Owocki.query.all()
    return render_template('about.html', colours=colours)


@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)


@app.route("/displayTest", methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    return render_template('empty.html', selects=select)

    # return str(select) # just to see what select is


if __name__ == '__main__':
    app.run(host='0.0.0.0')
