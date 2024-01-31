import requests
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate, COMMASPACE
from email import encoders
from datetime import date
import os
import time

def fetch_and_send_property_data():
    """
    Fetches property data from the Property Finder API, processes it, and sends out email reports.
    """
    try:
        # Dummy data for demonstration
        EMAIL_PW = "your_email_password"
        PF_TOKEN = "your_property_finder_token"

        # Dummy base URL for the Property Finder API
        BASE_URL = 'https://api.example.com/properties?per_page=100&page={page}&fields=id,reference,price,user,status,location,created_at,updated_at,import,state,type,marked_as_seen,publication,bedrooms,bathrooms,size,languages,images,furnished,landlord,available_from,charges,parking,amenities,unit_number,developer,metadata,hash,quality_score,licenses,freehold,build_year,plot_size,built_up_area,floors,occupancy,renovation,project_status,financial_status,transaction,listing_level,verifications,duplicated_list,furnished,listing_status,listing_expiry_date,rega_permit,listing_auto_renew,is_cts_available,is_cts_prioritized&filters[has_publication]=1&filters[portal]=propertyfinder&sort=updated&sort_order=desc'

        def send_email(from_address, to_address, cc_addresses, subject, message, attachment_path=None):
            """
            Sends an email with attachment if provided.
            """
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Cc'] = ", ".join(cc_addresses)
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = subject
            msg.attach(MIMEText(message))

            # Attach the file if provided
            if attachment_path:
                with open(attachment_path, "rb") as file:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(attachment_path)}")
                msg.attach(part)

            # Connect to the SMTP server and send the email
            smtp_server = smtplib.SMTP('smtp.example.com', 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(from_address, EMAIL_PW)
            recipient_list = [to_address] + cc_addresses
            smtp_server.sendmail(from_address, recipient_list, msg.as_string())
            smtp_server.close()

        # Fetch property data from the API
        properties = []
        total_pages = 5  # Dummy total pages for demonstration
        for i in range(1, total_pages+1):
            request_url = BASE_URL.replace('{page}', str(i))
            res = requests.get(request_url)
            if res.status_code == 200:
                res_data = res.json()
                for prop in res_data["properties"]:
                    property = {}
                    # Extract property information
                    # Dummy property data extraction code
                    properties.append(property)

        df = pd.DataFrame(properties)
        if not df.empty:
            # Send success email with property data attached
            send_email("sender@example.com", "recipient@example.com", ["cc1@example.com", "cc2@example.com"],
                       "Property Finder Data Report", "Dear Recipient,\n\nPlease find the Property Finder Daily Report attached with this email.\n\nThanks,\n\nYour Name",
                       attachment_path="Properties.xlsx")
            df.to_excel("Properties.xlsx", index=False)
        else:
            # Send email notification for unsuccessful operation
            send_email("sender@example.com", "recipient@example.com", [],
                       "Error in Property Finder Reporting Script", "Something went wrong in fetching Property Finder Data. Please check.\n\nThis is an auto-generated email.")

    except Exception as e:
        # Handle any exceptions and send email notification
        print(f"Error: {e}")
        send_email("sender@example.com", "recipient@example.com", [],
                   "Error in Property Finder Reporting Script", "An error occurred while executing the script. Please check the logs for details.\n\nThis is an auto-generated email.")


# Call the function to execute the script
fetch_and_send_property_data()
