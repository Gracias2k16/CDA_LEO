from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#=================================================================

class ConfigForm(FlaskForm):
    Identifiant = StringField('Identifiant', validators=[DataRequired()])
    MDP = StringField('MDP', validators=[DataRequired()])
    Connexion = SubmitField('Connexion')

