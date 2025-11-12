from openai import OpenAI

client = OpenAI(
  api_key="your_api_key"
)
prompt=input("Enter your prompt here:")
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)
