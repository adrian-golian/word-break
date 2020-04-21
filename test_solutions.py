import pytest
import word_break_2 as wb


test_examples = [
    {"input": ("pineapplepenapple", ["pineapple", "apple", "pen", "applepen", "pine"]), "output": ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]},
    {"input": ("leetcode", ["leet", "code"]), "output": ["leet code"]},
    {"input": ("applepenapple", ["apple", "pen"]), "output": ["apple pen apple"]}
]

@pytest.mark.parametrize("test_input,expected", [(t["input"], t["output"]) for t in test_examples])
def test_word_break_2(test_input, expected):
    assert set(wb.Solution().wordBreak(*test_input)) == set(expected)
