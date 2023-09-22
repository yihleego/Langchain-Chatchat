docker stop chatchat
docker rm   chatchat
docker rmi  chatchat

docker build -t chatchat .
docker run -d -itd -p 8501:8501 --name=chatchat chatchat