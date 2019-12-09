from chatterbot.response_selection import get_most_frequent_response

CHAT_BOT_NAME = "Nir ChatBot"
DATABASE_NAME = "chatbotdb"
DB_URL = 'sqlite:///' + DATABASE_NAME +'.sqlite3'


STORAGE_ADAPTER = 'chatterbot.storage.SQLStorageAdapter'


LOGIC_ADAPTERS = ['chatterbot.logic.MathematicalEvaluation',
                  {
                      'import_path': 'chatterbot.logic.BestMatch',
                      'default_response': 'I am sorry, but I do not understand.',
                      'maximum_similarity_threshold': 0.90
                  },
                  {
                      'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                      'input_text': 'What is your name?',
                      'output_text': 'My Name is Nir Chat Bot!'
                  }
                  ]

PREPROCESSORS=[
        'chatterbot.preprocessors.clean_whitespace',
            'chatterbot.preprocessors.unescape_html',
            'chatterbot.preprocessors.convert_to_ascii'
    ]

from chatterbot import filters
FILTERS = [filters.get_recent_repeated_responses]

from chatterbot.comparisons import levenshtein_distance

STATEMENT_COMPARISON_FUNCTION=levenshtein_distance

RESPONSE_SELECTION_METHOD = get_most_frequent_response