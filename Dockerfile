FROM debian:bullseye-slim

RUN apt-get update
RUN apt-get install apache2 python3 python3-pip libmariadb-dev \
    libapache2-mod-wsgi-py3 python-dev openssh-client \
    python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 \
    libjpeg-dev libopenjp2-7-dev libffi-dev -y

# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf  /etc/l/usr/share/zoneinfo/$TZocaltime && echo $TZ > /etc/timezone

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
# COPY ./seguimiento.conf /etc/apache2/sites-available/

# RUN adduser --disabled-password user

# RUN touch /app/log
# RUN touch /app/err_log
# RUN chown www-data:www-data /app/log
# RUN chown www-data:www-data /app/err_log

# RUN a2ensite seguimiento.conf


RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

EXPOSE 80

CMD [ "apachectl", "-DFOREGROUND" ]

# USER user


