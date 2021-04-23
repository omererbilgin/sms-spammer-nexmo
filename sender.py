import nexmo

apikey = "82d4770b"  # nexmo api key

api_secret = "mgT4NNCwnIVAlwqp"  # nexmo api secret

sms_sender = "18885975336"  # place your sender name here

sms_text = open('body.txt', mode='r', encoding='utf-8').read().split('\n')  # place your sms text file here

phone_numbers = open('numbers.txt', mode='r',
                     encoding='utf-8').read().split('\n')  # phone number list file

change = 0
j = 0
limit = 3   # enter the body text refresh cycle 
	    # if you only have 1 body text this can be left as it is
initial = limit
lNum = 0 

for num in sms_text:
    lNum = lNum + 1

    if num == "":
       lNum = lNum - 1 
       break
   
print(lNum)

def sendText(sms, phone_number, body):
    response = sms.send_message({
        "from": sms_sender,
        "to": phone_number,
        "text": body
    })


if __name__ == "__main__":

    client = nexmo.Client(key=apikey, secret=api_secret)
    sms = nexmo.Sms(client)
    
    for number in phone_numbers:

        if number == "":
            continue
            
        if change >= limit:
            j = j + 1
            limit = limit + initial
        
        if j >= lNum:
            j = 0
        
        change = change + 1         
        body = sms_text[j]
        print("Sms sent to: {}\nBody text({}): {}\n\n".format(number, j, body))

        try:
            sendText(sms, number, body)
        except Exception as e:
            print("Failed to send sms")
            print(str(e))
