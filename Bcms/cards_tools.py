#记录所有的名片字典
card_list = []

def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】 v1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)

def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    #1、提示用户输入名片的详细信息
    name_str =input("请输入姓名： ")
    phone_str = input("请输入电话： ")
    qq_str = input("请输入QQ： ")
    email_str = input("请输入邮箱： ")
    #2、使用用户输入的信息建立一个名片字典
    card_dict ={"name":name_str,
                "phone":phone_str,
                "qq":qq_str,
                "email":email_str}
    #3、将名片字典添加到列表中
    card_list.append(card_dict)
    #print(card_list)
    #4、提示用户添加成功
    print("添加 %s 的名片成功!" % name_str)
def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    #打印表头
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片！")
        return
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    #遍历字典数据
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t"% (card_dict["name"],card_dict["phone"],card_dict["qq"],card_dict["email"]))
def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入要搜索的姓名： ")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"], card_dict["phone"], card_dict["qq"], card_dict["email"]))

            #定义一个函数来传递查找到的card_dict
            #针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)
            break
    else:
        print("抱歉没有找到相关信息")

def deal_card(find_card):
    """处理查找到的名片

    :param find_card:查找到的名片
    """
    print(find_card)
    action_str =input("请选择要执行的操作"
                      " 【1】 修改 【2】 删除 【0】 返回上级菜单")
    if action_str == "1":
        find_card["name"]=input_card(find_card["name"],"name")
        find_card["phone"] = input_card(find_card["phone"],"phone")
        find_card["qq"] = input_card(find_card["qq"],"qq")
        find_card["email"] = input_card(find_card["email"],"email")
        print("修改名片")
    elif action_str == "2":
        card_list.remove(find_card)
        print("删除名片成功")

def input_card(dict_value,message):
    """输入名片信息

    :param dict_value:字典中原有的值
    :param message:输入的提示文字
    :return:如果用户输入了内容就返回内容，否则返回字典中原有的值
    """
    #1、提示用户输入内容
    result_str = input(message)
    #2、针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    #3、如果用户没有输入内容。返回`字典中原有的值`
    else:
        return dict_value