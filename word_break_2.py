# word-break-ii challenge solution.
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences.
import re
import itertools
import copy

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return []

if __name__ == "__main__":
    solution = Solution()

    test_examples = [
        {"input": ("leetcode", ["leet", "code"]), "output": ["leet code"]},
        {"input": ("applepenapple", ["apple", "pen"]), "output": ["apple pen apple"]},
    ]

    test_results = map(lambda test_pair: solution.wordBreak(*test_pair["input"]) == test_pair["output"], test_examples)
    print "Test results: {}".format(map(lambda r: "pass" if r else "fail" , test_results))
