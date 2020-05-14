import random
import string
def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)

print(Unicode())

# 写入随机纯数字字母
#
file = open('11.txt','w')
for i in range(100):
    random_str = ''.join(random.sample(string.digits *5 +string.ascii_letters *4,255))
    file.write(random_str + '\n')
file.close()

# 写入随机纯中文
# file = open('11.txt','w')
# for i in range(100):
#     random_str = ''.join(Unicode())
#     file.write(random_str)
# file.close()


