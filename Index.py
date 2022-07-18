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


convo1 = [
    "Hi",
    "Hi there! How can I help you?",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What can I do if I have a cold?",
    "You can get information about cold on <a href='https://www.webmd.com/cold-and-flu/8-tips-to-treat-colds-and-flu-the-natural-way' target='_blank'>cold</a>",
    "What do I do if I have fever?",
    "You can get information about fever on <a href='https://my.clevelandclinic.org/health/symptoms/10880-fever' target='_blank'>fever</a>",
    "What if someone is unconscious?",
    "If someone is unconscious see how you can help on <a href='https://www.medicalnewstoday.com/articles/322872' target='_blank'>unconsciousness</a>",
    "How do I stop bleeding?",
    "To know about how you can stop bleeding see <a href='https://www.webmd.com/first-aid/bleeding-cuts-wounds' target='_blank'>bleeding</a>",
    "What if someone is choking?",
    "If someone is choking see how you can help on <a href='https://www.webmd.com/first-aid/choking-treatment' target='_blank'>choking</a>" ,
    "How to treat burns?",
    "To treat burns, you can get information on <a href='https://www.webmd.com/first-aid/thermal-heat-or-fire-burns-treatment' target='_blank'>burns</a>",
    "How to treat blisters?",
    "To treat blisters, you can get information on <a href='https://www.webmd.com/first-aid/blisters-treatment' target='_blank'>blisters</a>",
    "What if someone got a sprain?",
    "If someone is unconscious see how you can help on <a href='https://www.webmd.com/first-aid/sprains-and-strains-treatment' target='_blank'>sprain</a>",
    "What if someone has nosebleed?",
    "If someone has nosebleed see how you can help on <a href='https://www.mayoclinic.org/first-aid/first-aid-nosebleeds/basics/art-20056683#:~:text=Pinch%20your%20nose.,stops%20the%20flow%20of%20blood' target='_blank'>nosebleed</a>",
    "How to treat frostbite?",
    "To treat frostbite, you can get information on <a href='https://www.mayoclinic.org/first-aid/first-aid-frostbite/basics/art-20056653#:~:text=Gently%20rewarm%20frostbitten%20areas.,feel%20very%20warm%2C%20not%20hot.' target='_blank'>frostbite</a>",
    "How to treat a bee sting?",
    "To treat bee stings, you can get information on <a href='https://www.webmd.com/first-aid/bee-and-wasp-stings-treatment' target='_blank'>beesting</a>",
    "What are the symptoms of someone infected with a coronavirus?",
    "It depends on the virus, but common signs include respiratory symptoms, fever, cough, shortness of breath, and breathing difficulties. In more severe cases, infection can cause pneumonia, severe acute respiratory syndrome, kidney failure and even death.",
    "What is diabetes?",
    "Diabetes is a chronic disease that occurs when the pancreas is no longer able to make insulin, or when the body cannot make good use of the insulin it produces.Insulin is a hormone made by the pancreas, that acts like a key to let glucose from the food we eat pass from the blood stream into the cells in the body to produce energy. All carbohydrate foods are broken down into glucose in the blood. Insulin helps glucose get into the cells. Not being able to produce insulin or use it effectively leads to raised glucose levels in the blood (known as hyperglycaemia). Over the long-term high glucose levels are associated with damage to the body and failure of various organs and tissues.",
    "Do I have diabetes?",
    "You can know more about diabetes on <a href='https://www.idf.org/aboutdiabetes/what-is-diabetes.html' target='_blank'>diabetes</a>",
    "What is chickenpox?",
    "Know more about chickenpox on <a href='https://www.mayoclinic.org/diseases-conditions/chickenpox/symptoms-causes/syc-20351282#:~:text=Chickenpox%20is%20an%20infection%20caused,that%20protects%20children%20against%20chickenpox.' target='_blank'>chickenpox</a>",
    "What is malaria?",
    "Here is a link to know about malaria: <a href='https://www.mayoclinic.org/diseases-conditions/malaria/symptoms-causes/syc-20351184#:~:text=Malaria%20is%20a%20disease%20caused,in%20tropical%20and%20subtropical%20countries.' target='_blank'>malaria</a>",
    "What is dengue?",
    "<a href='https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue#:~:text=Dengue%20is%20a%20viral%20infection,called%20dengue%20virus%20(DENV).' target='_blank'>dengue</a>",
    "What if someone is dehydrated?",
    "For dehydration check <a href='https://www.webmd.com/a-to-z-guides/dehydration-adults' target='_blank'>dehydration</a>",
    "What are allergies?",
    "To know more about allergies check <a href='https://my.clevelandclinic.org/health/diseases/8610-allergy-overview#:~:text=Allergies%20are%20your%20body's%20reaction,eyes%20%E2%80%93%20to%20life%2Dthreatening.' target='_blank'>allergies</a>",
    "What causes headaches?",
    "To know what causes headaches check <a href='https://my.clevelandclinic.org/health/diseases/9639-headaches' target='_blank'>headaches</a>",
    "What if i feel nauseous?",
    "For nausea check <a href='https://www.everydayhealth.com/nausea/guide/' target='_blank'>nausea</a>",
    "What are the symptoms of corona?",
    "Most common symptoms : fever, cough, tiredness, loss of taste or smell; Less common symptoms: sore throat, headache, aches and pains, diarrhea, a rash on skin, or discolouration of fingers or toes, red or irritated eyes; Serious symptoms:difficulty breathing or shortness of breath, loss of speech or mobility, or confusion, chest pain. Seek immediate medical attention if you have serious symptoms. Always call before visiting your doctor or health facility. People with mild symptoms who are otherwise healthy should manage their symptoms at home. On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.",
    "How can I avoid getting infected from corona?",
    "The virus enters your body via your eyes, nose and/or mouth, so it is important to avoid touching your face with unwashed hands. Washing of hands with soap and water for at least 20 seconds, or cleaning hands with alcoholbased solutions, gels or tissues is recommended in all settings. It is also recommended to stay 1.5 meter or more away from people infected with COVID-19(social distancing) who are showing symptoms, to reduce the risk of infection through respiratory droplets.",
    "What should I do if I have had close contact with someone who has COVID-19?",
    "Notify public health authorities in your area who will provide guidance on further steps to take. If you develop any symptoms, you should immediately contact your healthcare provider for advice.",

]

