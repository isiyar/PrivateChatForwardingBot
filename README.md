# PrivateChatForwardingBot
Бот позволяет пересылать сообщения из Telegram-каналов и чатов(в том числе из веток)

## Запуск
1. Сборка контейнера<br>
```docker build -t forwarding-bot .```
2. Запуск контейнера<br>
```docker run -it --name forwarding-bot --env-file .env forwarding-bot```
