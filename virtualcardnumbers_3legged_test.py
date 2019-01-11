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


class VirtualCardNumbers3LeggedTest(unittest.TestCase):
    def test_virtualcardnumbers_3legged(self):

        # base_url = ... # Capital One Sandbox URL
        # client_id = ... # Client Id of the registered app at developer.capitalone.com
        # client_secret = ... # Client Secret of the registered app at developer.capitalone.com
        # auth_code = ... // Authorization Code

        virtualcardnumbers.setup_oauth_3legged(base_url, client_id, client_secret, auth_code)

        # POST /payment-services/create-customer-virtual-card
        customer_virtual_card = virtualcardnumbers.create_customer_virtual_card()
        self.assertEqual("UNYX+LmwrgBYGUut5nliFOezJW2I6ZLDlxlcLAm2gtZznmdsOV7Q=",
                         customer_virtual_card["virtualCardReferenceId"])


if __name__ == '__main__':
    unittest.main()
