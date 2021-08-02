FROM tiangolo/uvicorn-gunicorn:python3.8

RUN mkdir /fastapi

COPY fast_api_requriements.txt /fastapi

WORKDIR /fastapi

RUN pip install -r fast_api_requriements.txt

COPY . /fastapi

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]