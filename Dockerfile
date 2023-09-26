FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -U pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r requirements.txt

EXPOSE 7861
EXPOSE 8501
EXPOSE 8888

CMD ["python", "startup.py", "-a"]
