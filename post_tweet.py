import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials
import schedule
import tweepy
import time

#Twitter keys
CONSUMER_KEY = 'XXXX'
CONSUMER_SECRET = 'XXXX'
ACCESS_KEY = 'XXXX-XXXX'
ACCESS_SECRET = 'XXXX'

#Google keys
JSON_KEYFILE = 'XXXX'
SHEET_NAME = 'XXXX'

#the defined function, we will call this on a scheduler
def post_tweet() :
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds',
	 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEYFILE, scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open(SHEET_NAME).sheet1

    #update the cells
    cell_list = sheet.findall("Confirm")[1:]   
    
    #only post if there are valid posts
    if(len(cell_list) != 0):
        #get a random index
        index = random.randint(0,len(cell_list) - 1)
        cell = cell_list[index]

        #get the parts for the tweet
        tweet_you = sheet.cell(cell.row, 2)
        tweet_me = sheet.cell(cell.row, 3)

        #authenticate with twitter
        auth = tweepy.OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET )
        auth.set_access_token( ACCESS_KEY, ACCESS_SECRET )

        #Create the tweet string and check if it is too long
        tweet = "You: " + tweet_you + "\nMe, woke: " + tweet_me
        if len( tweet ) < 280 :

            #tweet it out
            api = tweepy.API( auth )
            api.update_status( tweet )

        #clear out the cell
        sheet.update_cell(cell.row, 4, '')

#the main function
def main() :
    #sets the scheduler
    schedule.every().day.at( "17:00" ).do( post_tweet )
    #running the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__" :
    main()
