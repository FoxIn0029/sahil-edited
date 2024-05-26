FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requiremtns.txt .

RUN pip install -r requiremtns.txt
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
