line = open(words.txt).readline()
words=line.split(" ")
count=0
for word in words:
    word=word.strip()
    if(word.len()>2) and (word[0]==word[-1]):
        count++
print(count)