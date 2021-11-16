"""
yesterday.txt 파일을 읽어서
yesterday 단어가 몇 번 나오는지를 count 
"""

"""
open mode
r: read, w:write
rb : read binary, wb: write binary
o : oppend
"""
def file_read(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        lyric = file.read()
        return lyric


read = file_read("yesterday.txt")
print(read)
n_of_YESTERDAY = read.upper().count("YESTERDAY")
print(f'Number of a word YESTERDAY {n_of_YESTERDAY}')
n_of_Yesterday = read.count("Yesterday")
print(f'Number of a word Yesterday {n_of_Yesterday}')
n_of_yesterday = read.lower().count("YESTERDAY")
print(f'Number of a word YESTERDAY {n_of_yesterday}')
