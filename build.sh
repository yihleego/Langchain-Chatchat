docker stop chatchat
docker rm   chatchat
docker rmi  chatchat

docker build -t chatchat .
docker run -d -itd -p 7861:7861 -p 8501:8501 -p 8888:8888 --name=chatchat chatchat