import json

from django.test import TestCase
from django.urls import reverse

from main.models import Email, Press


class TestPressViewView(TestCase):
    def setUp(self):
        self.press = []
        for i in range(6):
            press = Press.objects.create(author=f"Author_{i}", title=f"Title_{i}")
            self.press.append(press.id)
        self.press.reverse()

    def test_get(self):
        with self.subTest("default request"):
            response = self.client.get(reverse("get-press"))
            self.assertEqual(200, response.status_code)
            self.assertEqual(self.press[:5], [press["id"] for press in json.loads(response.content)["press"]])

        with self.subTest("request with query param"):
            response = self.client.get(reverse("get-press"), {"limit": 10})
            self.assertEqual(200, response.status_code)
            self.assertEqual(self.press, [press["id"] for press in json.loads(response.content)["press"]])


class TestSendEmailView(TestCase):
    def test_post(self):
        with self.subTest("request with empty body"):
            response = self.client.post(reverse("send-email"), {"sender": ""})
            self.assertEqual(400, response.status_code)

        with self.subTest("request with incorrect email"):
            response = self.client.post(
                reverse("send-email"), {"sender": "Sender_1", "msg": "Msg_1", "email": "incorrect_email"}
            )
            self.assertEqual(400, response.status_code)

        with self.subTest("correct request"):
            response = self.client.post(
                reverse("send-email"), {"sender": "Sender_2", "msg": "Msg_2", "email": "test@example.com"}
            )
            self.assertEqual(200, response.status_code)
            self.assertTrue(Email.objects.filter(sender_name="Sender_2", message="Msg_2").exists())
