from flask import render_template

from app.h5 import h5


@h5.route('/preview2/<stock_or_code>', methods=['GET'])
@h5.route('/preview/<stock_or_code>', methods=['GET'])
def preview(stock_or_code):
    print(stock_or_code)
    return render_template('h5/preview.html')
