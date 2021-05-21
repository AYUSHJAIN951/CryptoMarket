import boto3
from botocore.exceptions import ClientError
import pandas as pd
# asdbh123b@
def sendemail(buy,sell,msg):
    RECIPIENTS=pd.read_csv("RECIPIENTS.csv")
    print(RECIPIENTS)
    for RECIPIENT in RECIPIENTS['Email']:
        print(RECIPIENT)
        # Replace sender@example.com with your "From" address.
        # This address must be verified with Amazon SES.
        SENDER = "cryptomarketupdater@gmail.com"

        # Replace recipient@example.com with a "To" address. If your account 
        # is still in the sandbox, this address must be verified.

        # Specify a configuration set. If you do not want to use a configuration
        # set, comment the following variable, and the 
        # ConfigurationSetName=CONFIGURATION_SET argument below.
        # CONFIGURATION_SET = "cryptomarketupdater"

        # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
        AWS_REGION = "us-east-1"

        # The subject line for the email.
        if(buy==1):
            SUBJECT = "ALERT!!! BUY!! BUY!!  CryptoMarket UPDATE"
        

        # The email body for recipients with non-HTML email clients.
            BODY_TEXT = (
                # "Amazon SES Test (Python)\r\n"
                #         "This email was sent with Amazon SES using the "
                #         "AWS SDK for Python (Boto)."

                        "A change is seen in the value \r\n"
                        " BUY BUY BUY"
                        "{msg}"
                        )
                        
            # The HTML body of the email.
            BODY_HTML = """<html>
            <head></head>
            <body>
            <h1>CRYPTO MARKET UPDATE </h1>
            BUY!! BUY!! BUY !!
            {msg}
            
     
            </body>
            </html>
                        """.format(msg=msg)              
        else:
            SUBJECT = "ALERT!!! SELL!! SELL!!  CryptoMarket UPDATE"
        

        # The email body for recipients with non-HTML email clients.
            BODY_TEXT = (
                # "Amazon SES Test (Python)\r\n"
                #         "This email was sent with Amazon SES using the "
                #         "AWS SDK for Python (Boto)."

                        "A change is seen in the value \r\n"
                        " SELL SELL SELL"
                        "{msg}"
                        )
                        
            # The HTML body of the email.
            BODY_HTML = """<html>
            <head></head>
            <body>
            <h1>CRYPTO MARKET UPDATE </h1>
            SELL!! SELL!! SELL !!
            <br>{msg}
    
            </body>
            </html>
                        """.format(msg=msg)        

        # The character encoding for the email.
        CHARSET = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=AWS_REGION)

        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                # ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])