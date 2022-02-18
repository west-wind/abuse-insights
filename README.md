# Abuse INSIGHTS  
**Abuse INSIGHTS** is a python script created to extract the usernames brute forced by a compromised host. This data is extracted by regex from Abuse IP DB's reporter comments.
# Installing
## Prerequisites
 - Python 2.7
## Dependencies
 - Abuse IP DB API Key. Get one from https://www.abuseipdb.com
## Installation 

    $ git clone https://github.com/west-wind/abuse-insights.git
    $ cd abuse-insights
    $ python abuse-insights.py
# Intended Use
The intention of this script is to obtain insights about the sort of usernames that are attempted in a brute force from a compromised host. This can be an RDP, SSH etc brute force. Assuming your host was compromised and was used for brute-forcing SSH nodes, and folks started reporting your IP to AbuseIPDB. When folks report, they sometimes share the raw log, and this log has information related to the username it was attempting to login with. Generating a list of the usernmaes used can provide insight into the sort of adversary that compromised your host. 

It is the end user's responsibility to obey all applicable local, state and federal laws. Developer assume no liability and are not responsible for any misuse or damage caused by this program. 
# Getting Started
This script requires the user to input the AbuseIPDB API key into the configuration file - **abuseIPDB_API.conf**. 

To begin

    $ cd abuse-insights
    $ python abuse-insights.py

Enter target IP address.

IF the IP address has been reported to Abuse IP DB in the past 90 days, & username data was avaialble, then output will be saved to a csv file - **abuseIPDB_Username_Intel.csv**.

## Reporting Errors
If you encounter an error, create an issue here. Currently this script uses 3 regular expressions to extract username related information from reporter comments. If you notice the need to extract usernames from a different type of reporter comment, please create an issue here. 

# Built With
 - Python
 - Abuse IP DB API ([Abuse IP DB API Documentation](https://www.abuseipdb.com/api.html))   

# Authors
Alex John, B. ([@Praetorian_GRD](https://twitter.com/Praetorian_GRD))

# License
Copyright (C) 2022 Alex John, B. This project is licensed under the MIT License - see the [LICENSE.md](https://raw.githubusercontent.com/west-wind/abuse-insights/main/LICENSE) file for details.
