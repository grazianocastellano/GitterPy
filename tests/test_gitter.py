import json
import unittest

from mock import MagicMock, patch

from gitterpy.client import Auth, Groups, Messages, Rooms


class TestGitter(unittest.TestCase):
    def setUp(self):
        self.auth = Auth('Token')
        self.rooms = Rooms('Token')
        self.groups = Groups('Token')
        self.messages = Messages('Token')
        self.json_data = json.dumps([{'id': '1', 'name': 'Freshjelly'}])
        self.mock_data = MagicMock(
            status_code=200,
            json_data=self.json_data
        )

    def tearDown(self): pass

    @patch('gitterpy.client.r')
    def test_gitter_auth(self, request):
        request.get.return_value = self.mock_data
        self.assertTrue(self.json_data, self.auth.check_auth)

    @patch('gitterpy.client.r')
    def test_groups_list(self, request):
        request.get.return_value = self.mock_data
        self.assertTrue(self.json_data, self.groups.list)

    @patch('gitterpy.client.r')
    def test_join_in_room(self, request):
        request.get.return_value = self.mock_data
        self.assertTrue(self.json_data, self.rooms.join('gitterHQ/sandbox'))

    @patch('gitterpy.client.r')
    def test_update_room_topic(self, request):
        request.get.return_value = self.mock_data
        self.assertTrue(
            self.json_data,
            self.rooms.update('gitterHQ/sandbox', 'My topic')
        )

    @patch('gitterpy.client.r')
    def test_room_sub_resource(self, request):
        request.get.return_value = self.mock_data
        self.assertTrue(
            self.json_data,
            self.rooms.sub_resource('gitterHQ/sandbox')
        )

    @patch('gitterpy.client.r')
    def test_message_list(self, request):
        request.get.return_value = self.mock_data
        self.assertTrue(self.json_data, self.messages.list('gitterHQ/sandbox'))


if __name__ == '__main__':
    unittest.main()
