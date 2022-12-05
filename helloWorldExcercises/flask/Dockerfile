FROM python:3.9

ENV FLASK_APP=app.py

WORKDIR /usr/app/

COPY . /usr/app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# CMD ["python3", "-m", "flask", "--app", "app", "run", "--host='0.0.0.0'", "--port=81"]
CMD ["python3", "app.py"]
