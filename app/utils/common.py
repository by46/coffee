from flask import current_app

from app import db


def select_bind(db_name='coffee01'):
    return db.get_engine(current_app, bind=db_name)
