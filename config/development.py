# Local development environment setting
DEBUG = True

# SQL-Alchemy settings
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@10.16.76.245:3306/coffee"
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/coffee"
SQLALCHEMY_ECHO = True
SQLALCHEMY_BINDS = {
    'coffee01': "mysql+pymysql://root:root@10.16.76.245:3306/coffee",
    'coffee02': "mysql+pymysql://root:root@10.16.76.245:3306/coffee"
}

# Flask-Upload settings
UPLOAD_URL_PREFIX = '/coffee/_uploader'
UPLOAD_QINIU_ACCESS_KEY = 'IJQd3tLTbv8CRAzew4R1JHpWAW5cKcDBgJX01MAi'
UPLOAD_QINIU_SECRET_KEY = 'bVBnQx445tH2OAIbiWLKN7fYl1SRSm7hR95OQr3a'
UPLOAD_QINIU_BUCKET = 'testing'
UPLOAD_QINIU_CDN = 'http://7xjoeo.com1.z0.glb.clouddn.com.backss'

# Flask-JWT
JWT_AUTH_URL_RULE = '/coffee/auth'
