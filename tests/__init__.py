from unittest import TestCase


class CustomTestBase(TestCase):

    def run_assert_equals(self, callback, datasets):
        for dataset in datasets:
            if isinstance(dataset, dict):
                result = callback(dataset['input'])
                self.assertEqual(result, dataset['expectation'])
            elif isinstance(dataset, list) or isinstance(dataset, tuple):
                result = callback(dataset[0])
                self.assertEqual(result, dataset[1])
            else:
                raise Exception("Unexpected input format running assertEquals")
