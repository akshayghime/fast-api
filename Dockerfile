# Use the official Python image as the base image
FROM python:3.12-rc-slim-buster
RUN mkdir -p /app
COPY . main.py /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]