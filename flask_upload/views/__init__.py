import hashlib
import httplib
import mimetypes
import os.path

import requests
from flask import Blueprint
from flask import render_template
from flask_wtf import Form
from flask_wtf.file import FileField
from qiniu import Auth
from qiniu import put_data
from werkzeug.utils import secure_filename


class ImageForm(Form):
    picture = FileField('UploadFile')


upload_blueprint = Blueprint('_uploader', __name__, template_folder=os.path.join(__file__, '../..', 'templates'),
                             url_prefix='/_uploader')


@upload_blueprint.route('/upload', methods=('GET', 'POST'))
def upload_file():
    form = ImageForm()
    if form.validate_on_submit():
        filename = secure_filename(form.picture.data.filename)
        with open('uploads/' + filename, 'wb') as writer:
            # while True:
            data = form.picture.data.read(12)
            writer.write(data)

        # form.picture.data.save('uploads/' + filename)
        picture_url = None
        file_hash = 'file hash'
        return render_template('upload_result.html', picture_url=picture_url, file_hash=file_hash)

    else:
        return render_template('upload.html', form=form)


def handle_uploaded_file2(key, data, mime_type):
    url = self.make_url(key)
    response = requests.head(url)
    if response.status_code == httplib.OK:
        return response.headers.get('etag').strip("\"")
    q = Auth(self._access_key, self._secret_key)
    token = q.upload_token(self._bucket_name, key, 3600)
    ret, response = put_data(token, key, data, mime_type=mime_type)
    if response.status_code == httplib.OK:
        return ret.get('hash')
    return None


def handle_uploaded_file(entity):
    __, ext = os.path.splitext(entity.name)
    mime, __ = mimetypes.guess_type(entity.name)
    mime = mime or 'html/plain'
    content = entity.read()
    key = '{0}{1}'.format(hashlib.sha256(content).hexdigest(), ext)
    file_hash = client.upload(key, content, mime)
    if file_hash:
        return client.make_url(key), file_hash
    else:
        return None, None
