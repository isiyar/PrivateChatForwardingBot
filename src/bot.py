from config import (
    API_ID,
    API_HASH,
    TARGET_CHAT_ID,
    SOURCE_CHAT_ID,
    SOURCE_TO_TARGET_TOPICS,
)
from telethon import TelegramClient, events


client = TelegramClient("seesion_name", API_ID, API_HASH)


async def send_message_to_target_chat(message, topic_id):
    await client.send_message(entity=TARGET_CHAT_ID, message=message, reply_to=topic_id)


@client.on(
    events.NewMessage(
        chats=SOURCE_CHAT_ID,
        func=lambda e: e.is_group and str(e.reply_to_msg_id) in SOURCE_TO_TARGET_TOPICS,
    )
)
async def handle_message(event):
    await send_message_to_target_chat(
        event.message, SOURCE_TO_TARGET_TOPICS[str(event.reply_to_msg_id)]
    )


async def main():
    await client.start()
    print("Start...")
    await client.run_until_disconnected()


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
