# -*- coding: utf-8 -*-
import fido.exceptions
import twisted.internet.error
import twisted.web.client

from bravado.fido_client import FidoClient
from bravado.fido_client import FidoFutureAdapter
from bravado.testing.integration_test import IntegrationTestsBaseClass


class TestServerFidoClient(IntegrationTestsBaseClass):

    http_client_type = FidoClient
    http_future_adapter_type = FidoFutureAdapter
    connection_errors_exceptions = {
        fido.exceptions.TCPConnectionError(),
        twisted.internet.error.ConnectingCancelledError('address'),
        twisted.internet.error.DNSLookupError(),
        twisted.web.client.RequestNotSent(),
    }

    @classmethod
    def encode_expected_response(cls, response):
        return response

    def cancel_http_future(self, http_future):
        http_future.future._eventual_result.cancel()
