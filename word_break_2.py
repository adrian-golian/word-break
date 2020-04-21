# word-break-ii challenge solution.
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences.
import re
import copy

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.fullstring = s

        self.found_tokens = [m for matches in map(self.get_matches, wordDict) for m in matches]
        sentences = [[t] for t, _ in enumerate(self.found_tokens)]

        complete_sentences = []
        done = False
        while not done:
            # Grow only valid sentences, one token at a time
            # (better than generating all token permutations and validating each)
            sentence_sets = map(self.build_sentences, sentences)
            sentences = [s for sentences in sentence_sets for s in sentences]

            # Put complete valid sentences aside
            to_remove = []
            for i, sentence in enumerate(sentences):
                if self.is_complete(sentence):
                    complete_sentences.append(sentences[i])
                    to_remove.append(i)
            sentences = [s for i, s in enumerate(sentences) if i not in to_remove]

            if len(sentences) == 0:
                done = True

        return map(self.make_string_sentence, complete_sentences)

    def make_string_sentence(self, sentence):
        return " ".join([self.found_tokens[t]["token"] for t in sentence])

    def is_complete(self, sentence):
        """
            Check if sentence is complete
            (whether it makes the fullstring when joined)
        """
        return "".join([self.found_tokens[t]["token"] for t in sentence]) == self.fullstring

    def build_sentences(self, sentence):
        """
            Take a sentence of length N
            and find all valid sentences of length N+1
            (so the output can be an empty list!)
        """
        last_token = self.found_tokens[sentence[-1]]
        candidate_token_ids = []
        for i, token in enumerate(self.found_tokens):
            if token["start"] == last_token["end"] + 1:
                candidate_token_ids.append(i)
        new_sentences = [copy.deepcopy(sentence) + [id] for id in candidate_token_ids]
        return new_sentences

    def get_matches(self, token):
        """
            Find all occurances of a token in the `full string`
            and output each one in a token object.
        """
        return [{"token":token, "start":i, "end":i+len(token)-1} for i in self.find_occurances(token)]

    def find_occurances(self, substring):
        """ Find occurances of a substring in the full string """
        return map(lambda match: match.start(), re.finditer(substring, self.fullstring))


if __name__ == "__main__":
    solution = Solution()

    test_examples = [
        {"input": ("pineapplepenapple", ["pineapple", "apple", "pen", "applepen", "pine"]), "output": ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]},
        {"input": ("leetcode", ["leet", "code"]), "output": ["leet code"]},
        {"input": ("applepenapple", ["apple", "pen"]), "output": ["apple pen apple"]}
    ]

    test_results = map(lambda test_pair: set(solution.wordBreak(*test_pair["input"])) == set(test_pair["output"]), test_examples)
    print "Test results: {}".format(map(lambda r: "pass" if r else "fail" , test_results))
