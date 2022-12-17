from django.core.exceptions import ValidationError
from django.test import TestCase

from ProjectDefence.accounts.models import Profile, AppUser


# Create your tests here.

class ProfileModelTests(TestCase):
    # 3A - Arrange,Act,Assert
    #      Setup , DO , Check result
    def test_profile_save__when_first_name_is_valid__expect_correct_result(self):
        user = AppUser(
            email='ganukoff@gmail.com',
            is_staff='True',
            password='Georgi123',

        )

        user.full_clean()
        user.save()

        profile = Profile(
            first_name='Georgi',
            last_name='Ganukov',
            city='Wraysbury',
            number='263',
            street='Staines Road',
            user=user,

        )

        profile.full_clean()
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_first_name_has_digit__expect_exception(self):
        user = AppUser(
            email='ganukoff@gmail.com',
            is_staff='True',
            password='Georgi123',

        )
        profile = Profile(
            first_name='Georgi1',
            last_name='Ganukov',
            city='Wraysbury',
            number='263',
            street='Staines Road',
            user=user,

        )
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_save__when_last_name_is_valid__expect_correct_result(self):
        user = AppUser(
            email='demendiafame@gmail.com',
            is_staff='True',
            password='Georgi123',

        )
        user.full_clean()
        user.save()

        profile = Profile(
            first_name='Georgi',
            last_name='Ganukov',
            city='Wraysbury',
            number='263',
            street='Staines Road',
            user=user,

        )

        profile.full_clean()
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_last_name_has_digit__expect_exception(self):
        user = AppUser(
            email='ganukoff@gmail.com',
            is_staff='True',
            password='Georgi123',

        )
        profile = Profile(
            first_name='Georgi',
            last_name='Ganukov1',
            city='Wraysbury',
            number='263',
            street='Staines Road',
            user=user,

        )
        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)
