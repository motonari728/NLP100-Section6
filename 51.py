# 51. 単語の切り出し
# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．


import re

if __name__ == "__main__":
    f = open('lines.txt', 'r')
    for line in f:
        l = line.strip()
        for word in l.split():
            print(re.sub(r"\W", "", word))
        print("")
    f.close()