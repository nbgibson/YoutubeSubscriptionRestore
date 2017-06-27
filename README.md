# YoutubeSubscriptionRestore
A quick and dirty Python script to make the process of recovering subscribed channels a bit less painful


How to use

Visit https://www.youtube.com/subscription_manager and export your subscriptions to .xml via the "Export to RSS readers" tool at the bottom of the page. Move/rename the file to the directory that the script will run from and execute the python program. The program will parse through the document, extract the feed URLs, convert them to standard channel URLs, export them to a document in the local directory, and proceed to open all these URLs in new browser tabs to that you can more easily resubscribe when moving/changing channels.
