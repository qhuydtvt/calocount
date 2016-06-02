from flask import Flask, render_template

app = Flask(__name__)

class Movie:
    def __init__(self, title, img):
        self.title = title
        self.img = img
movie1 = Movie('The girl next door', "http://ecx.images-amazon.com/images/I/51izKX%2BywRL._SY300_.jpg")
movie2 = Movie('Kungfu Panda',
               'http://vignette2.wikia.nocookie.net/kungfupanda/images/3/39/Bao.jpg/revision/latest?cb=20150617161134')
m_list = [
    movie1,
    movie2,
    Movie('500 days of summer',
          "https://images-na.ssl-images-amazon.com/images/G/01/dvd/fox/500_days_of_summer/500_1L.jpg")
]

@app.route('/')
def hello_world():
    return 'Hello Giang!'

@app.route('/c4e')
def hello_c4e():
    return 'Hello C4E!'

@app.route('/c4e-1')
def hello_team1():
    return 'Hello Hoang + Hoang'

@app.route('/<name>')
def hello(name):
    return('Hello' + name)

@app.route('/movie')
def get_movie():
    return render_template('movie.html')

@app.route('/movie2')
def get_movie2():
    return render_template(
        'movie_2.html',
        title = 'civil war',
        img = 'http://media.comicbook.com/2016/04/civil-war-cap-tony-179110.jpg')


@app.route('/movies')
def movies():

    return render_template('movies.html', movie_list = m_list)

if __name__ == '__main__':
    app.run()
