# encoding:utf8
import yaml
import time
import os
from task import AnsibleTask

# history = "history/" + str(time.time()).split('.')[0] + '.tmp'


def clear():
    os.system('clear')


dirs = "config-repo"
files = []
for file in os.listdir(dirs):
    if os.path.isdir(dirs + os.sep + file):
        continue
    else:
        files.append(dirs + os.sep + file)

while True:
    clear()
    t = 1
    array = []
    for a1 in files:
        print t, a1
        array.append(a1)
        t += 1
    r = raw_input("?: ")

    try:
        if int(r) > 0 and int(r) <= len(files):
            pass
        else:
            raise
    except:
        print "Input Error."
        exit(0)

    choice = array[int(r) - 1]
    print choice
    machine = '10.6.199.83'

    # dest_prefix = "/tima/conf/"
    dest_prefix = "/opt/"
    #
    x = []
    x.append(machine)
    # x.append("172.17.19.42")


    all_var = open("publiclabel.yml", 'r')
    a = AnsibleTask('\n'.join(x), yaml.load(all_var))

    path = choice.split(os.sep)
    filename = path.pop()
    dirname = path.pop()
    # print "path=" + dest_prefix + os.sep + dirname + " mode=0755       state=directory"
    # print "src=" + choice + " dest=" + dest_prefix + os.sep + dirname + os.sep + filename
    # print "src=" + choice + " dest=" + dest_prefix + os.sep + dirname + os.sep + filename
    # exit(0)
    tasks = []
    tasks.append(
        {'module': 'file',
         'args': "path=" + dest_prefix + os.sep + dirname + " mode=0755       state=directory"})
    if choice.endswith('j2'):
        name = filename.split('.j2')[0]
        tasks.append(
            {'module': 'template', 'args': "src=" + choice + " dest=" + dest_prefix + os.sep + dirname + os.sep + name})
    else:
        tasks.append(
            {'module': 'copy', 'args': "src=" + choice + " dest=" + dest_prefix + os.sep + dirname + os.sep + filename})
    a.ansbilePlayBook(tasks)