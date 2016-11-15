from flask import render_template
from flask_restful import Resource
from flask_wtf import Form
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename

from app.main import api


@api.resource('/api/v1/version')
class Version(Resource):
    def get(self):
        return dict(version='0.0.1')


class PhotoForm(Form):
    file = FileField("Your photo")


def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/' + filename)
    else:
        filename = None

    return render_template('main/upload.html', form=form, filename=filename)
