import smtplib
import csv
from email.utils import make_msgid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

email_id = 'hultprize.ioe@pcampus.edu.np'
pswd = 'vecekwizbpuosbbh'

names=["Kopila Pant","Prajjwal budha chhetri","Prakriti Pandey","Samir Bikram Rakhal","Saurab Gyawali","Adhish Paudel","Prince Parajuli","Rakshyak Dhakal","Dipesh Singh","Resima Budhathoki","Sijal Jha","Taniya Yadav","Swastika Lamichhane","Tika Rijal","Pratyush Adhikari","Atharba Pal","Prastav Pandey","Sangam Ghimire","Animesh Dhakal","Shasank Wagle","Arden hang Samsohang","Nabina Thapa","Reazon Neupane","Shreyam Regmi"]
emails=["081bar013.kopila@pcampus.edu.np","079bel057.prajjwal@pcampus.edu.np","pandeyprakriti034@gmail.com","080bch037.samir@pcampus.edu.np","saurabgyawali77@gmail.com","081bel009.adhish@pcampus.edu.np", "pricneparajuli@gmail.com", "rakshyakdhakal@gmail.com","dipruc06@gmail.com","budhathokiresima@gmail.com","080bel082.sijal@pcampus.edu.np","080BEL092.taniya@pcampus.edu.np","081bce180.swastika@pcampus.edu.np","081bce182.tika@pcampus.edu.np","adhikaripratyush505@gmail.com","palatharba9@gmail.com","prastavpandey1@gmail.com","080bel073.sangam@pcampus.edu.np","081bei005.animesh@pcampus.edu.np","shasankwagle0@gmail.com","080bas011.arden@pcampus.edu.np","080bct047.nabina@pcampus.edu.np","reazon.np@gmail.com","shreyamregmi5@gmail.com"]


