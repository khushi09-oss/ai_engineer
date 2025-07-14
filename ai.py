from openai import OpenAI

client = OpenAI(
  api_key="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"
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
