FROM python
RUN python -m pip install -r r.txt
RUN mkdir /app
WORKDIR /app

CMD python main.py
