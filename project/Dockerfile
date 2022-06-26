FROM python:3.7
EXPOSE 5000


# RUN conda install opencv


CMD ["python3", "--version"]
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install opencv-python
RUN pip3 install py-find-1st
COPY ./webapp .

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install Pillow

CMD python3 manage.py runserver 0.0.0.0:1337 --noreload
