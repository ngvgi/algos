import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr.Smidcht

'''

sentence = 'Start a sentence and then bring it to an end'

# match any digit
# pattern = re.compile(r'\d')

# match any 'word' character(a-z,A-z,0-9)
# pattern = re.compile(r'\w')

# match any space (tab, space, newline) 
# pattern = re.compile(r'\s')

# match any space (tab, space, newline) 
# pattern = re.compile(r'\s')

# match any number separated by a dash or dot
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')

# match 800 or 900 at the beginning
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# match all the misters in text_to_search
# pattern = re.compile(r'Mr\.?\s?[A-Z]\w*')

# match all Mr. Mrs. Ms. regardless of whether they have the period
# pattern = re.compile(r'M(r|s|rs)\.?\s?[A-Z]\w*')





pattern = re.compile(r'M(r|s|rs)\.?\s?[A-Z]\w*')
matches = pattern.finditer(text_to_search)

# with open('data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

for match in matches:
    print (match)

