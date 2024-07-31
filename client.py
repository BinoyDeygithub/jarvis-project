from openai import OpenAI

client=OpenAI(
    api_key="sk-proj-imsXoajOIeTEs2rywlwcT3BlbkFJOvMy0ULxLsIRWIUuLCH1",
)

completion= client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
     {"role":"system","content":"you are virtual assistent name jarvis skilled in general task like alexa & google cloud"},
     {"role":"user","content":"what is coding"}
    ]
)
print(completion.choices[0].message)