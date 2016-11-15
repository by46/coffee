import hashlib
import mimetypes
import os.path

from flask import Blueprint
from flask import current_app as app
from flask import render_template
from flask_wtf import Form
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename


class ImageForm(Form):
    picture = FileField('UploadFile')


upload_blueprint = Blueprint('_uploader', __name__, template_folder=os.path.join(__file__, '../..', 'templates'),
                             url_prefix='/_uploader')


@upload_blueprint.route('/upload', methods=('GET', 'POST'))
def upload_file():
    form = ImageForm()
    if form.validate_on_submit():
        uploader = app.upload
        storage = form.picture.data
        filename = secure_filename(form.picture.data.filename)
        __, ext = os.path.splitext(filename)
        mime, __ = mimetypes.guess_type(filename)
        mime = mime or 'html/plain'
        content = storage.read()
        key = '{0}{1}'.format(hashlib.sha256(content).hexdigest(), ext)
        picture_url, file_hash = uploader.upload(key, content, mime)
        return render_template('upload_result.html', picture_url=picture_url, file_hash=file_hash)

    else:
        return render_template('upload.html', form=form)
