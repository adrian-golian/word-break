# word-break challenge solution.
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return True


if __name__ == "__main__":
    solution = Solution()

    test_examples = [
        {"input": ("leetcode", ["leet", "code"]), "output": True},
        {"input": ("applepenapple", ["apple", "pen"]), "output": True},
        {"input": ("applepenpple", ["apple", "pen"]), "output": False},
        {"input": ("applepenpenapple", ["apple", "pen"]), "output": True},
        {"input": ("categorycat", ["category", "cat"]), "output": True},
        {"input": ("catsandog", ["cats", "dog", "sand", "and", "cat"]), "output": False},
        {"input": ("catsand", ["cats", "sand", "and", "cat"]), "output": True},
        {"input": ("catsand", ["cats", "sand", "cat"]), "output": True},
        {"input": ("catsand", ["cats", "sand", "and"]), "output": True},
        {"input": ("catsand", ["cats", "and", "cat"]), "output": True},
    ]

    test_results = map(lambda test_pair: solution.wordBreak(*test_pair["input"]) == test_pair["output"], test_examples)
    print "Test results: {}".format(map(lambda r: "pass" if r else "fail" , test_results))
