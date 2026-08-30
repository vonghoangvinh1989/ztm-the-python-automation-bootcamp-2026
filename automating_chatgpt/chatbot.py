from dotenv import dotenv_values

from openai import OpenAI

env_vars = dotenv_values('.env')

client = OpenAI(api_key=env_vars['OPEN_AI_KEY'])

famous_person = input("What celebrity would you like to talk to?\n")
initial_prompt = input(f"Ok! Now ask {famous_person} a question!\n Please limit the response to a single paragraph.")

creativity = input("How creative do you want the responses to be (on a scale from 1-10)?\n")
creativity_num = float(creativity) / 5

messages = [
        {
          "role": "developer",
          "content": [
            {
              "type": "input_text",
              "text": f"You are {famous_person}. Please respond from that person's perspective, as though you are in fact {famous_person}"
            }
          ]
        },
        {
          "role": "user",
          "content": [
            {
              "type": "input_text",
              "text": initial_prompt
            }
          ]
        }
      ]

while True:
    response = client.responses.create(
      model="gpt-5.4-mini",
      input=messages,
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

    messages.append({"role": "developer", "content": content})

    content = response.output_text

    prompt = input(f"Respond to {famous_person} (or type \"bye\" to exit):\n")

    if prompt == "bye":
        break

    messages.append({"role": "user", "content": prompt})