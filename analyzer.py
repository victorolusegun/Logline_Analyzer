# Import Libraries
from datetime import datetime

# Placeholder Welcome message
print('Welcome')

# Functions
def reask_input(user_input):
    print('Please try again')
    user_input = input('Enter file path: \n')
    return user_input

def file_extension(valid_file):
    check = valid_file.endswith('.txt')
    ext = '.txt'
    if check is False:
        valid_file = valid_file + ext
    return valid_file

# Assigning values to variables
valid = 0
invalid = 0
attempt = 0
counter = 0
alert = ['INFO', 'ERROR', 'WARNING']

# Requesting file path from user and input validation
file_name  = input('Enter file path: \n')
while file_name  == '' and attempt < 1:
    print('No file path provided.')
    file_name = reask_input(file_name)
    attempt += 1
    if file_name != '':
        break
    if attempt >= 1:
        print('Max attempts reached. Program ending.')
        quit()
    # print('Loop exited')

file_name = file_extension(file_name)

# Opening, reading and analyzing file
while file_name == '' or counter < 1:
    try:
        with open(file_name, 'r') as log_file:
            for line in log_file:
                # print(line, end = '')
                # Text preprocesing & Checking line validity
                test = line.split('|')
                # v_rule1 = None
                # rule2 = []
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
                    rule2 = []
                # Final validity check
                if len(test) == 3 and rule2 in alert and v_rule1 is not None:
                    valid = valid + 1
                else:
                    invalid = invalid + 1
    except FileNotFoundError:
        print(f'{file_name} not found.')
        file_name = ''
    counter += 1
    if file_name == '':
        file_name = reask_input(file_name)
        file_name = file_extension(file_name)
        if file_name != '':
            counter = 0


# Writing reeport summary into a new file
print('\n\nSummary Report Generated\n')
save_path = input('Enter path to save report: (default: report.txt)\n')
if save_path == '':
    save_path = 'report.txt'
with open(save_path, 'w') as log_summary:
    log_summary.write(f'Summary Report\n')
    log_summary.write(f'====================\n')
    log_summary.write(f'Total valid lines: {valid}\n')
    log_summary.write(f'Total invalid lines: {invalid}\n')
print('Report successfully saved.')