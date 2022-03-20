from django.contrib.auth import get_user_model
from django.test import TestCase
from user.models import TrustPerson


class UserModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'user_tes@test.com'
        password = '123qwe!@#'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # assert email == user.email, 'erhdfghf'
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalize(self):
        email = 'user_test@TEST.coM'
        user = get_user_model().objects.create_user(
            email=email,
            password='123qwe!@#'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='123qwe!@#'
            )


class TrustPersonTests(TestCase):
    def test_create_trust_person(self):
        name = 'Alisa'
        contact_phone = '+3806745816'
        town = 'Kiev'
        person = TrustPerson.objects.create(
            name=name,
            contact_phone=contact_phone,
            town=town
        )
        self.assertEqual(person.contact_phone, contact_phone)

    def test_normalize__name_trust_person(self):
        name = 'aliSA'
        contact_phone = '+3806745816'
        person = TrustPerson.objects.create(
            name=name,
            contact_phone=contact_phone
        )
        self.assertEqual(person.name, name.capitalize())

    def test_contact_phone_trust_person(self):

        with self.assertRaises(ValueError):
            TrustPerson.objects.create(
                name='Alisa',
                contact_phone=None
            )
