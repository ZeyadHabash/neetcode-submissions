class Solution:

    # naive way is just joining them with a character in between prob?
    # hmm that failed
    # maybe we can learn from RLE and use a number to tell the decoder how many letters is the upcoming word?
    # this should be O(n+m) where m is the sum of lengths of all strings and n is the number of strings
    # but its runtime is pretty bad

    # this is basically the solution they just use the 2 pointers better than I do lol

    def encode(self, strs: List[str]) -> str:
        result = ""
        # O(n)
        for s in strs:
            result += (str(len(s)) + "#" + s)

        return result

    def decode(self, s: str) -> List[str]:
        str_next_word_size = ""
        int_next_word_size = 0
        result = []
        i = 0
        # m + 2*n
        # O(m+n)
        while i < len(s):
            if s[i] == '#':
                int_next_word_size = int(str_next_word_size)
                word = ""
                i+=1
                for j in range(int_next_word_size):
                    word += s[i+j]
                result.append(word)
                i += int_next_word_size - 1
                str_next_word_size = ''
            else:
                str_next_word_size += s[i]
            i += 1
        return result

