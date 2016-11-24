from flask import render_template

from app.h5 import h5


@h5.route('/preview', methods=['GET'])
def preview():
    return render_template('h5/preview.html')
