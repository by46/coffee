# PRD environment setting

# Flask-NegLog Settings
LOG_LEVEL = 'debug'
LOG_FILENAME = "logs/application.error.log"
LOG_ENABLE_CONSOLE = False

# SQL-Alchemy settings
SQLALCHEMY_DATABASE_URI = "mysql://root:root@10.16.76.245/coffee"
SQLALCHEMY_ECHO = True

# Flask-Upload settings
UPLOAD_URL_PREFIX = '/coffee/_uploader'
UPLOAD_QINIU_ACCESS_KEY = 'IJQd3tLTbv8CRAzew4R1JHpWAW5cKcDBgJX01MAi'
UPLOAD_QINIU_SECRET_KEY = 'bVBnQx445tH2OAIbiWLKN7fYl1SRSm7hR95OQr3a'
UPLOAD_QINIU_BUCKET = 'testing'
UPLOAD_QINIU_CDN = 'http://7xjoeo.com1.z0.glb.clouddn.com.backss'
