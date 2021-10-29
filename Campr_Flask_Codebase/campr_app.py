from flask import Flask, url_for, render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

camp_sites = [
    {
        'site_name': 'Peaceful Valley',
        'gps': '40.13196, -105.50705',
        'city': 'Allenspark',
        'state_abr': 'CO',
        'date': '5/15/20',
        'rating': 4,
        'notes': 'Nice site, could hear street noise from peak to peak highway though'
    },
    {
        'site_name': 'Meeker Park',
        'gps': '40.24075, -105.53691',
        'city': 'Allenspark',
        'state_abr': 'CO',
        'date': '9/17/19',
        'rating': 5,
        'notes': 'Close to Longs Peak but otherwise not an exciting site'
    }
]

@app.route('/')
@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/home/')
def home():
    return render_template('home.html', title='Home Page', camp_sites=camp_sites)

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

@app.route('/retrieve_login/')
def retrieve_login():
    return render_template('retrieve_login.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)
