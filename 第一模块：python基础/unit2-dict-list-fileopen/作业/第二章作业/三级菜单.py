menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

current_level=menu
levels=[]
while True:
    for k in current_level: print(k)
    choice=input("你想要移动到哪层: ").strip()
    if not choice:continue
    elif choice in current_level:
        levels.append(current_level)
        current_level=current_level[choice]`
    elif choice == 'b':
        if levels:
            current_level=levels.pop()
        else:
            print("到最顶层了: ")
    elif choice == 'q':     exit("退出程序")
    else:   print("值不存在: ")