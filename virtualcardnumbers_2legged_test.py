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

import virtualcardnumbers, unittest
from models import *


class VirtualCardNumbers2LeggedTest(unittest.TestCase):
    def test_virtualcardnumbers_2legged(self):

        # base_url = ... # Capital One Sandbox URL
        # client_id = ... # Client Id of the registered app at developer.capitalone.com
        # client_secret = ... # Client Secret of the registered app at developer.capitalone.com

        virtualcardnumbers.setup_oauth_2legged(base_url, client_id, client_secret)

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
        self.assertEqual("UNYX+LmwrgBYGUut5nliFOezJW2I6ZLDlxlcLAm2gtZznmdsOV7Q=",
                         virtual_card_response["virtualCardReferenceId"])

        # GET /payment-services/virtual-cards/{virtualCardReferenceId}
        virtual_card_details = virtualcardnumbers.retrieve_virtual_card_details(
            virtual_card_response["virtualCardReferenceId"])
        self.assertEqual("UNYX+LmwrgBYGUut5nliFOezJW2I6ZLDlxlcLAm2gtZznmdsOV7Q=",
                         virtual_card_details["virtualCardReferenceId"])

        # POST /payment-services/virtual-cards/{virtualCardReferenceId}/merchant-activities
        merchant_activity = MerchantActivity()
        merchant_activity.activityCode = ActivityCode.VIRTUALCARDONFILE.value
        merchant_activity.activityDetails = "New customer"

        virtualcardnumbers.report_mechant_activity(virtual_card_response["virtualCardReferenceId"], merchant_activity)


if __name__ == '__main__':
    unittest.main()
