3. smaller tasks
----------------

find the word with the most a’s in it
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

return the index of the word from a list of words that contains the
highest number of the letter a (lower OR higher case, so the word Array
contains 2). if none of the words contain any a’s, return -1, if
multiple contain the same amount return the index of the first one.
(remember, indexing starts with zero)

   ``["a", "aA", "abc"] -> 1``

.. code:: ipython3

    from jkg_evaluators import string_with_most_a_letters

.. code:: ipython3

    def most_a_letters_solution(list_of_words):
        # modify this function
        return -1

.. code:: ipython3

    string_with_most_a_letters.evaluate(most_a_letters_solution)

find the two numbers in a list that produce the highest number as their multiple
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the numbers have to be two different numbers in the list, but if the
same number occurs in the list twice, it can be used twice. return the
result of the multiplications.

   ``[1, 2, 3] -> 6``

.. code:: ipython3

    from jkg_evaluators import largest_multiple

.. code:: ipython3

    def find_largest_multiple(list_of_numbers):
        # modify this function
        return 0

.. code:: ipython3

    largest_multiple.evaluate(find_largest_multiple)

return the sum of distinct positive odd numbers from a list of numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

calculate from a list of integers, the sum of positive odd numbers,
taking each different number only once.

   ``[1, 1, 2, 3, 4] -> 1 + 3 = 4``

.. code:: ipython3

    from jkg_evaluators import sum_odd_positives

.. code:: ipython3

    def sum_solution(list_of_numbers):
        # modify this function
        return 1

.. code:: ipython3

    sum_odd_positives.evaluate(sum_solution)

find the largest number, where the digits are in ascending order
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

from a list of integers, find the one that is the largest among the ones
where the digits are in ascending order, if there is no such number,
return 0

   ``[10, 20, 7, 15] -> 15``

.. code:: ipython3

    from jkg_evaluators import largest_ascending_num

.. code:: ipython3

    def find_largest_ascending(list_of_numbers):
        # modify this function
        return 0

.. code:: ipython3

    largest_ascending_num.evaluate(find_largest_ascending)

find the number of strings in a list of strings that contain a given letter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

upper or lower case

   ``["abfg", "Bcd", "Ijk"], "b" -> 2``

.. code:: ipython3

    from jkg_evaluators import letter_occurrences

.. code:: ipython3

    def find_letter_occurrences(list_of_strings, letter):
        # modify this function
        return 2

.. code:: ipython3

    letter_occurrences.evaluate(find_letter_occurrences)

find the string that contains a given letter the largest number of times
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if none of the strings contain the letter, return an empty string. upper
or lower case should be ignored. if multiple strings contain the letter
the same amount of time, that is the highest, return the first one

   ``["bAbB", "cad", "BBaaCc"], "B" -> "bAbB"``

.. code:: ipython3

    from jkg_evaluators import word_with_most_of_letters

.. code:: ipython3

    def find_worth_with_most_of_letters(list_of_strings, letter):
        # modify this function
        return ''

.. code:: ipython3

    word_with_most_of_letters.evaluate(find_worth_with_most_of_letters)

find the largest number from a list, that divided by a given number, results in an even number
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if no such number is in the list, return 0

   ``[10, 15, 9, 38, 20], 2 -> 20``

.. code:: ipython3

    from jkg_evaluators import largest_even_divided

.. code:: ipython3

    def find_largest_even_divided(list_of_numbers, number):
        # modify this function
        return 0

.. code:: ipython3

    largest_even_divided.evaluate(find_largest_even_divided)

find the smallest number in a list, the double of which is also in the list
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

id there is no such number, return 0

   ``[1, 3, 7, 6, 15, 12, 20, 2] -> 3``

(as 6 is also in the list)

.. code:: ipython3

    from jkg_evaluators import smallest_where_double_also

.. code:: ipython3

    def find_smallest_where_double(list_of_numbers):
        # modify this function
        return 0

.. code:: ipython3

    smallest_where_double_also.evaluate(find_smallest_where_double)

find the last number in a list that has a difference from a given number that is a multiple of 3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if there is no such number, return 0.

   ``[1, 4, -5, 3, 9, 11, 7, 6, 4, 9], 10 -> 4``

beacause 10 - 4 = 6 that is a multiple of 3. although 10 -1 = 9 which is
also a multiple of 3, that number occurs earlier in the list and we’re
looking for the last number that satisfies this condition

.. code:: ipython3

    from jkg_evaluators import last_with_three_multiple_difference

.. code:: ipython3

    def find_last_with_three_multi_diff(list_of_numbers, number):
        # modify this function
        return 0

.. code:: ipython3

    last_with_three_multiple_difference.evaluate(find_last_with_three_multi_diff)

find the longest string in a list of words that contains the same letter at least three times
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if there is no such string, return "", if there are multiple words that
have same length and have at least 3 of the same letter, return the
first one. uppercase/lowercase does NOT matter

   ``["aBab", "ccaakjiHzuitg", "cacCrg", "hhhj", "aBGKi"] -> "caccrg"``

although ``"ccaakjihzuitg"`` is longer, there is no letter that appears
three times in it.

.. code:: ipython3

    from jkg_evaluators import longest_with_three_same_letters

.. code:: ipython3

    def find_longest_with_three_same_letters(list_of_words):
        # modify this function
        return ""

.. code:: ipython3

    longest_with_three_same_letters.evaluate(find_longest_with_three_same_letters)
