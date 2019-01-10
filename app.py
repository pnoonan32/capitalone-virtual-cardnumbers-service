import tweepy
import requests
import json

# customerId = '5c34b800322fa06b677942fa'
# apiKey = '6f4d4a5b2db171dcf82d90f69a685fd9'

# url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
# payload = {
#   "type": "Savings",
#   "nickname": "test",
#   "rewards": 10000,
#   "balance": 10000,	
# }
# # Create a Savings Account
# response = requests.post( 
# 	url, 
# 	data=json.dumps(payload),
# 	headers={'content-type':'application/json'},
# 	)

# if response.status_code == 201:
# 	print('account created')


"""
Requires apiKey and the customerId to create an(other) account for that customer
"""
def create_account():
    customer_id = '5c34b800322fa06b677942fa'
    api_key = '6f4d4a5b2db171dcf82d90f69a685fd9'
    url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_id,api_key)

    payload = {
        "type": "Savings",
        "nickname": "test",
        "rewards": 10000,
        "balance": 10000,	
    }

    response = requests.post( 
 	url, 
 	data=json.dumps(payload),
 	headers={'content-type':'application/json'},
    )

    if response.status_code == 201:
        return(response.content)
    else:
        return('Error: Account could not be made!')


"""
Get accounts by customer id
"""
def return_customer_with_customerid():
    customer_id = '5c34b800322fa06b677942fa'
    api_key = '6f4d4a5b2db171dcf82d90f69a685fd9'
    url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_id,api_key)
    
    response = requests.get( 
	    url,
	    headers={'content-type':'application/json'},
)

    if response.status_code == 200:
	    return(response.content)
    else: 
        return('Failed to retreive account information!')



def add_new_customer():
    api_key = '6f4d4a5b2db171dcf82d90f69a685fd9'
    url = 'http://api.reimaginebanking.com/customers?key={}'.format(api_key)

    payload = {
  "first_name": "Steve",
  "last_name": "Jobs",
  "address": {
    "street_number": "21",
    "street_name": "Majestic Lane",
    "city": "Honolulu",
    "state": "HI",
    "zip": "96795"
  }
}
    response = requests.post( 
 	url, 
 	data=json.dumps(payload),
 	headers={'content-type':'application/json'},
    )

    if response.status_code == 201:
        return('New Customer was created: {}'.format(response.content))
    else:
        return('Error: New Customer could not be added!')

def main():
    #Declare functions as variables
    creating_account = create_account()
    return_customer = return_customer_with_customerid()
    add_customer = add_new_customer()

    return {
        'Creating an account': creating_account,
        'Fetching an account': return_customer,
        'Add new customer': add_customer
    }



if __name__ == "__main__":
    x = main()
    






        # super(CLASS_NAME, self).__init__(*args, **kwargs)
        
