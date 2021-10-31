from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length

class camp_site_entry_form(FlaskForm):
	site_name = StringField('Site Name:', 
		validators =[DataRequired(), Length(min=2, max=50)], 
		render_kw={"placeholder":"Enter Site Name"})

	city = StringField('City:', 
		validators =[DataRequired(), Length(min=2, max=50)],
		render_kw={"placeholder":"Enter City Name"})

	states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN',
			  'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV',
			  'NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN',
			  'TX','UT','VT','VA','WA','WV','WI','WY']

	state = SelectField('State:', choices=states, validators =[DataRequired(), Length(min=2, max=2)])

	gps_coordinates = StringField('GPS Coordinates:', 
		validators =[DataRequired(), Length(min=2, max=50)],
		render_kw={"placeholder":"Enter GPS Coordinates"})

	date_of_visit = StringField('Date Of Visit:', validators =[DataRequired(), Length(min=2, max=50)],
		render_kw={"placeholder":"MM-DD-YY"})

	ratings = [5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0]
	
	rating = SelectField('Rating:', choices=ratings, validators =[DataRequired(), Length(min=3, max=3)])

	fees = RadioField('Fees:', choices = ['Yes', 'No'], validators =[DataRequired(), Length(min=2, max=3)])

	notes = TextAreaField('Notes:', 
		validators =[DataRequired(), Length(min=2, max=3)],
		render_kw={"placeholder":"Enter notes about campsite"})

	submit = SubmitField('Submit')