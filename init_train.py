from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

conversation1 = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]


conversation2 = [
    "Hi there!",
    "Hello",
]
conversation3 = [
    "Greetings!",
    "Hello",
]

def list_train(chat_bot):

    trainer = ListTrainer(chat_bot)
    trainer.train(conversation1)
    trainer.train(conversation2)
    trainer.train(conversation3)


def corpus_train(chat_bot):
    trainer = ChatterBotCorpusTrainer(chat_bot)
    trainer.train(
        "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations"
    )


def train_bot(chat_bot):
    list_train(chat_bot)
    corpus_train(chat_bot)





