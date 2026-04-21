import json
import termcolor
from pathlib import Path

jsonstring = Path("people-e1.json").read_text()
people_list = json.loads(jsonstring)

total_people = len(people_list)
termcolor.cprint(f"Total people in database: {total_people}", 'yellow', attrs=['bold'])

for person in people_list:
    print('-' * 20)

    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    phoneNumbers = person['phoneNumber']

    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])
print('-' * 20)