from django.core.exceptions import ValidationError
from django.test import TestCase

from ProjectDefence.common.models import Complaint


# Create your tests here.
class ComplaintModelTest(TestCase):
    def test_complaint_save__when_first_name_is_valid__expect_correct_result(self):
        complaint = Complaint(
            first_name='Georgi',
            email='ganukoff@gmail.com',
            subject='Dont like it',
            message='asdasdasdasdasdasdasdasdasdasdasdasd'
        )

        complaint.full_clean()
        complaint.save()
        self.assertIsNotNone(complaint.pk)

    def test_complaint_save__when_first_name_has_digit__expect_exception(self):
        complaint = Complaint(
            first_name='Georgi1',
            email='ganukoff@gmail.com',
            subject='Dont like it',
            message='asdasdasdasdasdasdasdasdasdasdasdasd'
        )

        with self.assertRaises(ValidationError) as context:
            complaint.full_clean()
            complaint.save()
        self.assertIsNotNone(context.exception)