import virtualcardnumbers
from virtualcardnumbers import *
from models import *

setup_oauth_with_token('https://api-sandbox.capitalone.com',  "eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwicGNrIjoxLCJhbGciOiJkaXIiLCJ0diI6Miwia2lkIjoicjRxIn0..mNskdJSXGmGLb8GN9qeoYg.nmhblQl_29gfWEYkRz685BGGos-OWtZk9zuykpMe_VVucSTMqNzr3Oo3ZdEL1xsXjwhW8w-iW9JuvihPXY3amEoiw80NGGhFQ37YQUSfejYGfvyDBUs8XVYeQt7x9qYfqeR_aF1ORhhW0-smHyBIE5MTOhpfEQHCq4hW7_qIc3WuF4aP0lDOj6nm3dwKIuthsFPv2NpAGGPFB7CcItDYkObNIHEfciX_1_eX81w6prHR_8c1GyW1MDaPZzeZSiqf8jshCsHc2ab7ftZwfi99pwterMMJWGdbnh1Yhf5zSNCs2mZ3WIZrAAxTX0qdr7LKDPkNflNefK0QdD_E8WNpMq87Kp894M7ZLwv3Tx4_87hlzJjf6apVf9giK1JA2S-llr-qrvuFUwhEF_wOcSb3GQDb0ExRS2qq9S3AuGmPdGsZjE_I4B8Lf43MWMf1tlnORWQ1OBhZjnKHyOnomBlCYEIcjfhFwGjSgatzW1_kN_WYUwvS7xSrW7SKOmOnJHfuVFtQ0mUyUwwjFlSMekWSDg.-1PBfPIwrYJCJCCCnZKuEQ")

base_url = 'https://api-sandbox.capitalone.com'
client_id = '83c59ee7d6a4479c8e142422cbe9022a'
client_secret = '6d5c0077c6d4e214c6850d5f1611689e'
auth_code = '64b68355715141feb23ae6048fc3c47f'

# virtualcardnumbers.setup_oauth_3legged(base_url, client_id, client_secret, auth_code)

# POST /payment-services/create-customer-virtual-card

customer_virtual_card = create_customer_virtual_card()

get_virtual_card = retrieve_virtual_card_details('UNYX+LmwrgBYGUut5nliFOezJW2I6ZLDlxlcLAm2gtZznmdsOV7Q=')

def main():
    # print(customer_virtual_card)
    print(get_virtual_card)

    

if __name__ == "__main__":
    main()