FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir /fastapi

COPY fast_api_requriements.txt /fastapi

WORKDIR /fastapi

RUN pip install -r fast_api_requriements.txt

COPY . /fastapi

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]