import smtplib
from email.utils import make_msgid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

email_id = 'Your_email_id'
pswd = 'Your_Password'

names=["List Item 1"]
emails=["listitem1@gmail.com"]


for i in range(24):
    eMail=emails[i]
    name=names[i]
    #role=roles[i]

    msg = MIMEMultipart()

    html=f'''\
        <!DOCTYPE html>
        <html lang="en">
           ftyui;jobjhvgc
                <!-- Footer Section -->
                <footer style="background-color: #EC2088; padding: 24px; border-bottom-left-radius: 12px; border-bottom-right-radius: 12px; text-align: center; font-size: 12px; color: #ffffff;">
                    <p style="margin-bottom: 8px; margin-top: 0;">&copy; 2025/26 Hult Prize at IOE, Pulchowk Campus. All rights reserved.</p>
                    <p style="margin-bottom: 0;">If you have any queries, please reply to this email.</p>
                </footer>

            </div>
        </body>
        </html>
        '''

    content = ""

    msg['Subject'] = 'Selection Outcome - Hult Prize at IOE, Pulchowk Campus Organizing Committee 2025/26'
    msg['From'] = email_id
    msg['To'] = eMail
    part = MIMEText(html, "html")
    msg.attach(part)

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)
    msgText = MIMEText('<p style="color:#ffffff; background-color: #EC2088; text-align: center; margin: 0 6px;"><b>Follow us on:</b><br><a href="https://www.facebook.com/HultatIOE"><img width="35" height="35" src="cid:image_fb"></a>  <a href="https://www.instagram.com/hultatioe/"><img width="35" height="35" src="cid:image_ig"></a>   <a href="https://www.linkedin.com/company/hult-prize-at-ioe-pulchowk-campus/"><img width="35" height="35" src="cid:image_ln"></a></p>', 'html')
    msgAlternative.attach(msgText)
    #Attach Images
    fp1 = open('D://Innovation//Portfolio Pull request//v2.O//assets//images//facebook-logo.png','rb')  # Read image
    msgImage1 = MIMEImage(fp1.read())
    fp1.close()
    msgImage1.add_header('Content-ID', '<image_fb>')
    msg.attach(msgImage1)
    fp2 = open('D://Innovation//Portfolio Pull request//v2.O//assets//images//instagram-logo.png','rb')  # Read image
    msgImage2 = MIMEImage(fp2.read())
    fp2.close()
    msgImage2.add_header('Content-ID', '<image_ig>')
    msg.attach(msgImage2)
    fp4 = open('D://Innovation//Portfolio Pull request//v2.O//assets//images//linkedin-logo.png','rb')  # Read image
    msgImage4 = MIMEImage(fp4.read())
    fp4.close()
    msgImage4.add_header('Content-ID', '<image_ln>')
    msg.attach(msgImage4)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, pswd)
        smtp.sendmail(email_id, eMail, msg.as_string())
        smtp.quit()
        del msg['To']
        del eMail
        print("Email sent successfully...")

