FROM python:3.6-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=captains_log

# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]