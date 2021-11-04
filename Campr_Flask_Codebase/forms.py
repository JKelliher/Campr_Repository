from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired, InputRequired, Length, Regexp

class camp_site_entry_form(FlaskForm):
	site_name = StringField('Site Name:', 
		validators =[InputRequired(), Length(min=2, max=50)], 
		render_kw={"placeholder":"Enter Site Name"})

	city = StringField('City:', 
		validators =[InputRequired(), Length(min=2, max=50)],
		render_kw={"placeholder":"Enter City Name"})

	states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN',
			  'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV',
			  'NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN',
			  'TX','UT','VT','VA','WA','WV','WI','WY']
	state = SelectField('State:', choices=states, validators =[InputRequired()])

	gps_coordinates = StringField('GPS Coordinates:', 
		validators =[Regexp('((?:[\+-]?[0-9]*[\.,][0-9]+)|(?:[\+-]?[0-9]+))', message="Please enter GPS Coordinates in format: dd,dddd, dd,dddd")],
		render_kw={"placeholder":"Enter GPS Coordinates format: dd,dddd, dd,dddd"})

	date_of_visit = StringField('Date Of Visit:', 
		validators =[Regexp('(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.][0-9][0-9]$', message="Please Provide Date in mm/dd/yy format.")],
		render_kw={"placeholder":"MM/DD/YY"})

	type_of_campsite = StringField('Type of Campsite:', validators =[InputRequired(), Length(min=2, max=50)],
		render_kw={"placeholder":"Enter Campsite Type"})

	restrooms = RadioField('Restrooms:', choices = ['Yes', 'No'], validators =[InputRequired(), Length(min=2, max=3)])

	ratings = [5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0]
	rating = SelectField('Rating:', choices=ratings, validators =[InputRequired(), Length(min=3, max=3)])

	fees = RadioField('Fees:', choices = ['Yes', 'No'], validators =[InputRequired(), Length(min=2, max=3)])

	notes = TextAreaField('Notes:', 
		validators =[],
		render_kw={"placeholder":"Enter notes about campsite"})

	submit = SubmitField('Submit')

	upload_photo = FileField('Image:', validators=[FileAllowed(['jpg', 'png'], 'Only .jpg and .png are allowed.')])