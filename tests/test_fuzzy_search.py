from unittest import TestCase

from fuzzywuzzy.fuzzy_search import (
    compare_pattern_similarity,
    get_closest_match
)


class GeneralUtilsTests(TestCase):

    def test_compare_pattern_similarity(self):
        self.assertGreater(
            compare_pattern_similarity('cow', 'cowsay'),
            compare_pattern_similarity('cow', 'giraffe'),
        )

        self.assertGreater(
            compare_pattern_similarity('item', 'itemize'),
            compare_pattern_similarity('item', 'thing'),
        )

    def test_get_closest_match(self):
        result = get_closest_match('cow', ['giraffe', 'cows', 'cowsay'])
        self.assertEqual(result, 'cows')

        result = get_closest_match('dolphin', ['dolls', 'elephants', 'giraffe'])
        self.assertEqual(result, 'dolls')

        result = get_closest_match(
            'Are you sure fuzzy search works?',
            ['Not yet', 'Ok now I\'m pretty sure fuzzy search works', 'naw']
        )
        self.assertEqual(result, 'Ok now I\'m pretty sure fuzzy search works')
