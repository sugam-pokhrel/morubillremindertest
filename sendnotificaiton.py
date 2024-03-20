import smtplib
from pymongo import MongoClient
def sendEmail(name,amount,email):

      #using my own email and app password for testing
      s = smtplib.SMTP('smtp.gmail.com', 587)
      s.starttls()
      s.login("sugamf1@gmail.com", "jspsfvfizwgaewpo")
      subject = "Electricity Bill Reminder"
      body = f"""
              <html>
                  <head></head>
                  <body>
                      <p style="color: #333; font-size: 16px;">
                          Hello {name}, Your Total Amount is Rs:{amount}
                      </p>
                      <p style="color: #333; font-size: 16px;">
                          This is a reminder about your monthly electricity bill. Please ensure to make the payment on time to avoid any disruptions.
                      </p>
                      <p style="color: #333; font-size: 16px;">
                          If you've already paid the bill, please ignore this message. Otherwise, pay via Moru app right now.
                      </p>
                      <p style="color: #333; font-size: 16px;">
                          <a href="https://moru.com.np/home/nea?lang=en" style="color: #007BFF; text-decoration: none;">Pay Your Bill</a>
                      </p>
                  </body>
              </html> """
      message = f"Subject: {subject}\nMIME-Version: 1.0\nContent-Type: text/html\n\n{body}"
  
          # Send email to the specific user
      s.sendmail("sugamf1@gmail.com", email, message)
      s.quit()