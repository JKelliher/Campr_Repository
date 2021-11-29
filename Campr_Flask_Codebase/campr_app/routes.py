import os
from flask import Flask, url_for, render_template, redirect, flash, request
from campr_app import app, db, CampsiteDB
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
        user_image = form.upload_photo.data
        path = os.path.join('campr_app/static/upload_images', user_image.filename)
        user_image.save(path)
        campsite = CampSites(Site_Name=form.site_name.data, GPS=form.gps_coordinates.data, City=form.city.data, State=form.state.data, Date=form.date_of_visit.data, Rating=form.rating.data, Type=form.type_of_campsite.data, Restrooms=form.restrooms.data, Fees=form.fees.data, Notes=form.notes.data, Image=user_image.filename)
        db.session.add(campsite)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('new_campsite.html', form=form, legend='New Post')



@app.route('/search/', methods=['GET', 'POST'])
def search():
    form = search_form()
    if form.validate_on_submit():
        search_gps_coordinates = form.given_gps_coordinates.data
        gps_result_id = CampsiteDB.nearby('campr_app/CampTableDB.db', search_gps_coordinates)
        result = CampSites.query.filter(CampSites.idCamp == gps_result_id).all()
        return render_template('search_result.html', camp_sites=result)
    return render_template('search.html', form=form)



@app.route('/search_result/')
def search_result():
    return render_template('search_result.html')


@app.route('/profile/')
def profile():
    return render_template('profile.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = new_user_form()
    if form.validate_on_submit():
        return """
        <h1> Welcome to Campr. </h1>
        <a href="/new_campsite">Click Here to Submit Your First Site!</a>
        """
    return render_template('new_user.html', form=form)


@app.route('/edit_profile/')
def edit_profile():
    return render_template('edit_profile.html')


@app.route('/retrieve_login/')
def retrieve_login():
    return render_template('retrieve_login.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/campsite/<int:idcamp>', methods=['GET'])
def campsite(idcamp):
    campsite = CampSites.query.get_or_404(idcamp)
    return render_template('campsite.html', title=campsite.Site_Name, campsite=campsite)

@app.route('/campsite/<int:idcamp>/update', methods=['GET', 'POST'])
def update_campsite(idcamp):
    campsite = CampSites.query.get_or_404(idcamp)
    form = camp_site_entry_form()
    if form.validate_on_submit():
        campsite.Site_Name = form.site_name.data
        campsite.GPS = form.gps_coordinates.data
        campsite.City = form.city.data
        campsite.State = form.state.data
        campsite.Date = form.date_of_visit.data
        campsite.Rating = form.rating.data
        campsite.Type = form.type_of_campsite.data
        campsite.Restrooms = form.restrooms.data
        campsite.Fees = form.fees.data
        campsite.Notes = form.notes.data
        campsite.Image = form.notes.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('campsite', idcamp=campsite.idCamp))
    elif request.method == 'GET':
        form.site_name.data = campsite.Site_Name 
        form.gps_coordinates.data = campsite.GPS
        form.city.data = campsite.City
        form.state.data = campsite.State 
        form.date_of_visit.data = campsite.Date
        form.rating.data = campsite.Rating 
        form.type_of_campsite.data = campsite.Type
        form.restrooms.data = campsite.Restrooms
        form.fees.data = campsite.Fees
        form.notes.data = campsite.Notes
        form.upload_photo.data = campsite.Image
    return render_template('new_campsite.html', title='Update Post', form=form, legend='Update Post')


@app.route('/campsite/<int:camp_id>/delete', methods=['POST'])
def delete_campsite(camp_id):
    campsite = CampSites.query.get_or_404(camp_id)
    db.session.delete(campsite)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))