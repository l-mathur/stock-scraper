#import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#store the page urls to be scraped
page_urls = ['https://www.bloomberg.com/quote/SPX:IND', 
'https://www.bloomberg.com/quote/VTI:US']

# extract data from all page_urls
data = []
message = []
for url in page_urls:
 # query the website and return the html to 'page_html'
 page_html = urlopen(url)
 # parse the html using beautiful soap and store in variable `soup`
 page_soup = BeautifulSoup(page_html, 'html.parser')
 
 #get index name
 name_box = page_soup.find('h1', attrs={'class': 'name'})
 name = name_box.text.strip() 
 # get index price
 price_box = page_soup.find('div', attrs={'class':'price'})
 price = price_box.text

 line = name + " is currently at this price: " + price
 # save the data in triple
 data.append((name, price))
 message.append(line)

#append data to csv for storage
with open('stock_data.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	for name,price in data:
		writer.writerow([name, price, datetime.now().date(), datetime.now().time()])

finalMessage = ""
count = 0
for str in message:
	if count==0 :
		finalMessage = str + ". "
		count = count + 1
	else :
		finalMessage = finalMessage + str + ". "

#send stock information as an email

#specify "from" and "to" email addresses
from_address = "SENDER ADDRESS"
to_address = "RECIPIENT ADDRESS"

#construct the message with MIMEMultipart
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = 'Stock Update for ' + datetime.now().strftime('%Y-%m-%d')
msg.attach(MIMEText(finalMessage, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

#replace with user's from_address password
server.login(from_address, "FROM_ADDRESS PASSWORD")
text = msg.as_string()

#replace with the desired email and destination email
server.sendmail(from_address, to_address, text)
server.quit()
