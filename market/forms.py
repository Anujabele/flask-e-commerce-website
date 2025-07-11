from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, DecimalField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check): #to check if user already exist
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username already exist! Please try a diffrent Username")
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError("Email Address already exist ! Please try another email address")


    username = StringField(label='User Name:', validators=[Length(min=2,max=30), DataRequired()])
    email_address = StringField(label='Email Address:',validators=[Email(),DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellingItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')

class AddItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired(), Length(min=2, max=30)])
    price = DecimalField('Price ($)', validators=[DataRequired()])
    barcode = StringField('Barcode', validators=[DataRequired(), Length(min=5)])
    description = StringField('Description', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField('Add Item')  

