#!/usr/bin/env python

import unittest
import numpy as np
import numpy.testing as npt
from common.util import preprocess


class TestUtil(unittest.TestCase):
    # 2.3.1 Prepossessing by Python
    def test_preprocess(self):
        input = 'You say goodbye and I say hello.'
        expected_word_to_id = {
            "you": 0,
            "say": 1,
            "goodbye": 2,
            "and": 3,
            "i": 4,
            "hello": 5,
            ".": 6
        }
        expected_id_to_word = {
            0: "you",
            1: "say",
            2: "goodbye",
            3: "and",
            4: "i",
            5: "hello",
            6: "."
        }
        expected_corpus = np.array([0, 1, 2, 3, 4, 1, 5, 6])

        actual_corpus, actual_word_to_id, actual_id_to_word = preprocess(input)

        npt.assert_array_equal(
            actual_corpus,
            expected_corpus)

        self.assertDictEqual(
            actual_word_to_id,
            expected_word_to_id)

        self.assertDictEqual(
            actual_id_to_word,
            expected_id_to_word)
