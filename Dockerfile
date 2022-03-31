FROM python:3.9.2-slim-buster
RUN mkdir /app && chmod 777 /app
COPY bashrc /root/.bashrc
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
RUN apt -qq update && apt -qq install -y git python3 python3-pip ffmpeg
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["bash","convertor.sh"]
