from openai import OpenAI

client = OpenAI(
  api_key="Your_api_key"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": input("what do you want me to do: ")}
  ]
)
print(completion.choices[0].message.content)

#print(completion) #complex object
#print(completion.choices[0])
#print(completion.choices[0].message)
 #resultant string
