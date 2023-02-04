# adapted from https://medium.com/fintechexplained/flask-host-your-python-machine-learning-model-on-web-b598151886d

from flask import Flask, render_template, request
app = Flask('movie_recommender')
from models import get_model

@app.route('/')
def show_movie_recommender_form():
    return render_template('movie_form.html')

@app.route('/results', methods=['POST'])
def results():
    form = request.form
    if request.method == 'POST':
        model = get_model()
        movie_title = request.form['title']
        recommended_movie = model.predict(movie_title)
        return render_template('resultsform.html', title = movie_title,   predicted_movies=recommended_movie)
