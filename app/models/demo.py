from app import db


class Demo(db.Model):
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = db.Column(db.Integer, primary_key=True)


from sqlalchemy.event import listens_for
from sqlalchemy import desc

idx_name = db.Index('idx_demo3_name', 'name desc')


@listens_for(idx_name, 'before_parent_attach')
def receive_before_parent_attach(target, parent):
    if target.expressions:
        tmp = []
        pending_col_args = []
        for expression in target.expressions:
            if ' ' in expression:
                name, direction = expression.split(' ')
                pending_col_args.append(name)
                direction = direction.lower()
                if direction == 'desc':
                    name = desc(parent.columns.get(name))
                tmp.append(name)
            else:
                tmp.append(expression)
                pending_col_args.append(name)

        target.expressions = tuple(tmp)
        target._pending_colargs = pending_col_args


class Demo3(db.Model):
    __table_args__ = (idx_name, {'mysql_engine': 'InnoDB'})
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))


idx_name2 = db.Index('idx_demo5_name', 'name desc')


@listens_for(idx_name2, 'before_parent_attach')
def receive_before_parent_attach(target, parent):
    if target.expressions:
        tmp = []
        pending_col_args = []
        for expression in target.expressions:
            if ' ' in expression:
                name, direction = expression.split(' ')
                pending_col_args.append(name)
                direction = direction.lower()
                if direction == 'desc':
                    name = desc(parent.columns.get(name))
                tmp.append(name)
            else:
                tmp.append(expression)
                pending_col_args.append(name)

        target.expressions = tuple(tmp)
        target._pending_colargs = pending_col_args


class Demo5(db.Model):
    __table_args__ = (db.Index('idx_demo5_name_2', 'name'),idx_name2, {'mysql_engine': 'InnoDB'})
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
