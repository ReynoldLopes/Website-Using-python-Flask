from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,length,EqualTo,Email
from wtforms.fields.html5 import EmailField


class Regristrationform(FlaskForm):
    username=StringField("username",validators=[DataRequired(),length(min=2,max=20)])
    Email=EmailField("Email",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    confirm_password=PasswordField("confirmpassword",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField("Submit")
class login(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    rememberme = BooleanField("remember me")
    submit = SubmitField("Login")


