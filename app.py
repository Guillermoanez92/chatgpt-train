import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define a function to interact with the chatbot
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=512,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=5
    )

    if response.choices[0].text:
        return response.choices[0].text.strip()
    else:
        return "Sorry, I didn't understand. Can you please rephrase?"

# Start the conversation with the chatbot
print("Bot: Hello! How can I assist you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'bye':
        print("Bot: Goodbye!")
        break
    response = chat_with_gpt("User: " + user_input)
    print("Bot:", response)

