from datetime import datetime
# Supposed to: read a line -> check it's validity -> extract info from valid lines -> Produce a human-readable summary report
# What makes a line valid: timestamp, type of info(INFO, WARNING or ERROR), message
print('Welcome \n')
valid = 0
invalid = 0

# file_name  = input('Enter fle path')
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

with open('summary.txt', 'w') as log_summary:
    log_summary.write(f'Summary Report\n')
    log_summary.write(f'====================\n')
    log_summary.write(f'Total valid lines: {valid}\n')
    log_summary.write(f'Total invalid lines: {invalid}\n')

print('\nSummary Report Generated\n')