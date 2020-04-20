# word-break challenge solution.

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
        {"input": ("catsandog", ["cats", "dog", "sand", "and", "cat"]), "output": False}
    ]

    test_results = map(lambda test_pair: solution.wordBreak(*test_pair["input"]) == test_pair["output"], test_examples)
    print "Test results: {}".format(map(lambda r: "pass" if r else "fail" , test_results))
