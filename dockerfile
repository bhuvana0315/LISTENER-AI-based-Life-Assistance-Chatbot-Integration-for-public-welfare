FROM python:3.11
WORKDIR /code
COPY . /code
RUN pip install -r /code/requirements.txt
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]

