import re
import webbrowser
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

openJson = open(dir_path + '\\subscriptions.txt')
url = openJson.read()
writeFile = open(dir_path + '\\outputList.txt', 'w+')

urls = re.findall(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)

parsedURLs = []
for channel in urls:
    parsedURL = 'https://www.youtube.com/channel/' + \
        channel.split("channel_id=", 1)[1]
    parsedURLs.append(parsedURL)

for item in parsedURLs:
    writeFile.write('%s\n' % item)
writeFile.close()

for item in parsedURLs:
    webbrowser.open_new_tab(item)
