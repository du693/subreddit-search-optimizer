from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3
from scrape import *

app= Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('subreddits.sqlite')
    return conn

@app.route('/')
def index():
    return render_template('index.html')

#add loading bar?
@app.route('/loading', methods=['GET','POST'])
def loading():
    if request.method == 'POST':
        results = request.form.getlist('job_search')
        URL=get_subreddit(input_stream(str(results)))
        return redirect(URL)


if __name__ == '__main__':
    app.run(host="localhost", debug=True)