from openai import OpenAI

client = OpenAI(
  api_key="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"
)
chat_transcript = """Agent: Hello! Thank you for contacting TechWorld Support. My name is Alex. How can I help you today?
Customer: Hi Alex, I'm having trouble logging into my account. It says "invalid password" even though I'm sure it's correct.
Agent: I'm sorry to hear that. Let's get this sorted out. Can you please confirm the email address associated with your account?
Customer: Sure, it's john.doe@example.com.
Agent: Thank you. One moment while I check your account.
Agent: It looks like your account was locked after multiple failed login attempts. I'll unlock it now and send a password reset link to your email.
Customer: Oh, I see. Thanks for that. I’ll check my inbox.
Agent: No problem. Please let me know once you've reset your password and tried logging in again.
Customer: Got it. I reset the password and was able to log in successfully. Thank you for your help!
Agent: You're very welcome, John. Is there anything else I can assist you with today?
Customer: No, that’s all. Have a great day!
Agent: You too! Thanks for contacting TechWorld Support. Goodbye!"""

prompt=f"Summarize the customer support chat in three concise key points: {chat_transcript}"
max_completion_tokens=500
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": prompt}
  ],
    max_completion_tokens=max_completion_tokens #limit response length
)

ip_token_price = 0.15/1_000_000 #openai's pricing is per million tokens
op_token_price = 0.6/1_000_000

ip_tokens = completion.usage.prompt_tokens
op_tokens = max_completion_tokens

cost= (ip_tokens*ip_token_price) + (op_tokens*op_token_price)
print(cost)