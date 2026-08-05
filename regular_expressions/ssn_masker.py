# write a function that
# converts this: 123-45-6789
# to this: ***-**-6789
# But 123-45 shouldn't change
# An example of a valid SSN is 321-54-9876.
# However, 321-54 is NOT a valid SSN
import re

def ssn_masker(text_string):
    pattern = r'\d{3}-\d{2}-(\d{4})'
    result_text = re.sub(pattern, r'***-**-\1', text_string)
    return result_text

sample_text = 'An example of a valid SSN is 321-54-9876. However, 321-54 is NOT a valid SSN.'
print(ssn_masker(sample_text))
print(ssn_masker('321-54-9876'))