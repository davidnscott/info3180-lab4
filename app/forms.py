from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
	pic = FileField('Picture',validators = [FileRequired(),FileAllowed(['jpg','png'],'imagesonly')])
	