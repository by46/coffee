from sqlalchemy import and_
from sqlalchemy import orm
from sqlalchemy import schema
from sqlalchemy import types
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@10.16.76.245/coffee')

metadata = schema.MetaData(bind=engine, reflect=False)

# metadata.reflect()
# print metadata.tables

mountain_table = schema.Table('mountain', metadata,
                              schema.Column('id', types.Integer, primary_key=True),
                              schema.Column('name', types.String(30), nullable=False),
                              schema.Column('altitude', types.DECIMAL(11, 2), nullable=False))

mountain_album_table = schema.Table('mountain_album', metadata,
                                    schema.Column('id', types.Integer, primary_key=True),
                                    schema.Column('title', types.String(30), nullable=False),
                                    schema.Column('url', types.String(300), nullable=False),
                                    schema.Column('mountain_id', types.Integer, schema.ForeignKey('mountain.id')))

article_table = schema.Table('article', metadata,
                             schema.Column('id', types.Integer, primary_key=True),
                             schema.Column('title', types.String(30), nullable=False),
                             schema.Column('content', types.Text))
tag_table = schema.Table('tag', metadata,
                         schema.Column('id', types.Integer, primary_key=True),
                         schema.Column('name', types.String(30)))

article_tag_table = schema.Table('article_tag', metadata,
                                 schema.Column('article_id', schema.ForeignKey('article.id')),
                                 schema.Column('tag_id', schema.ForeignKey('tag.id')))


# if not person.exists():
#     person.create()


# metadata.create_all()


class Mountain(object):
    def __init__(self, name, weight, altitude):
        self.name = name
        self.weight = weight
        self.altitude = altitude

    def __repr__(self):
        return "<Person>"


class MountainAlbum(object):
    def __init__(self, title, url, mountain_id):
        self.title = title
        self.url = url
        self.mountain_id = mountain_id

    def __repr__(self):
        return '<MountainAlbum>'


class Article(object): pass


# def __init__(self, title, content):
#     self.title = title
#     self.content


class Tag(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<tag {name}>'.format(name=self.name)


orm.mapper(Mountain, local_table=mountain_table,
           properties={'photos': orm.relation(MountainAlbum, backref='mountain')})

orm.mapper(MountainAlbum, local_table=mountain_album_table)

orm.mapper(Tag, tag_table)
orm.mapper(Article, article_table,
           properties={'tags': orm.relation(Tag, secondary=article_tag_table, backref='articles')})

Base = declarative_base()
from sqlalchemy import Column


class Cookie(Base):
    __tablename__ = 'cookies'
    cookie_id = Column(types.Integer(), primary_key=True)
    cookie_name = Column(types.String(50), index=True)
    cookie_sku = Column(types.String(55))
    quantity = Column(types.Integer())
    unit_cost = Column(types.Numeric(12, 2))


Session = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False, expire_on_commit=True)

session = Session()

print session.query(Tag).all(), session.query(Tag).count()
print session.query(Tag).filter(Tag.id > 1).all()
print session.query(Tag).filter(Tag.name.like('%ts')).all()
print session.query(Tag).filter(Tag.name.in_(['sports'])).all()
print session.query(Tag).filter(~Tag.name.in_(['sports'])).all()
print session.query(Tag).filter(and_(Tag.id > 1, Tag.name.like('%s'))).all()
print session.query(Tag).filter_by(name='sports').all()
print session.query(Tag).get(1), session.query(Tag).get('1')
print session.query(Tag).order_by(Tag.name).all()
print session.query(Tag, Tag.id, Tag.name).first()
print session.query(Article).all()
article = Article()
article.title = 'hello'
article.content = 'demo'
session.add(article)
session.flush()

print session.query(Article).all()
article = session.query(Article).get(2)
article.content = 'Parts'
session.add(article)
session.flush()
print article.content
session.commit()
