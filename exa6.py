list = []
list += "apple"
list += "banana"

print(list[1])
# appleではなくpと表記される
print(list)

# リストはリスト以外と結合できないので、結合させるものをリストにすればいいだけ。

list1 = []
list1 = list1 + ["apple"]
list1 += ["banana"]
print(list1[1])
print(list1)
