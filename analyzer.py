# Import Libraries
from datetime import datetime

# Placeholder Welcome message
print('Welcome')

# Functions
def accept_input(user_input):
    print('Please try again')
    user_input = input('Enter file path: \n')
    return user_input

def file_extension(valid_file):
    ext = '.txt'
    if sth is False:
        valid_file = valid_file + ext
    return valid_file

def checking_file_validity(file):
    check = file.endswith('.txt')
    return check

# Initializing counter variables
valid = 0
invalid = 0
attempt = 0

# Storing valid alert types in list
alert = ['INFO', 'ERROR', 'WARNING']

# Requesting file path from user and input validation
file_name  = input('Enter file path: \n')
while file_name  == '' and attempt < 1:
    print('No file path provided.')
    file_name = accept_input(file_name)
    if file_name != '':
        print('Exiting')
        break
    attempt += 1
    if attempt >= 1:
        print('Max attempts reached. Program ending.')
        quit()
# print('Loop exited')

sth = checking_file_validity(file_name)
# if sth is False:
file_name = file_extension(file_name)
    # print(file_name)

try:
    with open(file_name, 'r') as log_file:
        for line in log_file:
            print(line, end = '')
            # Text preprocesing
            test = line.split('|')
            # Checking line validity
            if len(test) == 3:
                rule1 = test[0].strip()
                rule2 = test[1].strip()
                rule3 = test[2].strip()
            # Validation and confirmation of timestamp
                f1 = '%Y-%m-%d %H:%M:%S'
                try:
                    v_rule1 = datetime.strptime(rule1, f1) 
                except ValueError:
                    v_rule1 = None
            else:
                pass
            # Final validity check
            if len(test) == 3 and rule2 in alert and type(v_rule1) is datetime:
                valid = valid + 1
            else:
                invalid = invalid + 1
except FileNotFoundError:
    print(f'{file_name} not found. Exiting program.')
    quit()
    # print(f'{file_name} not found.')
    # file_name = accept_input(file_name)
    # if file_name != '':
    #     sth = checking_file_validity(file_name)

# Writing reeport summary into a new file
with open('summary.txt', 'w') as log_summary:
    log_summary.write(f'Summary Report\n')
    log_summary.write(f'====================\n')
    log_summary.write(f'Total valid lines: {valid}\n')
    log_summary.write(f'Total invalid lines: {invalid}\n')

print('\n\nSummary Report Generated\n')