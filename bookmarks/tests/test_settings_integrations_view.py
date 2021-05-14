from django.test import TestCase
from django.urls import reverse

from bookmarks.tests.helpers import BookmarkFactoryMixin


class SettingsIntegrationsViewTestCase(TestCase, BookmarkFactoryMixin):

    def setUp(self) -> None:
        user = self.get_or_create_test_user()
        self.client.force_login(user)

    def test_should_render_successfully(self):
        response = self.client.get(reverse('bookmarks:settings.integrations'))

        self.assertEqual(response.status_code, 200)

    def test_should_check_authentication(self):
        self.client.logout()
        response = self.client.get(reverse('bookmarks:settings.integrations'), follow=True)

        self.assertRedirects(response, reverse('login') + '?next=' + reverse('bookmarks:settings.integrations'))
