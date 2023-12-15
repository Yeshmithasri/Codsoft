data={
    "hi":"Hey! I'm here to help you",
    "hello":"Hello! How can I assist you today?",
    "hey":"Hi there!",
    "what is your name":"I'm Bubble",
    "what are you doing":"I'm just waiting to help you out",
    "what color do you like":"Same as you",
    "what do you like to eat ":"I'm a simple bot..I don't like",
    "tell me a joke":"This one is an acquired taste: Did you know that all clouds have dandruff?....That's where snowflakes come from,The right eye said to the left eye,between you and me, something smells",
    "tell me about yourself":"I'm curious,helpful and always looking for reasons to use an emoji",
    "who is your boss":"I look up to humans who are curious about the world. You definitely fit the bill",
    "do you like someone":"Ofcourse! Its you",
    "that's great,thank you":"Glad to help you",
    "thank you":"Your welcome",
    "bye":"Byee",
}
def get_response(user_input):
    for pattern,response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry,I didn't understand that.Can you please rephrase your sentence?"
print("Bubble: Hi! I'm here to assist you!")
while True:
    user_input=input("Me: ")
    if user_input=='bye':
       print("Bubble: Goodbye! Have a great day!")
       break
    response=get_response(user_input)
    print("Bubble:",response)