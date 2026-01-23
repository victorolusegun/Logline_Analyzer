from datetime import datetime
# Supposed to: read a line -> check it's validity -> extract info from valid lines -> Produce a human-readable summary report
# What makes a line valid: timestamp, type of info(INFO, WARNING or ERROR), message
print('Welcome')
with open('logfile.txt', 'r') as log_file:
    line = log_file.readline()
    print(line, end = '')
    test = line.split('|')
    print(test)
    if len(test) == 3:
        rule1 = test[0].strip()
        rule2 = test[1].strip()
        rule3 = test[2].strip()
        f1 = '%Y-%m-%d %H:%M:%S'
        try:
            v_rule1 = datetime.strptime(rule1, f1)
        except:
            if rule1 is not datetime:
                pass
            else:
                v_rule1 = datetime.strptime(rule1, f1)
    else:
        pass
    
    alert = ['INFO', 'ERROR', 'WARNING']

    if len(test) == 3 and rule2 in alert and type(v_rule1) is datetime:
        print('Valid line')
    else:
        print('Invalid line')
    # print(rule1)
    # print(rule2)
    # print(rule3)
    # v_rule1 = datetime.strptime(rule1, f1)
    # print(type(v_rule1))
    # if type(v_rule1) is datetime and type(rule2) is str and type(rule3) is str:
    #     print('Valid timestamp')
    # else:
    #     print('Invalid timestamp')



    # for line in log_file:
    #     print(line, end='')
    # if ' ' in line and '|' in line and '|' in line:
    #     print('Valid line')
    # else:
    #     print ('Invalid line')