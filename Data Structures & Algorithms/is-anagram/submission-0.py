class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = dict()
        s2 = dict()

        for letter in s:
            s1[letter] = s1.get(letter, 0) + 1

        for letter in t:
            s2[letter] = s2.get(letter, 0) + 1

        if s1 == s2:
            return True

        return False
