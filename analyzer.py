from datetime import datetime
# Supposed to: read a line -> check it's validity -> extract info from valid lines -> Produce a human-readable summary report
# What makes a line valid: timestamp, type of info(INFO, WARNING or ERROR), message
print('Welcome')
with open('logfile.txt', 'r') as log_file:
    line = log_file.readline()
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
        except:
            # if rule1 is not datetime:
            #     pass
            # else:
            #     v_rule1 = datetime.strptime(rule1, f1)
            pass
    else:
        pass
    
    alert = ['INFO', 'ERROR', 'WARNING']
    try:
        if len(test) == 3 and rule2 in alert and type(v_rule1) is datetime:
            print('Valid line')
        else:
            print('Invalid line')
    except:
        if len(test) == 3 and rule2 in alert:
            print('Invalid line')