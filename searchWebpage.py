import time
from urllib.request import urlopen, Request

# setting the URL you want to monitor
number = "NEWY202107190004"
mynumber = "NEWY202107270005"
def status(number):
    url = Request('https://www.mzv.cz/consulate.newyork/en/visa_and_consular_information/visa/approved_visa/short_term_visa_approved.html')
    
    # to perform a GET request and load the 
    # content of the website and store it in a var
    response = urlopen(url).read()
    if number in str(response):
        print(True)
    else:
        print(False)

status(mynumber)