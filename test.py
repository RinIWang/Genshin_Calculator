A = {'a': 1, 'b': 2, 'c': 3}
B = {'b': 4, 'c': 6, 'd': 8}
C = {}
for key in list(set(A) | set(B)):
    if A.get(key) and B.get(key):
        C.update({key: A.get(key) + B.get(key)})
    else:
        C.update({key: A.get(key) or B.get(key)})
print(C)

with open("output.json", "w", encoding='utf-8') as f:
   json.dump(Dict, f, ensure_ascii=False, indent=4)
   print(u'加载入文件完成...')
