Question:
Write a function to generate the generalized abbreviations of a word.

Example:
Given word ="word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
test='word'
round 1: ['w','1']
round 2: ['wo','w1','1o','2']
round 3: ['wor','wo1','w1r',...]


Solution:

    def generateAbbreviations(self, word: str):
        if not word:
            return [""]
        ans = ['']
        for i in range(len(word)):
            temp = []
            for item in ans:
                temp.append(item + word[i])
                if not item:
                    temp.append('1')
                elif item[-1].isdigit():
                    temp.append(item[:-1] + str(int(item[-1]) + 1))
                else:
                    temp.append(item + '1')
            ans = temp
        return ans
