import webbrowser as wb

# Enter your User Name
uid = input("Enter the user name: ")
url = "twitter.com/"

# It opens in your Default browser and Checks for the Username in Twitter website
def getTwid():
    print('Fetching details...')
    wb.open(url + uid, new=0, autoraise=True)
    
getTwid()
