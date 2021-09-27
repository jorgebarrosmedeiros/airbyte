#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from typing import Any, List, Mapping, Tuple

import stripe
from airbyte_cdk import AirbyteLogger
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.sources.streams.http.auth import TokenAuthenticator
from source_stripe.streams import (
    BalanceTransactions,
    BankAccounts,
    Charges,
    Coupons,
    CustomerBalanceTransactions,
    Customers,
    Disputes,
    Events,
    InvoiceItems,
    InvoiceLineItems,
    Invoices,
    PaymentIntents,
    Payouts,
    Plans,
    Products,
    Refunds,
    SubscriptionItems,
    Subscriptions,
    Transfers,
)


class SourceStripe(AbstractSource):
    def check_connection(self, logger: AirbyteLogger, config: Mapping[str, Any]) -> Tuple[bool, Any]:
        try:
            stripe.api_key = config["client_secret"]
            stripe.Account.retrieve(config["account_id"])
            return True, None
        except Exception as e:
            return False, e

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        authenticator = TokenAuthenticator(config["client_secret"])
        args = {"authenticator": authenticator, "account_id": config["account_id"]}
        return [
            BalanceTransactions(**args),
            BankAccounts(**args),
            Charges(**args),
            Coupons(**args),
            CustomerBalanceTransactions(**args),
            Customers(**args),
            Disputes(**args),
            Events(**args),
            InvoiceItems(**args),
            InvoiceLineItems(**args),
            Invoices(**args),
            PaymentIntents(**args),
            Payouts(**args),
            Plans(**args),
            Products(**args),
            Refunds(**args),
            SubscriptionItems(**args),
            Subscriptions(**args),
            Transfers(**args),
        ]
