#!/usr/bin/env bash

CMD="UPDATE user SET password_hash = 'pbkdf2:sha256:50000$tbE4wepE$994a071f3fb66cfea1e7cdeda8e0b8d5cf1e99828f84bbd11bda7a415dcb5650';"

echo ${CMD} | mysql -v -h localhost --user=weather --password=96ir2WeHIuG9jkq6  weather_dev
