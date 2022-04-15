from pip import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
        row1 += [letter.lower() for letter in row1]

        row2 = ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
        row2 += [letter.lower() for letter in row2]

        row3 = ["Z", "X", "C", "V", "B", "N", "M"]
        row3 += [letter.lower() for letter in row3]

        result = []

        for word in words:
            flag = [0]*3
            for letter in word:

                if letter in row1:
                    flag[0] = 1
                elif letter in row2:
                    flag[1] = 1
                elif letter in row3:
                    flag[2] = 1

            print(sum(flag))
            if sum(flag) == 1:
                result.append(word)

        return result


res = Solution()
words = ["Hello","Alaska","Dad","Peace"]
ans = res.findWords(words)
print(ans)