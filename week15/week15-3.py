# week15-3.py 
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #先用Python 把字串的迴圈寫出來
        N = len(s) # 先知道字串的長度
        ans = 0
        j = 0 #毛毛蟲的尾巴i
        for i in range(N): #字串的迴圈 毛毛蟲的頭i
            maxCost -= abs(ord(s[i]) - ord(t[i])) # 用了多少能量, 才能吃第i格
            while maxCost < 0: #能量不夠,尾巴要縮
                maxCost += abs(ord(s[j]) - ord(t[j]))
                j += 1
            ans = max(ans, i-j+1)

        return ans # 課堂作業1, 先歲便給個0當答案(答案當然不對)