# week16-1 的輔助常識1 collections.Counter
#import collections # 修改前
from collections import Counter  # 修改後
word = ["bella", "label", "roller"]
for i in range(3):
  #counter = collections.Counter(word[i]) # 修改前
  counter = Counter(word[i]) # 修改後
  print(word[i], counter)
#ans = collections.Counter(word[0]) &collections.Counter(word[1])&collections.Counter(word[2])
ans = Counter(word[0]) & Counter(word[1]) & Counter(word[2]) # 修改後
print(ans)