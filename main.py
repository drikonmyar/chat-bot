import re

def message_probability(user_input, recognised_words, single_response=False, required_words=[]):
    message_certainty=0
    has_required_words=True

    for word in user_input:
        if word in recognised_words:
            message_certainty+=1

    certainty_percentage = (float(message_certainty)/float(len(recognised_words)))*100

    for word in required_words:
        if word not in user_input:
            has_required_words=False
            break

    if has_required_words==True or single_response==True:
        return certainty_percentage
    else:
        return 0


def check_all_messages(user_input):
    highest_prob_list={}

    def response(bot_output,input_words,single_response=False,required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_output]=message_probability(user_input, input_words, single_response, required_words)

    
    response('Hello',['hello','hi','hey'],single_response=True)
    response("I'm doing great. What about you?",['what','how','are','you','doing'],required_words=['you','doing'])
    response('My name is Bot',['what','is','your','name'],required_words=['your','name'])
    response("I'm Bot",['who','are','you'],required_words=['who','you'])
    response("I help people",['what','you','do'],required_words=['you','do'])
    response("I help people by solving their queries",['how','you','help','people'],required_words=['how','help'])
    response('I mostly talk in English',['what','is','your','language','in','which','talk','speak','chat'],required_words=['language'])
    response("Currently I'm eating your computer memory :)",['what','you','eat'],required_words=['eat'])
    response("Thank you!",['i','love','you'], required_words=['love','you'])
    response("Thank you!",['i','like','you'], required_words=['like','you'])
    response("Thank you!",['great','good','well'], single_response=True)
    response("Okay! Hope to see you again.",['bye','close','exit'], single_response=True)


    best_match=max(highest_prob_list,key=highest_prob_list.get)
    # print(highest_prob_list)

    if highest_prob_list[best_match]<1:
        best_match="Sorry I couldn't understand, Google it."

    return best_match


    

def get_response(user_input):
    split_message=re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response=check_all_messages(split_message)
    return response


while True:
    user_input=input("User: ")
    bot_output=get_response(user_input)
    print("Bot: "+bot_output)
    if bot_output=="Okay! Hope to see you again.":
        break

