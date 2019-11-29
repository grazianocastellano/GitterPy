import json
import sys
import unittest

from mock import MagicMock, patch

from gitterpy.client import Auth, Groups, Messages, Rooms, User

sys.path.insert(0, '../gitterpy/')



class TestGitter(unittest.TestCase):
    def setUp(self):
        self.auth = Auth('Token')
        self.rooms = Rooms('Token')
        self.groups = Groups('Token')
        self.messages = Messages('Token')
        self.user = User('Token')
        self.json_data = json.dumps([{'id': '1', 'name': 'Freshjelly'}])
        self.mock_data = MagicMock(
            status_code=200,
            json_data=self.json_data
        )

    def tearDown(self): pass

    def return_assert(self, request, func):
        request.get.return_value = self.mock_data
        return self.assertTrue(self.json_data, func)
 
    @patch('gitterpy.client.r')
    def test_gitter_auth(self, request):
        return self.return_assert(request, self.auth.check_auth())

    @patch('gitterpy.client.r')
    def test_groups_list(self, request):
        return self.return_assert(request, self.groups.list)

    @patch('gitterpy.client.r')
    def test_join_in_room(self, request):
        return self.return_assert(request, self.rooms.join('gitterHQ/sandbox'))

    @patch('gitterpy.client.r')
    def test_update_room_topic(self, request):
        return self.return_assert(
            request,
            self.rooms.update('gitterHQ/sandbox', 'My topic')
        )

    @patch('gitterpy.client.r')
    def test_room_sub_resource(self, request):
        return self.return_assert(
            request,
            self.rooms.sub_resource('gitterHQ/sandbox')
        )

    @patch('gitterpy.client.r')
    def test_message_list(self, request):
        return self.return_assert(
            request,
            self.messages.list('gitterHQ/sandbox')
        )

    @patch('gitterpy.client.r')
    def test_send_message(self, request):
        return self.return_assert(
            request,
            self.messages.send('gitterHQ/sandbox', 'hello')
        )

    @patch('gitterpy.client.r')
    def test_get_message(self, request):
        return self.return_assert(
            request,
            self.messages.get_message('gitterHQ/sandbox', '3123123123')
        )

    @patch('gitterpy.client.r')
    def test_user_auth(self, request):
        return self.return_assert(
            request,
            self.user.check_auth()
        )

    @patch('gitterpy.client.r')
    def test_user_sub_resource(self, request):
        return self.return_assert(
            request,
            self.user.sub_resource
        )

    @patch('gitterpy.client.r')
    def test_user_unread_items(self, request):
        return self.return_assert(
            request,
            self.user.unread_items('gitterHQ/sandbox')
        )

    @patch('gitterpy.client.r')
    def test_user_orgs(self, request):
        return self.return_assert(
            request,
            self.user.orgs
        )

    @patch('gitterpy.client.r')
    def test_user_repos(self, request):
        return self.return_assert(
            request,
            self.user.repos
        )

    @patch('gitterpy.client.r')
    def test_user_channels(self, request):
        return self.return_assert(
            request,
            self.user.channels
        )


if __name__ == '__main__':
    unittest.main()
