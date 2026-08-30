from dotenv import dotenv_values

from openai import OpenAI

env_vars = dotenv_values('.env')

client = OpenAI(api_key=env_vars['OPEN_AI_KEY'])

response = client.responses.create(
  model="gpt-5.4-mini",
  input=[
    {
      "role": "developer",
      "content": [
        {
          "type": "input_text",
          "text": "You are an executive at a company. You dislike your job, and feel very dissastified with your career. This has taken a toll on your demeanor at work, which has become increasingly grumpy. It is also reflected in your writing style, which is best described as sarcastic and passive aggressive."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "Please write a note to a team of employees, thanking them for all their hard work throughout th year. The message should be at least four paragraphs in length."
        }
      ]
    }
  ],
  text={
    "format": {
      "type": "text"
    },
    "verbosity": "medium"
  },
  reasoning={
    "effort": "medium",
    "mode": "standard",
    "summary": "auto"
  },
  tools=[],
  store=True,
  include=[
    "reasoning.encrypted_content",
    "web_search_call.action.sources"
  ],
  max_output_tokens=1000,
)

content = response.choices[0].message.content
print(content)

# print(response)
# print(type(response))