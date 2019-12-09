CHAT_BOT_NAME = "Nir ChatBot"
DATABASE_NAME = "chatbotdb"
DB_URL = 'sqlite:///' + DATABASE_NAME +'.sqlite3'


STORAGE_ADAPTER = 'chatterbot.storage.SQLStorageAdapter'


LOGIC_ADAPTERS = ['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.TimeLogicAdapter']