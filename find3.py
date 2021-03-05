import re

keywords=['18ASSZtpfWxJW4K6XfwLtB71LtqQuAPqsB', '1KKYPvE6b1GKTF1t2eg8JEfjmq3wj56bFN', '12DSroNbamqud5qUAgZL5e4KZ7GKKVfvJW', '14HKqyXyCFc7VWDp69NX2Z51tNKJQWFGMQs']


with open("addresses.txt", "r", encoding="utf8") as f:
    searchInLines = f.readlines()

#pattern = re.compile("(" + "|".join(keywords) + ")", flags=re.IGNORECASE)
pattern = re.compile("(" + "|".join(r"\b{}\b".format(i) for i in keywords) + ")", flags=re.IGNORECASE)
for line in searchInLines:
    if pattern.search(line):
        print("word found",line)
