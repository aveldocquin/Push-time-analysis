import sys
import csv
from collections import defaultdict
from datetime import datetime, timedelta

# Custom print with forced output
def my_print(string):
    print('pushTimeAnalytics > ' + string)
    sys.stdout.flush()

# Error function, exit with code 1
def error_handler(string):
    my_print(string)
    sys.exit(1)
    
# Read the database file
def read_file(filename):
    datas = []
    try:
        with open(filename, 'r') as f:
            next(f)
            reader = csv.reader(f)
            for row in reader:
                datas.append(list(row[i] for i in [1, 3]))
            f.close()
            return datas
    except:
        error_handler('Error: Please enter a valid database file.')

# Create the users dictionnary from datas
def create_users_dic(datas):
    tempDic = defaultdict(list)
    for user, timestamp in datas:
        tempDic[user].append(timestamp)
    return dict((user, tuple(timestamp)) for user, timestamp in tempDic.items())

# Get the ideal time to send the push notification with timestamps
def handle_users_timestamps(users):
    now = datetime.now()
    try:
        for key, value in users.items():
            date = i = 0
            for timestamp in value:
                d = (datetime.fromtimestamp(int(timestamp) / 1e3))
                date += (d.hour * 3600) + (d.minute * 60)
                i += 1
            date = (timedelta(seconds=date / i) - timedelta(minutes=10))
            if (date.days < 0):
                date += timedelta(hours=24)
            users[key] = date
        return users
    except:
        error_handler('Error: Please enter a database file with valid timestamps.')  

# Print the results 
def print_results(users):
    for key, value in users.items():
        print('\tuser: ' + key + ' | time : ' + str(value).split(".")[0])

# Main loop
if __name__ == '__main__':
    if len(sys.argv) < 2:
        error_handler("Usage: py pushAnalytics.py <dbname>")
    my_print('Database loading...')
    datas = read_file(sys.argv[1])
    my_print('Databases loaded.')
    users = create_users_dic(datas)
    my_print('Analysis in progress...')
    users = handle_users_timestamps(users)
    my_print('Results:')
    print_results(users)
