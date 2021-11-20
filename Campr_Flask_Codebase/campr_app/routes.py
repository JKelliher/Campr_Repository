from flask import Flask, url_for, render_template, redirect
from campr_app import app, db
from campr_app.forms import camp_site_entry_form, new_user_form, search_form
from campr_app.models import CampSites



@app.route('/')
@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/home/')
def home():
    camp_sites = CampSites.query.all()
    return render_template('home.html', title='Home Page', camp_sites=camp_sites)


@app.route('/new_user/', methods=['GET', 'POST'])
def new_user():
    form = new_user_form()
    if form.validate_on_submit():
        return """
        <h1> Welcome to Campr. </h1>
        <a href="/new_campsite">Click Here to Submit Your First Site!</a>
        """
    return render_template('new_user.html', form=form)



@app.route('/new_campsite/', methods=['GET', 'POST'])
def new_campsite():
    form = camp_site_entry_form()
    if form.validate_on_submit():
        print('validate started')
        campsite = CampSites(Site_Name=form.site_name.data, GPS=form.gps_coordinates.data, City=form.city.data, State=form.state.data, Date=form.date_of_visit.data, Rating=form.rating.data, Type=form.type_of_campsite.data, Restrooms=form.restrooms.data, Fees=form.fees.data, Notes=form.notes.data, Image=form.upload_photo.data)
        db.session.add(campsite)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_campsite.html', form=form)



@app.route('/search/', methods=['GET', 'POST'])
def search():
    form = search_form()
    if form.validate_on_submit():
        return '<h2> Successful campsite search with coordinates: {}.</h2>'.format(form.given_gps_coordinates.data)
    return render_template('search.html', form=form)



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

@app.route('/about/')
def about():
    return render_template('about.html')