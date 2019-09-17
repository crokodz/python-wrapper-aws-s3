"""Tests for pyqalxapi.api."""

import unittest
import pyqalxapi
from unittest.mock import patch

api = pyqalxapi.API(token='1234567890')

class APITestCase(unittest.TestCase):
    @patch('pyqalxapi.request.requests.request')
    def test_get_item_request(self, mocked_request):
        resp = api.get('item')
        self.assertTrue(mocked_request.called)

    @patch('pyqalxapi.request.requests.request')
    def test_get_item_by_id_request(self, mocked_request):
        resp = api.get('item', guid='494b775f-7c95-437b-9989-1c9b730ea67e')
        self.assertIn('https://api.qalx.io/item',
            mocked_request.call_args[1]['url'])
        self.assertTrue(mocked_request.called)

    @patch('pyqalxapi.request.requests.request')
    def test_post_item_request(self, mocked_request):
        resp = api.post('item', data={'a':'b'})
        self.assertIn('a', mocked_request.call_args[1]['json']['data'])
        self.assertTrue(mocked_request.called)


    @patch('pyqalxapi.request.requests.request')
    def test_post_item_file_request_failed(self, mocked_request):
        resp = api.post('item', data={'a':'b'}, file='../pyqalx/requirements.txt')
        self.assertTrue(mocked_request.called)

    @patch('pyqalxapi.API.upload_to_s3')
    def test_post_item_file_request(self, mocked_upload_to_s3):
        resp = api.post('item', file='')
        self.assertFalse(mocked_upload_to_s3.called)

    @patch('pyqalxapi.request.requests.request')
    def test_get_set_request(self, mocked_request):
        resp = api.get('set')
        self.assertTrue(mocked_request.called)

    @patch('pyqalxapi.request.requests.request')
    def test_get_set_with_params_request(self, mocked_request):
        resp = api.get('set', params={'limit':2, 'skip':1, 'sort':'id'})
        self.assertIn('skip', mocked_request.call_args[1]['params'])
        self.assertTrue(mocked_request.called)


    @patch('pyqalxapi.request.requests.request')
    def test_post_set_request(self, mocked_request):
        resp = api.post('set', item_guids=[
            '494b775f-7c95-437b-9989-1c9b730ea67e'])
        self.assertIn('494b775f-7c95-437b-9989-1c9b730ea67e',
            mocked_request.call_args[1]['json']['item_guids'])
        self.assertTrue(mocked_request.called)

    @patch('pyqalxapi.request.requests.request')
    def test_get_group_request(self, mocked_request):
        resp = api.get('group')
        self.assertTrue(mocked_request.called)

    @patch('pyqalxapi.request.requests.request')
    def test_get_group_with_params_request(self, mocked_request):
        resp = api.get('group', params={'limit':2, 'skip':1, 'sort':'id'})
        self.assertIn('limit', mocked_request.call_args[1]['params'])
        self.assertTrue(mocked_request.called)

    @patch('pyqalxapi.request.requests.request')
    def test_post_group_request(self, mocked_request):
        resp = api.post('group', set_guids=[
            '2bc925a0-fd68-41e4-a779-6432ae36ba30',
            '191d8cbe-60c5-409c-9f2b-bfe8a80a09fa'])
        self.assertTrue(mocked_request.called)
        self.assertIn('2bc925a0-fd68-41e4-a779-6432ae36ba30',
            mocked_request.call_args[1]['json']['set_guids'])

    @patch('pyqalxapi.request.requests.request')
    def test_patch_by_id_request(self, mocked_request):
        resp = api.patch('queues/494b775f-7c95-437b-9989-1c9b730ea67e', data={'a':'b'})
        self.assertIn('494b775f-7c95-437b-9989-1c9b730ea67e',
             mocked_request.call_args[1]['url'])
        self.assertTrue(mocked_request.called)

    @patch('pyqalxapi.request.requests.request')
    def test_delete_by_id_request(self, mocked_request):
        resp = api.delete('bot/494b775f-7c95-437b-9989-1c9b730ea67e')
        self.assertIn('494b775f-7c95-437b-9989-1c9b730ea67e',
             mocked_request.call_args[1]['url'])
        self.assertTrue(mocked_request.called)
