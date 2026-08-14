from gen_fun import get_response

def main_bot():
    print("chatbot: Hi How can assist you sara?")

    while True:
        user_input = input("user: ").lower()
        response = get_response(user_input)
        print("chatbot:", response)

        if user_input == "goodbye":
            break
        