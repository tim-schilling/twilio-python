# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class WebhookTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.webhooks().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://messaging.twilio.com/v1/Sessions/Webhooks',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "pre_webhook_url": "http://pre.url",
                "post_webhook_url": "http://post.url",
                "webhook_method": "GET",
                "webhook_filters": [
                    "onMessageSend",
                    "onSessionAdded"
                ],
                "pre_webhook_retry_count": 1,
                "post_webhook_retry_count": 2,
                "target": "http",
                "url": "https://messaging.twilio.com/v1/Sessions/Webhooks"
            }
            '''
        ))

        actual = self.client.messaging.v1.webhooks().fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.messaging.v1.webhooks().update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://messaging.twilio.com/v1/Sessions/Webhooks',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "pre_webhook_url": "http://pre.url",
                "post_webhook_url": "http://post.url",
                "webhook_method": "GET",
                "webhook_filters": [
                    "onSessionAdded"
                ],
                "pre_webhook_retry_count": 1,
                "post_webhook_retry_count": 2,
                "target": "flex",
                "url": "https://messaging.twilio.com/v1/Sessions/Webhooks"
            }
            '''
        ))

        actual = self.client.messaging.v1.webhooks().update()

        self.assertIsNotNone(actual)
