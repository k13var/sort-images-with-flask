from wtforms import Form, FloatField, RadioField, validators
from math import pi

class InputForm(Form):
    n_clusters = FloatField(
        label='number of clusters', default=2,
        validators=[validators.InputRequired()])
    
    model = RadioField(
        label='classification model', choices=[
            ('option1','Simple k-means'),
            ('option2','With transfer learning')])
