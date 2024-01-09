FROM python:3.9-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY run_app.py ./

COPY test_run_app.py ./

CMD [ "python", "./run_app.py" ]