for i in range(24):
    eMail=emails[i]
    name=names[i]
    #role=roles[i]

    msg = MIMEMultipart()

    # html = '''\
    #     <!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #         <title>Interview Invitation - Hult Prize at IOE, Pulchowk Campus Organizing Committee 2025/26</title>
    #         <!-- Load Tailwind CSS CDN for styling -->
    #         <script src="https://cdn.tailwindcss.com"></script>
    #         <style>
    #             /* Fallback for email clients that may not support Tailwind CDN in production, 
    #             but provides a good visual structure here. */
    #             body {
    #                 font-family: 'Inter', sans-serif;
    #                 background-color: #f7f7f7;
    #                 margin: 0;
    #                 padding: 0;
    #             }
    #             /* Email clients often require specific width/centering setup */
    #             .email-container {
    #                 margin: 0 6px;
    #                 background-color: #ffffff;
    #                 box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    #             }
    #             /* Style for the Hult Prize Pink color */
    #             .hult-bg-pink {
    #                 background-color: #EC2088; /* Hult Prize Pink */
    #             }
    #             /* Button style (already uses pink via hult-bg-pink logic, but kept for clarity) */
    #             .btn-primary {
    #                 display: inline-block;
    #                 padding: 12px 24px;
    #                 background-color: #EC2088; /* Hult Prize Pink */
    #                 color: white;
    #                 border-radius: 8px;
    #                 text-decoration: none;
    #                 font-weight: 600;
    #             }

    #             /* Custom style for the mandatory alert block */
    #             .mandatory-alert {
    #                 background-color: #12B1E7; /* Bright Blue */
    #                 border-left: 4px solid #0F82A8; /* Darker shade for contrast */
    #                 padding: 16px;
    #             }
    #             .mandatory-alert p {
    #                 color: #000000; /* Changed text color to black for readability on light background */
    #             }
    #             .mandatory-alert .alert-title {
    #                 font-weight: 600;
    #                 font-size: 0.875rem; /* text-sm equivalent */
    #                 color: #000000; /* Ensure title is black */
    #             }
    #         </style>
    #     </head>
    #     <body class="bg-gray-100 p-4 sm:p-8">
    #         <!-- Email Container -->
    #         <div class="email-container rounded-xl shadow-lg my-8">
                
    #             <!-- Header Section -->
    #             <header class="hult-bg-pink p-6 rounded-t-xl">
    #                 <h1 class="text-xl font-bold text-white text-center tracking-wider" style="text-align: center; color: #ffffff;">HULT PRIZE at IOE, Pulchowk Campus</h1>
    #             </header>

    #             <!-- Body Content -->
    #             <main class="p-6 sm:p-10">
    #                 <h2 class="2xl font-semibold text-gray-800 mb-6 border-b pb-3">Interview Invitation for the Organizing Committee 2025/26</h2>

    #                 <p class="mb-4 text-gray-700">Dear %s,</p>

    #                 <p class="mb-6 text-gray-700">Thank courtesy for submitting your application for the Hult Prize at IOE, Pulchowk Campus Organizing Committee 2025/26. We appreciate the time and effort you invested in sharing your background and interest with us. We are pleased to inform you that your profile has been shortlisted for the next stage of our selection process: a formal interview.</p>

    #                 <!-- IMPORTANT MANDATORY REQUIREMENT BLOCK - Now using custom mandatory-alert class -->
    #                 <div class="mandatory-alert rounded-lg mb-6">
    #                     <p class="alert-title">MANDATORY SCHEDULING REQUIREMENT</p>
    #                     <p class="text-sm mt-1">
    #                         Please be advised that booking your interview time with at least a **one-hour advance notice is requisite** for your candidacy to be considered. Compliance with this stipulation is essential for your selection.
    #                     </p>
    #                     <p class="text-sm mt-2">
    #                         Furthermore, should you be unable to attend the scheduled interview, you must inform us within **twenty-four hours** of the original appointment time.
    #                     </p>
    #                 </div>
    #                 <!-- END IMPORTANT BLOCK -->

    #                 <p class="mb-6 text-gray-700">To proceed with scheduling your interview, please click the link below to access our booking portal:</p>

    #                 <!-- Call to Action Button -->
    #                 <div class="text-center my-8">
    #                     <a href="[LINK TO INTERVIEW BOOKING FORM]" target="_blank" class="btn-primary transform transition duration-300 hover:scale-105 hover:shadow-lg">
    #                         Book Your Interview Slot Now
    #                     </a>
    #                 </div>

    #                 <p class="mb-4 text-gray-700">We look forward to discussing your potential contributions to making the Hult Prize at IOE, Pulchowk Campus 2025/26 a resounding success.</p>
                    
    #                 <p class="text-gray-700 mt-8">Sincerely,</p>
    #                 <!-- Signature Block -->
    #                 <p class="font-semibold text-gray-800">Raunak Mishra</p>
    #                 <p class="text-sm text-gray-600">Campus Director<br>Hult Prize at IOE, Pulchowk Campus</p>
    #             </main>

    #             <!-- Footer Section -->
    #             <footer class="hult-bg-pink p-6 rounded-b-xl text-center text-xs text-white" style="text-align: center; color: #ffffff;">
    #                 <p class="mb-2">&copy; 2025/26 Hult Prize at IOE, Pulchowk Campus. All rights reserved.</p>
    #                 <p>If you have any queries, please reply to this email.</p>
    #             </footer>

    #         </div>
    #     </body>
    #     </html>

    #     ''' % (name)

    # html='''\
    #     <!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #         <meta charset="UTF-8">
    #         <meta name="viewport" content="width=device-width, initial-scale=1.0">
    #         <title>Selection Outcome - Hult Prize at IOE, Pulchowk Campus Organizing Committee 2025/26</title>
    #         <!-- Load Tailwind CSS CDN for styling -->
    #         <script src="https://cdn.tailwindcss.com"></script>
    #         <style>
    #             /* Fallback for email clients that may not support Tailwind CDN in production, 
    #             but provides a good visual structure here. */
    #             body {
    #                 font-family: 'Inter', sans-serif;
    #                 background-color: #f7f7f7;
    #                 margin: 0;
    #                 padding: 0;
    #             }
    #             /* Email clients often require specific width/centering setup */
    #             .email-container {
    #                 margin: 0 6px;
    #                 background-color: #ffffff;
    #                 box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    #             }
    #             /* Style for the Hult Prize Pink color */
    #             .hult-bg-pink {
    #                 background-color: #EC2088; /* Hult Prize Pink */
    #             }
    #             /* Button style */
    #             .btn-primary {
    #                 display: inline-block;
    #                 padding: 12px 24px;
    #                 background-color: #EC2088; /* Hult Prize Pink */
    #                 color: white;
    #                 border-radius: 8px;
    #                 text-decoration: none;
    #                 font-weight: 600;
    #             }

    #             /* Custom style for the mandatory alert block (Blue) */
    #             .mandatory-alert {
    #                 background-color: #12B1E7; /* Bright Blue */
    #                 border-left: 4px solid #0F82A8; /* Darker shade for contrast */
    #                 padding: 16px;
    #             }
    #             .mandatory-alert p {
    #                 color: #000000; /* Text color is black for readability on light blue */
    #             }
    #             .mandatory-alert .alert-title {
    #                 font-weight: 600;
    #                 font-size: 0.875rem; /* text-sm equivalent */
    #                 color: #000000;
    #             }
    #         </style>
    #     </head>
    #     <body class="bg-gray-100 p-4 sm:p-8">
    #         <!-- Email Container -->
    #         <div class="email-container rounded-xl shadow-lg my-8">
                
    #             <!-- Header Section -->
    #             <header class="hult-bg-pink p-6 rounded-t-xl" style="text-align:center; color: #ffffff;">
    #                 <h1 class="text-xl font-bold text-white text-center tracking-wider">HULT PRIZE at IOE, Pulchowk Campus</h1>
    #             </header>

    #             <!-- Body Content -->
    #             <main class="p-6 sm:p-10">
    #                 <h2 class="2xl font-semibold text-gray-800 mb-6 border-b pb-3" style="text-align: center;">Organizing Committee Selection Outcome 2025/26</h2>

    #                 <p class="mb-4 text-gray-700">Dear %s,</p>

    #                 <p class="mb-6 text-gray-700">We extend our gratitude for your participation in the Hult Prize at IOE, Pulchowk Campus Organizing Committee selection process. We received a tremendous number of highly qualified applicants, making the selection exceptionally competitive.</p>

    #                 <p class="mb-6 text-gray-700 font-semibold text-center text-lg p-3 border-2 border-dashed border-gray-300 rounded-lg">
    #                     The outcome of your application for the position of <span class="text-pink-600 font-extrabold"><b>%s</b></span> is: <br><span class="text-xl mt-2 block" style="color: #008000;"><b>ACCEPTED</b></span>
    #                 </p>

    #                 <!-- MANDATORY RESPONSE BLOCK (72 HOURS) -->
    #                 <div class="mandatory-alert rounded-lg mb-6">
    #                     <p class="alert-title text-base font-bold">MANDATORY ACCEPTANCE/REGRET CONFIRMATION</p>
    #                     <p class="mt-2">
    #                         As a requisite formality for concluding the selection, you are **required to reply to this email** within **72 hours** of receipt to officially confirm your decision (accepting or declining) or to acknowledge receipt of this notification.
    #                     </p>
    #                     <p class="mt-2 text-sm italic">
    #                         Failure to provide a timely response may result in the forfeiture of the offered position (if accepted) or conclusion of your candidacy.
    #                     </p>
    #                 </div>
    #                 <!-- END MANDATORY RESPONSE BLOCK -->

    #                 <p class="mb-4 text-gray-700">
    #                     Please ensure your reply is sent from the same email address used during the application process. We look forward to your response and potentially welcoming you to the team.
    #                 </p>
                    
    #                 <p class="text-gray-700 mt-8">Sincerely,</p>
    #                 <!-- Signature Block -->
    #                 <p class="font-semibold text-gray-800">Raunak Mishra</p>
    #                 <p class="text-sm text-gray-600">Campus Director<br>Hult Prize at IOE, Pulchowk Campus</p>
    #             </main>

    #             <!-- Footer Section -->
    #             <footer class="hult-bg-pink p-6 rounded-b-xl text-center text-xs text-white" style="text-align: center; color: #ffffff;">
    #                 <p class="mb-2">&copy; 2025/26 Hult Prize at IOE, Pulchowk Campus. All rights reserved.</p>
    #                 <p>If you have any queries, please reply to this email.</p>
    #             </footer>

    #         </div>
    #     </body>
    #     </html>

    #     ''' % (name, role)

    html=f'''\
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Selection Outcome - Hult Prize at IOE Organizing Committee 2025/26</title>
        </head>
        <body style="font-family: 'Inter', sans-serif; background-color: #f7f7f7; margin: 0; padding: 20px 0; line-height: 1.5;">
            <!-- Email Container (Max width 600px, centered, white background, shadow, rounded corners) -->
            <div class="email-container" style="margin: 0 6px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); border: 1px solid #e5e7eb;">
                
                <!-- Header Section (Hult Prize Pink) -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse;">
                    <tr>
                        <td align="center" style="background-color: #EC2088; padding: 24px; border-top-left-radius: 12px; border-top-right-radius: 12px;">
                            <h1 style="font-size: 20px; font-weight: 700; color: #ffffff; text-align: center; letter-spacing: 0.05em; margin: 0;">HULT PRIZE at IOE, Pulchowk Campus</h1>
                        </td>
                    </tr>
                </table>

                <!-- Body Content -->
                <div class="main-content" style="padding: 40px; color: #4b5563;">
                    <h2 style="font-size: 24px; font-weight: 700; color: #1f2937; margin-bottom: 24px; padding-bottom: 12px; text-align: center; border-bottom: 1px solid #e5e7eb; margin-top: 0;">Organizing Committee Selection Outcome 2025/26</h2>

                    <p style="margin-bottom: 16px;">Dear {name},</p>

                    <p style="margin-bottom: 24px;">On behalf of the Hult Prize at IOE, Pulchowk Campus, we sincerely thank you for your interest in the Organizing Committee for 2025/26. We appreciate the time you took to apply and participate in the interview process.</p>

                    <!-- REGRET BLOCK -->
                    <div class="regret-block" style="background-color: #fef2f2; border-left: 4px solid #EC2088; padding: 16px; color: #374151; border-radius: 8px; margin-bottom: 24px;">
                        <p style="font-weight: 700; font-size: 18px; color: #dc2626; margin-bottom: 8px; margin-top: 0;">Selection Outcome</p>
                        <p style="margin-bottom: 0;">
                            We regret to inform you that, after careful consideration of all candidates, we are unable to offer you a position on the Organizing Committee at this time.
                        </p>
                        <p style="margin-top: 12px; font-size: 14px; font-style: italic; margin-bottom: 0;">
                            This year, we received an unprecedented number of highly qualified applications, making the final selection extremely competitive. This decision reflects the limited number of positions available and not a lack of your qualifications or enthusiasm.
                        </p>
                    </div>
                    <!-- END REGRET BLOCK -->

                    <p style="margin-bottom: 16px;">
                        We genuinely value the passion you demonstrated for the Hult Prize mission. We strongly encourage you to remain involved by participating in the challenge itself and other upcoming Hult Prize events. Your ideas and energy are still essential to making this year a success!
                    </p>

                    <!-- Encouragement Button -->
                    <div style="text-align: center; margin-top: 32px; margin-bottom: 32px;">
                        <a href="https://discord.com/invite/Dereuy54de" target="_blank" style="display: inline-block; padding: 12px 24px; background-color: #f3f4f6; color: #EC2088; border: 2px solid #EC2088; border-radius: 8px; text-decoration: none; font-weight: 600; text-transform: uppercase;">
                            Stay Connected and Participate
                        </a>
                    </div>
                    
                    <p style="margin-top: 32px; margin-bottom: 16px;">We wish you the very best in your academic and professional pursuits.</p>
                    <!-- Signature Block -->
                    <p>Regards,</p>
                    <p style="font-weight: 600; color: #1f2937; margin-bottom: 4px; margin-top: 0;">Raunak Mishra</p>
                    <p style="font-size: 14px; color: #EC2088; margin: 0;">Campus Director<br>Hult Prize at IOE, Pulchowk Campus</p>
                </div>

                <!-- Footer Section (Hult Prize Pink) -->
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
