from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SelectField, FloatField, SubmitField, TimeField
from wtforms.validators import DataRequired, Length, NumberRange

class MovimientosForm(FlaskForm):
    fecha = DateField("Fecha", validators=[DataRequired(message="Falta la fecha")])
    hora = TimeField("Hora", validators=[DataRequired()])
    concepto = StringField("Concepto", validators=[DataRequired(), Length(min=5)])
    es_ingreso = SelectField("Tipo", validators=[DataRequired()],
                                     choices=[(0, 'Gasto'), (1,'Ingreso')])
    cantidad = FloatField("Cantidad", validators=[DataRequired(), 
                           NumberRange(message="Debe ser una cantidad positiva", min=0.01) ])

    aceptar = SubmitField("Aceptar")