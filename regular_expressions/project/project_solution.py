import re

phone_regex = r'\(?\d{3}\)?[- ]\d{3}[- ]\d{4}'
email_regex = r'([\w\.]+@\w+\.(com|net|org))'
website_regex = r'(^|\s)(\w+\.(com|net|org))'

with open('example_email.txt', 'r') as file:
    content = file.read()

phone_matches = re.findall(phone_regex, content)
email_matches = re.findall(email_regex, content, re.IGNORECASE)
website_matches = re.findall(website_regex, content, re.IGNORECASE)