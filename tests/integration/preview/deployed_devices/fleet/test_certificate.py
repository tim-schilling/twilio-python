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


class CertificateTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .certificates(sid="CYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Certificates/CYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "CYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "fleet_sid": "FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "device_sid": "THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "thumbprint": "1234567890",
                "date_created": "2016-07-30T20:00:00Z",
                "date_updated": null,
                "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Certificates/CYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .certificates(sid="CYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .certificates(sid="CYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Certificates/CYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .certificates(sid="CYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .certificates.create(certificate_data="certificate_data")

        values = {'CertificateData': "certificate_data", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Certificates',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "CYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "fleet_sid": "FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "device_sid": "THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "thumbprint": "1234567890",
                "date_created": "2016-07-30T20:00:00Z",
                "date_updated": null,
                "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Certificates/CYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .certificates.create(certificate_data="certificate_data")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .certificates.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Certificates',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "certificates": [],
                "meta": {
                    "first_page_url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Certificates?PageSize=50&Page=0",
                    "key": "certificates",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Certificates?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .certificates.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "certificates": [
                    {
                        "sid": "CYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "friendly_name",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "fleet_sid": "FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "device_sid": "THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "thumbprint": "1234567890",
                        "date_created": "2016-07-30T20:00:00Z",
                        "date_updated": null,
                        "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Certificates/CYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Certificates?PageSize=50&Page=0",
                    "key": "certificates",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Certificates?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .certificates.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                .certificates(sid="CYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/DeployedDevices/Fleets/FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Certificates/CYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "CYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "fleet_sid": "FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "device_sid": "THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "thumbprint": "1234567890",
                "date_created": "2016-07-30T20:00:00Z",
                "date_updated": "2016-07-30T20:00:00Z",
                "url": "https://preview.twilio.com/DeployedDevices/Fleets/FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Certificates/CYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.deployed_devices.fleets(sid="FLXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                                     .certificates(sid="CYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
