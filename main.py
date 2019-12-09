from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import constants
import init_train





def init_chat_bot():
    bot = ChatBot(
        constants.CHAT_BOT_NAME,
        storage_adapter= constants.STORAGE_ADAPTER,
        logic_adapters=constants.LOGIC_ADAPTERS,
        database_uri=constants.DB_URL
    )
    return bot


def run_bot(bot):
    while True:
        try:
            bot_input = bot.get_response(input())
            print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break


if __name__ == '__main__':
    chatbot = init_chat_bot()
    init_train.train_bot(chatbot)
    run_bot(chatbot)


