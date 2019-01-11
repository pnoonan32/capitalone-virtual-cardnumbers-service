#
# SPDX-Copyright: Copyright 2018 Capital One Services, LLC
# SPDX-License-Identifier: MIT
# Copyright 2018 Capital One Services, LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do so, subject to the
# following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
# OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

import requests, time, uuid, json
from models import JWSRequest
from jwkest.jwe import JWE
from jwkest.jwk import RSAKey
from jwkest.jws import JWS

OAUTH_ENDPOINT = "/oauth2/token"
PAYMENT_SERVICES = "/payment-services"
CREATE_CUSTOMER_VIRTUAL_CARD = "/create-customer-virtual-card"
VIRTUAL_CARDS = "/virtual-cards"
MERCHANT_ACTIVITIES = "/merchant-activities"

signing_keys = [RSAKey(use="sig").load('certs/Sign-PrivateKey.pem')]
verifying_keys = [RSAKey(use="sig").load('certs/Verify-PublicKey.pem')]
encryption_keys = [RSAKey(use="enc").load('certs/Encrypt-PublicKey.pem')]
decryption_keys = [RSAKey(use="enc").load('certs/Decrypt-PrivateKey.pem')]

def setup_oauth_with_token(base_url, token):
    global CAPITAL_ONE_SANDBOX
    CAPITAL_ONE_SANDBOX = base_url

    global ACCESS_TOKEN
    ACCESS_TOKEN = "Bearer" + ' ' + token

def setup_oauth(base_url, payload):
    global CAPITAL_ONE_SANDBOX
    CAPITAL_ONE_SANDBOX = base_url
    oauth_headers = {
        'Accept': "application/json",
        'Content-Type': "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post(CAPITAL_ONE_SANDBOX + OAUTH_ENDPOINT, data=payload, headers=oauth_headers)
        response.raise_for_status()
        json_response = response.json()

        global ACCESS_TOKEN
        ACCESS_TOKEN = json_response['token_type'] + ' ' + json_response['access_token']
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def setup_oauth_2legged(base_url, client_id, client_secret):
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    setup_oauth(base_url, payload)


def setup_oauth_3legged(base_url, client_id, client_secret, auth_code):
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "authorization_code",
        "code": auth_code
    }
    setup_oauth(base_url, payload)


def create_customer_virtual_card():
    url = CAPITAL_ONE_SANDBOX + PAYMENT_SERVICES + CREATE_CUSTOMER_VIRTUAL_CARD
    api_headers = {
        'Accept': 'application/jwt;v=0',
        'Authorization': ACCESS_TOKEN
    }
    try:
        response = requests.post(url, headers=api_headers)
        response.raise_for_status()
        print("Create Customer Virtual Card: Success:")
        return decrypt(response.content)
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def replace_virtual_card(virtual_card_request):
    url = CAPITAL_ONE_SANDBOX + PAYMENT_SERVICES + VIRTUAL_CARDS
    api_headers = {
        'Accept': 'application/jwt;v=0',
        'Content-Type': 'application/jwt',
        'Authorization': ACCESS_TOKEN
    }
    try:
        response = requests.post(url, data=encrypt(virtual_card_request), headers=api_headers)
        response.raise_for_status()
        print("Replace Virtual Card: Success")
        return decrypt(response.content)
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def retrieve_virtual_card_details(virtual_card_reference_id):
    url = CAPITAL_ONE_SANDBOX + PAYMENT_SERVICES + VIRTUAL_CARDS + "/" + virtual_card_reference_id
    api_headers = {
        'Accept': 'application/jwt;v=0',
        'Authorization': ACCESS_TOKEN
    }
    try:
        response = requests.get(url, headers=api_headers)
        response.raise_for_status()
        print("Retrieve Virtual Card Details: Success")
        return decrypt(response.content)
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def report_mechant_activity(virtual_card_reference_id, merchant_activity):
    url = CAPITAL_ONE_SANDBOX + PAYMENT_SERVICES + VIRTUAL_CARDS + "/" + virtual_card_reference_id + MERCHANT_ACTIVITIES
    api_headers = {
        'Accept': 'application/json;v=0',
        'Content-Type': 'application/json',
        'Authorization': ACCESS_TOKEN
    }
    try:
        response = requests.post(url, json=merchant_activity.__dict__, headers=api_headers)
        response.raise_for_status()
        print("Report Merchant Activity: Success")
    except requests.exceptions.HTTPError as error:
        print(error, "\n", response.json())


def encrypt(request):
    jws_request = JWSRequest()
    jws_request.iss = "https://merchantname.com"
    jws_request.aud = "https://capitalone.com"
    jws_request.payload = json.dumps(request, default=lambda x: x.__dict__)

    jws = JWS(json.dumps(jws_request, default=lambda x: x.__dict__), alg="RS256")
    signed_content = jws.sign_compact(keys=signing_keys)
    jwe = JWE(signed_content, alg="RSA-OAEP-256", enc="A256GCM", iat=int(round(time.time() * 1000)), jti=str(uuid.uuid4()))
    return jwe.encrypt(keys=encryption_keys)


def decrypt(request):
    decrypted_content = JWE().decrypt(request, keys=decryption_keys)
    response = JWS().verify_compact(decrypted_content, keys=verifying_keys)
    return json.loads(response["payload"])