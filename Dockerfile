FROM python:3.10
COPY main.py requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python3","main.py" ]
