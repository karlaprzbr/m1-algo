from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name=name)

@app.route('/books')
def books():
    with open('F:/GitHub/m1-python/2020-11-19 app flask/app/books.json') as f:
        return render_template('books.html', books=json.load(f))

@app.route('/books/<isbn>')
def book_by_isbn(isbn = None):
    with open('F:/GitHub/m1-python/2020-11-19 app flask/app/books.json') as f:
        return render_template('books.html', books=json.load(f), isbn=isbn)

@app.route('/books/<title>')
def book_by_title(title = None):
    with open('F:/GitHub/m1-python/2020-11-19 app flask/app/books.json') as f:
        return render_template('books.html', books=json.load(f), title=title)

if __name__ == "__main__":
    app.run(debug=True)