# 실습 1

import pandas as pd

df = pd.read_csv("data/13_diecasting_small.csv")
#s = df["형체력"]
#print(type(s))
#print(s.head(3))

#two = df[["형체력", "실린더압력"]]
#print(type(two))
#print(two.shape)

#one = df[["형체력"]]
#print(type(one))
#print(one.shape)

# 실습 2

#print(df.loc[0, "샷"])
#print(df.iloc[0]["샷"])

#srt = df.sort_values("형체력", ascending=False)
#print(srt.loc[0, "샷"])
#print(srt.iloc[0]["샷"])

# 실습 3

#for i, c in enumerate(df.columns):
#    print(i, c)

#a = df.loc[0:4, ["실린더압력", "형체력"]]
#print(a.shape)

#b = df.iloc[0:5, [2, 6]]
#print(b.shape)

#print(a.equals(b))

# 실습 4

print(df.shape)
for i, c in enumerate(df.columns):
    print(i, c)

top = df.loc[0:9, ["설비ID", "비스킷두께", "품질등급"]]
print(top.shape)
print(top)
tail5 = df.iloc[-5:]
print(tail5.shape)
print(tail5)