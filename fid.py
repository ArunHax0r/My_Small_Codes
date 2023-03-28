import webbrowser as wb

# Enter your User Name
uid = input("Enter the user name: ")
url = "www.facebook.com/"

# It opens in your Default browser and Checks for the Username in Facebook website
def getFbid():
    print('Fetching details...')
    wb.open(url + uid, new=0, autoraise=True)
    
getFbid()
