from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)



bot = ChatBot("docbot", read_only=False, storage_adapter='chatterbot.storage.SQLStorageAdapter', 
    logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.TimeLogicAdapter', 'chatterbot.logic.BestMatch',
        
        {   
            
            "import_path":"chatterbot.logic.BestMatch",
            "default_response":"Sorry I don't understand.",
            "maximum_similarity_threshold": 0.9
        }
        
        ], database_uri='sqlite:///database.sqlite3')




list_trainer = ListTrainer(bot)




trainer_corpus = ChatterBotCorpusTrainer(bot)

trainer_corpus.train("chatterbot.corpus.english")


@app.route("/")
def main():
  return render_template("index.html")



@app.route("/get")
def get_chatbot_response():
  userText = request.args.get('userMessage')
  return str(bot.get_response(userText))


if __name__ == "__main__":
  app.run(debug=True)

