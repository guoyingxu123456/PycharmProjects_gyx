def input_card(jieguo,msagess):
    res_str = input(msagess)
    if len(res_str) > 0:
        return res_str
    else:
        return jieguo

name = "郭迎旭"

name =input_card(name,"请输入信息")

print(name)