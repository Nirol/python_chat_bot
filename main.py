from chatterbot import ChatBot

from init_train import conversation

if __name__ == '__main__':

    chatbot = ChatBot("Nir ChatBot")

    from chatterbot.trainers import ListTrainer
    trainer = ListTrainer(chatbot)

    trainer.train(conversation)

    response = chatbot.get_response("Good morning!")
    print(response)

