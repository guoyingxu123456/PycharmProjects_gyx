def test(num):
    print("函数内部的内存地址 %d"% id(num))
    fs ="hello"
    print("hello %d" %id(fs))
    return fs
a=1
print("内存地址 %d"% id(a))

test(a)
l=test(a)
print("%s,%d"%(l,id(l)))


def sum(a,b):
    c = a + b;
    return c

d = sum(1,2)
print(d)
print("#" * 100)
sz = [];
print(type(sz))
sz.append(1)
print("%s"% sz)
print("#" * 100)
ls = 100;
i=0
lc= [];
while i <= ls:
    lc.append(i);
    i += 1;
print("%s"% lc)
print("#" * 100)
for a in lc:
    print("%s" % a)

a= 12500
b= 3000
c = a-b
print(c)
print("#" * 100)
def cljg():
    print("测量开始...")
    wd = 35
    sd =79
    print("测量结束...")
    return wd ,sd
h_wd,h_sd =cljg()
print(h_wd)
print(h_sd)
print("#" * 100)
def demo(num_list):
    print("函数开始")
    num_list.append(9)
    print(num_list)
    print("函数结束")
gl_list =[1,2,3]
demo(gl_list)
print(gl_list)
print("#" * 100)
def test(num):
    num += num
    print(num)
gl_num = [1,2,3]
test(gl_num)
print(gl_num)