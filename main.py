from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests #to use json data
from send_email import send_email


api_key="ee193857b06e43e38fa5679a4469887a"                      #newsapi.org
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-19&sortBy=publishedAt&apiKey="\
      "ee193857b06e43e38fa5679a4469887a&language=en"

# Create the container email message.
message = MIMEMultipart()
message['Subject'] = "Today's News"
message['From'] = 'sanjanaarj2003@gmail.com'  # Replace with your email address
message['To'] = 'sanjanaarj2003@gmail.com'  # Replace with recipient's email address

#Make request
request = requests.get(url)
content = request.json()            #Get a dictioary with data      -- json gets a dictionary   ;  #if content = request.text was used, the output would be string type

#Access the article titlw and description
body = " "

# Iterates and sends an email topicwise along with description
for article in content['articles'][:20]:
    body += article["title"] + "\n" + str(article["description"]) + "\n" + article["url"] + 2 * "\n"

# Attach the body to the email message
message.attach(MIMEText(body, 'plain'))

# Encode the entire message
encoded_message = message.as_string().encode("utf-8")

# Send the email
send_email(message=encoded_message)


#
# In the adjusted code:
#
# - I've used MIMEMultipart to create a message object that can hold both plain text and other parts (attachments, etc.).
#
# - The Subject is set only once in the message headers.
#
# - The body is built up with the articles' information.
#
# - Then, the body is attached to the message as plain text.
#
# -Finally, the message is encoded to UTF-8.
#
# Ensure that your send_mail function is set up to handle an email message object correctly. It should properly set up the SMTP connection, authenticate, and send the MIME message. This function is not shown in your snippet, but it will need to handle these tasks.
#
# Please replace 'your_email@example.com' and 'recipient_email@example.com' with the actual email addresses you're using to send and receive the email.
#
