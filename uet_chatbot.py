import json
import random
def load_knowledge():
    try:
        with open('knowlegde.json','r') as f:
            return json.load(f)
    except:
        return{"qna":[]}

def save_knowledge(data):
    with open('knowlegde.json','w') as f:
        json.dump(data,f,indent=4)

def get_response(user_input,knowledge):
    user_input=user_input.lower()
    for item in knowledge["qna"]:
        if item["question"].lower() in user_input:
            return random.choice(item["answers"])

    return "Sorry,I dont know yet.Can you teach me?TYPE:teach|question|answer"


def main():
    knowledge=load_knowledge()
    print("UET helperbot:Hi!I m here to help UET students.Type 'exit' to quit.")
    while True:
        user_input = input("You:")
        if user_input.lower()=='exit':
            break

        if user_input.startswith("teach|"):
            _,q,a = user_input.split("|")
            knowledge["qna"].append({"question":q,"answers":[a]})
            save_knowledge(knowledge)
            print("Bot:Got it! I learned something new.")
        else:
            response = get_response(user_input,knowledge)    
            print(f"Bot:{response}")


if __name__=="__main__":
    main()     


































            