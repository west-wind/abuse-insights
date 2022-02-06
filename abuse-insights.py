import requests, json, pprint, re, os, csv, ConfigParser
config                  = ConfigParser.ConfigParser()
config.readfp(open(r'abuseIPDB_API.conf'))
API                     = config.get('API_KEYS', 'API')

def regEx(comments):
    uname1, uname2, uname3 = '', '', ''
    extractedUsername1, extractedUsername2, extractedUsername3 = re.search(r"((?<=user\s)[a-zA-Z0-0]*)", comments), re.search(r"((?<=for\s)[a-zA-Z0-0]*)", comments), re.search(r"((?<=user=)[a-zA-Z0-0]*)", comments)
    if extractedUsername1 != None:
        uname1 = extractedUsername1.group().replace(".", "").encode('ascii')
    if extractedUsername2 != None:
        uname2 = extractedUsername2.group().replace(".", "").encode('ascii')
    if extractedUsername3 != None:
        uname3 = extractedUsername3.group().replace(".", "").encode('ascii')
    return uname1, uname2, uname3

url                     = 'https://api.abuseipdb.com/api/v2/check'
with open("abuseIPDB_Username_Intel.csv", "a") as inpFile:
    writer = csv.writer(inpFile)
    writer.writerow(["IP","Usernames Detected"])
ip                  = unicode(raw_input("\n[+] Enter IPv4 address: "))
queryString         = {'ipAddress': ip, 'maxAgeInDays': '90', 'verbose': 'true'}
headers             = {'Accept': 'application/json', 'Key': API}
try:
    print("[*] Checking IP address...")
    response            = requests.request(method='GET', url=url, headers=headers, params=queryString)
    usernameDetected    = []
    decodedResponse     = json.loads(response.text)['data']['reports']
    totalReports        = json.loads(response.text)['data']['totalReports']
    if totalReports != 0:
        reportComments      = [i['comment'] for i in decodedResponse]
        for comment in reportComments:
            username1, username2, username3  = regEx(comment)
            if username1 != None and username1 != '':
                usernameDetected.__iadd__([username1])
            if username2 != None and username2 != '':
                usernameDetected.__iadd__([username2])
            if username3 != None and username3 != '':
                usernameDetected.__iadd__([username3])
            if list(set(usernameDetected)):
                with open("abuseIPDB_Username_Intel.csv", "a") as inpFile:
                    writer = csv.writer(inpFile)
                    writer.writerow([ip,list(set(usernameDetected))])
        print("\n[*] Output has been stored in abuseIPDB_Username_Intel.csv file.")
    else:
        print("IP has not been reported to AbuseIPDB in the past 90 days. No data to save. Closing..")
except Exception as e:
    print("\n[!] Exception occured. Probably reached API limit or no reports found for IP.")
    print(e)