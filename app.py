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
    customer_id = '5c37af24b8e2a665da3ded43'
    api_key = '6f4d4a5b2db171dcf82d90f69a685fd9'
    url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer_id,api_key)

    payload = {
        "type": "Credit Card",
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



def create_new_transfer():
    account_id = '5c37f6a4b8e2a665da3eb5e4'
    api_key = '6f4d4a5b2db171dcf82d90f69a685fd9'
    url = 'http://api.reimaginebanking.com/accounts/{}/transfers?key={}'.format(account_id, api_key)

    payload = {
  "medium": "balance",
  "payee_id": "5c34b803322fa06b677942fd",
"amount": 78,
  "transaction_date": "2019-01-10",
  "status": "pending",
  "description": "Capital One cashback"
}

    response = requests.post( 
 	url, 
 	data=json.dumps(payload),
 	headers={'content-type':'application/json'},
    )

    if response.status_code == 201:
        return('The transfer was created: {}'.format(response.content))
    else:
        return('Error: Transfer was unsuccessful!')

def main():
    #Declare functions as variables
    creating_account = create_account()
    return_customer = return_customer_with_customerid()
    add_customer = add_new_customer()
    create_transfer = create_new_transfer()

    return {
        'Creating an account': creating_account,
        'Fetching an account': return_customer,
        'Add new customer': add_customer,
        'Create Transfer': create_transfer
    }



if __name__ == "__main__":
    x = main()
    






        # super(CLASS_NAME, self).__init__(*args, **kwargs)
        
