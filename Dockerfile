FROM python:3.8

ADD internet_speed_test.py .

RUN pip install speedtest-cli

CMD ["python", "./internet_speed_test.py"]