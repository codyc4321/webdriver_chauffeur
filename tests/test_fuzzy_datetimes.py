from datetime import datetime
from unittest import TestCase, skip

from tests import CustomTestBase
from fuzzywuzzy.fuzzy_datetimes import (
    pad_all_single_digits_with_zero,
    process_datetime_user_input,
    get_formatted_datestring
)


class GeneralUtilsTests(CustomTestBase):

    def test_pad_all_single_digits_with_zero(self):
        tests = [
            ('3-4-2016 10:00', '03-04-2016 10:00'),
            ('2016/3/4 10:00', '2016/03/04 10:00'),
            ('3-4-2016', '03-04-2016'),
            ('5', '05'),
            ('Jan 12, 2016', 'Jan 12, 2016'),
        ]
        self.run_assert_equals(pad_all_single_digits_with_zero, tests)

    def test_process_datetime_user_input(self):
        tests = [
            ('3-4-2016', datetime(2016, 3, 4, 0, 0)),
            ('2016/3/4 10:00', datetime(2016, 3, 4, 10, 0)),
            ('03-04-2017 6:00', datetime(2017, 3, 4, 6, 0)),
            ('Jan 12, 2015 2:00', datetime(2015, 1, 12, 2, 0)),
        ]
        self.run_assert_equals(process_datetime_user_input, tests)

    def test_get_gcp_ready_datestring(self):
        tests = [
            ('3-4-2016', '2016-03-04 00:00'),
            ('2016/3/4 10:00', '2016-03-04 10:00'),
            ('3-4-2016 5:00', '2016-03-04 05:00')
        ]
        self.run_assert_equals(get_formatted_datestring, tests)
