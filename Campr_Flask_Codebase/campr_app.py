from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/login/')
def index():
    return render_template('login.html')

@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/new_user/')
def new_user():
    return render_template('new_user.html')

@app.route('/new_campsite/')
def new_campsite():
    return render_template('new_campsite.html')

@app.route('/search/')
def search():
    return render_template('search.html')

@app.route('/search_result/')
def search_result():
    return render_template('search_result.html')

@app.route('/profile/')
def profile():
    return render_template('profile.html')

@app.route('/edit_profile/')
def edit_profile():
    return render_template('edit_profile.html')


if __name__ == '__main__':
    app.run(debug=True)
