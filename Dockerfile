FROM python:3.10

COPY requirements.txt /var/requirements.txt
RUN pip install --no-cache-dir -r /var/requirements.txt
COPY . /opt/buses

WORKDIR /opt/buses/web

CMD sh run.sh

