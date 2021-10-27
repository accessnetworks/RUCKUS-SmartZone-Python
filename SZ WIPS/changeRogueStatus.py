import csv
from SmartZone_API_calls import SZ_API_calls
SmartZone = SZ_API_calls()

SZADDRESS = "<ip address>" # SmartZone IP address
SZUSER = "admin" # SmartZone user
SZPASSWORD = "password" # SmartZone password
ROGUESFILE = "rogue_list.csv" # .csv file with rogue device mac addresses

knownList = []
ignoreList = []
rogueList = []
maliciousList = []

token = SmartZone.getToken(SZADDRESS,SZUSER, SZPASSWORD)

with open(ROGUESFILE, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'\tMAC address       Status')
        print(f'\t{row["mac_address"]} {row["status"]}')
        if (row["status"] == "Known"):
            knownList.append(row["mac_address"])
            line_count += 1
            if (len(knownList) > 0):
                SmartZone.markKnown(SZADDRESS, [row["mac_address"]], token)
        if (row["status"] == "Ignore"):
            ignoreList.append(row["mac_address"])
            line_count += 1
            if (len(ignoreList) > 0):
                SmartZone.markIgnore(SZADDRESS, [row["mac_address"]], token)
        if (row["status"] == "Rogue"):
            rogueList.append(row["mac_address"])
            line_count += 1
            if (len(rogueList) > 0):
                SmartZone.markRogue(SZADDRESS, [row["mac_address"]], token)
        if (row["status"] == "Malicious"):
            maliciousList.append(row["mac_address"])
            line_count += 1
            if (len(maliciousList) > 0):
                SmartZone.markMalicious(SZADDRESS, [row["mac_address"]], token)
    print(f'Processed {line_count} lines')

r = SmartZone.deleteToken(SZADDRESS,token)