from twilio.rest import Client 
 
account_sid = 'AC54e2074bd401cf9675a8c795e83b63e8' 
auth_token = 'paste the auth_token here' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+14352016860',  
                              body='Yup it really worked!!! Btw it\'s me Ritik Seth :-)',      
                              to='+919587029168' 
                          ) 
 
print(message.sid)