# Virtual Card Numbers

## Setup

This code sample is a Python client implementation that includes a unit test. Use the unit test to test our client implementation, and refer to the [Sample usage code](#sample-usage-code) we've provided to invoke the client implementation from your code base.

### Requirements

You must have these installed:

* Python 3.6.3 or greater
* ```pyjwkest```. To install, run ```pip3 install pyjwkest --trusted-host pypi.python.org```.

### Using the unit test and client implementation

Virtual Card Numbers API has 4 operation of which ```Create virtual card``` uses the authorization code (3-legged) OAuth flow. ```Replace physical card```, ```Retrieve virtual card details``` and ```Report merchant activity``` use client credentials (2-legged) OAuth flow.

We've provided a unit test that includes a set of assertions to make sure you're getting the right responses.

### Authorization Code (3-legged) OAuth Flow 
To run the unit test:

* add `"iat"` and `"jti"` to the list of args in ```<Path to Python Installation>/Versions/3.6/lib/python3.6/site-packages/jwkwest/jwe.py``` (lines 481, 730) and ```<Path to Python Installation>/Versions/3.6/lib/python3.6/site-packages/jwkest/jws.py``` (line 245)
* add the encryption and signing keys we've provided in [Encrypting and decrypting sensitive information](https://capitalone-devexchange.github.io/api-products/virtual-card-numbers/documentation/#_encrypting_and_decrypting_sensitive_information) to the appropriate ```certs``` files -- ```Decrypt-PrivateKey.pem```, ```Encrypt-PrivateKey.pem```, ```Sign-PrivateKey.pem```, and ```Verify-PublicKey.pem```
* add the ```base_url```, ```client_id```, ```client_secret```, and ```auth_code``` to the ```virtualcardnumbers_3legged_test.py``` file. Use ```https://api-sandbox.capitalone.com``` as your ```base_url```, and you'll find the ```client_id``` and ```auth_code``` in [Credentials and tokens](https://capitalone-devexchange.github.io/api-products/virtual-card-numbers/documentation/#_credentials_and_tokens). For ```auth_code```, complete [Authorization Code Auth Flow](https://capitalone-devexchange.github.io/documentation/api-products/virtual-card-numbers/documentation/index.html#_the_authorization_code_flow)
* type ```python3 -m unittest virtualcardnumbers_3legged_test.py``` on the command line

### Client Credentials (2-legged) OAuth Flow
To run the unit test:

* add `"iat"` and `"jti"` to the list of args in ```<Path to Python Installation>/Versions/3.6/lib/python3.6/site-packages/jwkwest/jwe.py``` (lines 481, 730) and ```<Path to Python Installation>/Versions/3.6/lib/python3.6/site-packages/jwkest/jws.py``` (line 245)
* add the encryption and signing keys we've provided in [Encrypting and decrypting sensitive information](https://capitalone-devexchange.github.io/api-products/virtual-card-numbers/documentation/#_encrypting_and_decrypting_sensitive_information) to the appropriate ```certs``` files -- ```Decrypt-PrivateKey.pem```, ```Encrypt-PrivateKey.pem```, ```Sign-PrivateKey.pem```, and ```Verify-PublicKey.pem```
* add the ```base_url```, ```client_id```, and ```client_secret``` to the ```virtualcardnumbers_2legged_test.py``` file. Use ```https://api-sandbox.capitalone.com``` as your ```base_url```, and you'll find the ```client_id``` and ```auth_code``` in [Credentials and tokens](https://capitalone-devexchange.github.io/api-products/virtual-card-numbers/documentation/#_credentials_and_tokens)
* type ```python3 -m unittest virtualcardnumbers_2legged_test.py``` on the command line

You can play around with the values you provide and the responses you retrieve; simply edit the data in the ```virtualcardnumbers_2legged_test.py``` file. Note that only our sandbox data will return a success response.

To run the client implementation without using the unit test, use the [Sample usage code](#sample-usage-code) shown below and complete this step:

* add the encryption and signing keys we've provided in [Encrypting and decrypting sensitive information](https://capitalone-devexchange.github.io/api-products/virtual-card-numbers/documentation/#_encrypting_and_decrypting_sensitive_information) to the appropriate ```certs``` files -- ```Decrypt-PrivateKey.pem```, ```Encrypt-PrivateKey.pem```, ```Sign-PrivateKey.pem```, and ```Verify-PublicKey.pem```

You can also check out the other code samples we've provided:

* [Java](https://github.com/CapitalOne-DevExchange/VirtualCardNumbers-Example-Java)

* [Javascript](https://github.com/CapitalOne-DevExchange/VirtualCardNumbers-Example-Javascript)

## Sample usage code

### Authorization Code (3-legged) OAuth Flow 
To use our client implementation from your own code, you'll need something like what's shown here. Use ```https://api-sandbox.capitalone.com``` as your ```base_url```, and you'll find the ```client_id``` and ```auth_code``` in [Credentials and tokens](https://capitalone-devexchange.github.io/api-products/virtual-card-numbers/documentation/#_credentials_and_tokens), and ```auth_code``` after completing [Authorization OAuth Flow](https://capitalone-devexchange.github.io/api-products/virtual-card-numbers/documentation/index.html#_the_authorization_code_flow):

```python
import virtualcardnumbers
from models import *

base_url = ... # Capital One sandbox URL
client_id = ... # Client Id of the registered app at developer.capitalone.com
client_secret = ... # Client Secret of the registered app at developer.capitalone.com
auth_code = ... # Authorization Code

virtualcardnumbers.setup_oauth_3legged(client_id, client_secret, base_url, auth_code)

# POST /payment-services/create-customer-virtual-card
customer_virtual_card = virtualcardnumbers.create_customer_virtual_card()
```

### Client Credentials (2-legged) OAuth Flow
To use our client implementation from your own code, you'll need something like what's shown here. Use ```https://api-sandbox.capitalone.com``` as your ```base_url```, and you'll find the ```client_id``` and ```auth_code``` in [Credentials and tokens](https://capitalone-devexchange.github.io/api-products/virtual-card-numbers/documentation/#_credentials_and_tokens):

```python
import virtualcardnumbers
from models import *

base_url = ... # Capital One sandbox URL
client_id = ... # Client Id of the registered app at developer.capitalone.com
client_secret = ... # Client Secret of the registered app at developer.capitalone.com

virtualcardnumbers.setup_oauth_2legged(client_id, client_secret, base_url)

# POST /payment-services/virtual-cards
virtual_card_request = VirtualCardRequest()

billing_address = BillingAddress()
billing_address.addressLine1 = "789 BREEZY LANE"
billing_address.city = "SAN FRANCISCO"
billing_address.postalCode = "95187"
billing_address.stateCode = "CA"
billing_address.countryCode = "USA"

physical_card_details = PhysicalCardDetails()
physical_card_details.cardholderName = "LEE CARDHOLDER"
physical_card_details.cardNumber = "4266929827109461"
physical_card_details.expirationDate = "2020-10"
physical_card_details.billingAddress = billing_address

virtual_card_request.authenticationType = AuthenticationType.PASSWORD.value
virtual_card_request.physicalCardDetails = physical_card_details

virtual_card_response = virtualcardnumbers.replace_virtual_card(virtual_card_request)

# GET /payment-services/virtual-cards/{virtualCardReferenceId}
virtual_card_details = virtualcardnumbers.retrieve_virtual_card_details(virtual_card_response["virtualCardReferenceId"])

# POST /payment-services/virtual-cards/{virtualCardReferenceId}/merchant-activities
merchant_activity = MerchantActivity()
merchant_activity.activityCode = ActivityCode.VIRTUALCARDONFILE.value
merchant_activity.activityDetails = "New customer"

virtualcardnumbers.report_mechant_activity(virtual_card_response["virtualCardReferenceId"], merchant_activity)
```

## Licence

[MIT License](https://github.com/CapitalOne-DevExchange/VirtualCardNumbers-Example-Python/blob/master/LICENSE)