convo2 = [
    "Hello",
    "Hey there! How can I help you?",
    "How are you?",
    "I'm good.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "What if I have a cold?",
    "Get information about cold on <a href='https://www.webmd.com/cold-and-flu/8-tips-to-treat-colds-and-flu-the-natural-way' target='_blank'>cold</a>",
    "What if I a have fever?",
    "You can get information about fever on <a href='https://my.clevelandclinic.org/health/symptoms/10880-fever' target='_blank'>fever</a>",
    "What if someone is unconscious?",
    "If someone is unconscious see how you can help on <a href='https://www.medicalnewstoday.com/articles/322872' target='_blank'>unconsciousness</a>",
    "How do I stop bleeding?",
    "To know about how you can stop bleeding see <a href='https://www.webmd.com/first-aid/bleeding-cuts-wounds' target='_blank'>bleeding</a>",
    "How to help someone who is choking?",
    "If someone is choking see how you can help on <a href='https://www.webmd.com/first-aid/choking-treatment' target='_blank'>choking</a>" ,
    "How do you treat burns?",
    "Get information for treating burns on <a href='https://www.webmd.com/first-aid/thermal-heat-or-fire-burns-treatment' target='_blank'>burns</a>",
    "How to treat blisters?",
    "Get information on treating <a href='https://www.webmd.com/first-aid/blisters-treatment' target='_blank'>blisters</a>",
    "What if someone got a sprain?",
    "See how you can help with a sprain on <a href='https://www.webmd.com/first-aid/sprains-and-strains-treatment' target='_blank'>sprain</a>",
    "What if someone has nosebleed?",
    "See how you can treat nosebleed on <a href='https://www.mayoclinic.org/first-aid/first-aid-nosebleeds/basics/art-20056683#:~:text=Pinch%20your%20nose.,stops%20the%20flow%20of%20blood' target='_blank'>nosebleed</a>",
    "How can we treat frostbite?",
    "To treat frostbite, you can get information on <a href='https://www.mayoclinic.org/first-aid/first-aid-frostbite/basics/art-20056653#:~:text=Gently%20rewarm%20frostbitten%20areas.,feel%20very%20warm%2C%20not%20hot.' target='_blank'>frostbite</a>",
    "How to treat a bee sting?",
    "To treat bee stings, you can get information on <a href='https://www.webmd.com/first-aid/bee-and-wasp-stings-treatment' target='_blank'>beesting</a>",
    "What are the symptoms if one is infected by the coronavirus?",
    "It depends on the virus, but common signs include respiratory symptoms, fever, cough, shortness of breath, and breathing difficulties. In more severe cases, infection can cause pneumonia, severe acute respiratory syndrome, kidney failure and even death.",
    "What is diabetes?",
    "Diabetes is a chronic disease that occurs when the pancreas is no longer able to make insulin, or when the body cannot make good use of the insulin it produces.Insulin is a hormone made by the pancreas, that acts like a key to let glucose from the food we eat pass from the blood stream into the cells in the body to produce energy. All carbohydrate foods are broken down into glucose in the blood. Insulin helps glucose get into the cells. Not being able to produce insulin or use it effectively leads to raised glucose levels in the blood (known as hyperglycaemia). Over the long-term high glucose levels are associated with damage to the body and failure of various organs and tissues.",
    "Do I have diabetes?",
    "You can know more about diabetes on <a href='https://www.idf.org/aboutdiabetes/what-is-diabetes.html' target='_blank'>diabetes</a>",
    "What is chickenpox?",
    "Know more about chickenpox on <a href='https://www.mayoclinic.org/diseases-conditions/chickenpox/symptoms-causes/syc-20351282#:~:text=Chickenpox%20is%20an%20infection%20caused,that%20protects%20children%20against%20chickenpox.' target='_blank'>chickenpox</a>",
    "What is malaria?",
    "Here is a link to know about malaria: <a href='https://www.mayoclinic.org/diseases-conditions/malaria/symptoms-causes/syc-20351184#:~:text=Malaria%20is%20a%20disease%20caused,in%20tropical%20and%20subtropical%20countries.' target='_blank'>malaria</a>",
    "What is dengue?",
    "<a href='https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue#:~:text=Dengue%20is%20a%20viral%20infection,called%20dengue%20virus%20(DENV).' target='_blank'>dengue</a>",
    "What if someone is dehydrated?",
    "For dehydration check <a href='https://www.webmd.com/a-to-z-guides/dehydration-adults' target='_blank'>dehydration</a>",
    "What are allergies?",
    "To know more about allergies check <a href='https://my.clevelandclinic.org/health/diseases/8610-allergy-overview#:~:text=Allergies%20are%20your%20body's%20reaction,eyes%20%E2%80%93%20to%20life%2Dthreatening.' target='_blank'>allergies</a>",
    "What causes headaches?",
    "To know what causes headaches check <a href='https://my.clevelandclinic.org/health/diseases/9639-headaches' target='_blank'>headaches</a>",
    "What if i feel nauseous?",
    "For nausea check <a href='https://www.everydayhealth.com/nausea/guide/' target='_blank'>nausea</a>",
    "What are the symptoms of corona?",
    "Most common symptoms : fever, cough, tiredness, loss of taste or smell; Less common symptoms: sore throat, headache, aches and pains, diarrhea, a rash on skin, or discolouration of fingers or toes, red or irritated eyes; Serious symptoms:difficulty breathing or shortness of breath, loss of speech or mobility, or confusion, chest pain. Seek immediate medical attention if you have serious symptoms. Always call before visiting your doctor or health facility. People with mild symptoms who are otherwise healthy should manage their symptoms at home. On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.",
    "How can I avoid getting infected from corona?",
    "The virus enters your body via your eyes, nose and/or mouth, so it is important to avoid touching your face with unwashed hands. Washing of hands with soap and water for at least 20 seconds, or cleaning hands with alcoholbased solutions, gels or tissues is recommended in all settings. It is also recommended to stay 1.5 meter or more away from people infected with COVID-19(social distancing) who are showing symptoms, to reduce the risk of infection through respiratory droplets.",
    "What should I do if I have had close contact with someone who has COVID-19?",
    "Notify public health authorities in your area who will provide guidance on further steps to take. If you develop any symptoms, you should immediately contact your healthcare provider for advice.",

]



list_trainer = ListTrainer(bot)
list_trainer.train(convo1)
list_trainer.train(convo2)



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

