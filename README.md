Twitter Sheets

This code posts a tweet on Twitter at 5 every day.
We have a Google Sheets backend that contains all of the Tweets we want to tweet so that we can add to a repository of tweets from anywhere.
We add to the repository by a Google forms front end.

The code is written in python.
	The things that you would need to change if you wanted to use this is the credentials at the top.
	
	The Twitter keys come from developer.twitter.com after you apply for a developer account.
	The Google Keyfile comes from the Google Drive API.
	The Sheet name is the name of the sheet that your data is coming from.

Our sheet is formatted:
	Top row is the title for each column.
	Every row is timestamp, you, me, and a column with the word "Confirm" in it that will clear out when the row is used.
