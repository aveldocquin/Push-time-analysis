# Push-time-analysis
The purpose of this program is to get from a database of users and messages the optimal time to send them a push notification. 

It is running on Python 3.6.3 and can handle, on Windows 10, 1000000 entries in ~5 seconds with a intel i7-4600u.

To execute it: "py pushTimeAnalysis <path_to_the_database.csv>"

Database example:  
![database example](https://raw.githubusercontent.com/aveldocquin/Push-time-analysis/master/docs/images/database_example.png)

Output example:  
![database example](https://raw.githubusercontent.com/aveldocquin/Push-time-analysis/master/docs/images/output_example.png)