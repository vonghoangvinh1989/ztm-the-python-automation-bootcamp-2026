import requests
import html
import csv

# get input from users
number_of_questions = str(input("Please enter the number of trivia question you'd like to see: "))
difficulty = str(input("Please specify how difficult you'd like the question to be (easy/medium/hard): ")).lower()

url = f"https://opentdb.com/api.php"

request_params = {
    "amount": number_of_questions,
    "difficulty": difficulty,
    "category": "18"
}

# making request
response = requests.get(url, params=request_params, headers={"Accept": "application/json"})

# csv_content
csv_content = []

if response.ok:
    json_response = response.json()
    results = json_response["results"]

    for result in results:
        question = html.unescape(result['question'])

        if result['type'] == 'boolean':
            question = f"True or False? {html.unescape(result['question'])}"

        answer = html.unescape(result['correct_answer'])
        csv_content.append([question, answer])
else:
    print(f'Encountered an error. HTTP status code: {response.status_code}')

with open("tech trivia.csv", 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Question', 'Answer'])
    csv_writer.writerows(csv_content)
