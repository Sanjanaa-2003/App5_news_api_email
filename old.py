
import requests
from send_email import send_email


api_key="ee193857b06e43e38fa5679a4469887a"
url="https://newsapi.org/v2/everything?q=tesla"\
     "&from=2023-11-19&sortBy=publishedAt&apiKey="\
     "ee193857b06e43e38fa5679a4469887a&language=en"

#Make request
request = requests.get(url)

#Get a dictioary with data      -- json gets a dictionary
content = request.json()    #if content = request.text was used, the output would be string type

#Access the article titlw and description
body = " "
# Iterates and sends an email topicwise along with description
for article in content["articles"][:20]:     #In key articles: searches for titles and description

    if article["title"] is not None:
        body = "Subject: Today's news" + "\n"\
               + body + article["title"] + "\n" \
               + str(article["description"]) + "\n" \
               + article["url"] + 2 * "\n"



body = body.encode("utf-8")
send_email(message=body)





# On running this code the following error occurred:
# The error message you're seeing indicates that the email you're trying to send is being rejected by Gmail's SMTP server because it does not comply with RFC 5322 standards. The specific complaint is that there are multiple Subject headers in your message, which is a common characteristic of spam emails.
#Traceback (most recent call last):
#   File "E:\app5-news-api-email\old.py", line 31, in <module>
#     send_email(message=body)
#   File "E:\app5-news-api-email\send_email.py", line 18, in send_email
#     server.sendmail(username, receiver, message)
#   File "C:\Users\Jayachandran\AppData\Local\Programs\Python\Python311\Lib\smtplib.py", line 908, in sendmail
#     raise SMTPDataError(code, resp)
# smtplib.SMTPDataError: (550, b'5.7.1 This message is not RFC 5322 compliant. There are multiple Subject\n5.7.1 headers. To reduce the amount of spam sent to Gmail, this message has\n5.7.1 been blocked. For more information, go to\n5.7.1  https://support.google.com/mail/?p=RfcMessageNonCompliant and review\n5.7.1 RFC 5322 specifications. fi29-20020a056a00399d00b006cbe1bb5e3asm19494721pfb.138 - gsmtp')
# Looking at the snippet of your Python code, it seems that you're appending the string "Subject:Today's News" before every article in the body of your message. This would indeed create multiple subject lines when the message is compiled, which is not allowed in a properly formatted email.
#
# Here's how you should structure your email content:
#
# 1- The Subject should be set once and included in the email headers, not in the body of the email.
#
# 2- The body should contain the content of the email message, such as the articles' titles, descriptions, and URLs.






#If there is key error try this
# try:
#     for article in content.get("articles", [])[:20]:
#         if article.get("title") is not None:
#             body = "subject: Today's news" \
#                    + "\n" + body + article["title"] + "\n" \
#                    + article.get("description", "") \
#                    + "\n" + article.get("url", "") + 2 * "\n"
# except KeyError:
#     print("The 'articles' key was not found in the API response.")















#OUTPUT -- Check the receiver maid address if any email has been received.
#To create an app password:
# 1.Google account -- Security -- 2 step authentication -- App passwords -- Create a new one for this app
#  -- Paste it in the ppassword variable in the code

#Goto newsapi.org and visit documentation. Language is one of the parameters and en is used for english