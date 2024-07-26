import openai


class ChatBox:
    def __init__(self):
        openai.api_key = "sk-IMKC3xi36HselABsHT9ZT3BlbkFJe9DH1slqo1yuXQRBl"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbox = ChatBox()
    response = chatbox.get_response("write joke on brother.")
    print(response)
