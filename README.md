docker build -t forwarding-bot .
docker run -it --name forwarding-bot --env-file .env forwarding-bot