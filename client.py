from openai import OpenAI
 
# PIP pinstall openai. 
# If you saved the key under a different environment variable name, you can do something like.

client = OpenAI(
  api_key="sk-proj-YsDwjJ84WLdNBSGftblMT3BlbkFJFhfQzyBvtEGos3ckd7jP",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)