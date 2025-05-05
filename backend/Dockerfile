
FROM python:3.9

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt uvicorn

COPY . /backend

CMD ["uvicorn", "app:main"]