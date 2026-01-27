# Import Libraries
from datetime import datetime

# Placeholder Welcome message
print('Welcome \n')

# Initializing counters
valid = 0
invalid = 0
attempt = 0

with open('logfile.txt', 'r') as log_file:
    for line in log_file:
        # print(line, end='')
        # line = log_file.readline()
        print(line, end = '')
        test = line.split('|')
        # print(test)
        if len(test) == 3:
            rule1 = test[0].strip()
            rule2 = test[1].strip()
            rule3 = test[2].strip()
            f1 = '%Y-%m-%d %H:%M:%S'
            try:
                v_rule1 = datetime.strptime(rule1, f1) 
            except ValueError:
                v_rule1 = None
        else:
            pass
        
        alert = ['INFO', 'ERROR', 'WARNING']
        # try:
        if len(test) == 3 and rule2 in alert and type(v_rule1) is datetime:
            # print('Valid line')
            valid = valid + 1
        else:
            # print('Invalid line')
            invalid = invalid + 1
        # except:
        #     if len(test) == 3 and rule2 in alert:
        #         # print('Invalid line')
        #         invalid = invalid + 1

# Requesting file path from user and input validation
file_name  = input('Enter file path: \n')
while file_name  == '' and attempt < 1:
    print('No file path provided. Please try again.\n')
    file_name  = input('Enter file path: \n')
    if file_name != '':
        print('Exiting')
        break
    attempt += 1
    if attempt >= 1:
        print('Max attempts reached. Program ending.')
        quit()
# print('Loop exited')

sth = file_name.endswith('.txt')
ext = '.txt'
if sth is False:
    file_name = file_name + ext
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
    quit()
# Writing reeport summary into a new file
with open('summary.txt', 'w') as log_summary:
    log_summary.write(f'Summary Report\n')
    log_summary.write(f'====================\n')
    log_summary.write(f'Total valid lines: {valid}\n')
    log_summary.write(f'Total invalid lines: {invalid}\n')

print('\nSummary Report Generated\n')
