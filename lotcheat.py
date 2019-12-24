# coding:utf-8
import requests
import json
def get_tags(url: str) -> list:
    openId = url.split('ownerId=')[-1]
    data_url = 'https://2020luck.news.qq.com/friend/getInfo?openId={}'.format(openId)

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    r = requests.get(url = data_url, headers=headers)
    jsondata = json.loads(r.text)['data']
    nickname = jsondata['nickname']
    tags = jsondata['tags'].split(',')
    tags = [int(tag) for tag in tags]
    return nickname, tags

def get_items(tags: list) -> list:
    all_tags = [i for i in range(24)]
    all_items = ['限量款包包', '可爱玩偶', '惊喜红包', '猫咪主子',
                '优秀员工奖', '偶像见面票', '年终股票', '财神爷',
                '永和钻戒', '每日鲜花', '健康好身体', '暖心房东',
                '男朋友', '超能力大脑', '10W+文章', '时光倒流机',
                '好运锦鲤', '瘦身魔法', '特价机票', '千杯酒量',
                '高薪Offer', '女朋友', '啤酒烧烤', '最强王者']
    tags_items = dict(zip(all_tags, all_items))
    items = [tags_items[tag] for tag in tags]
    return items

if __name__ == "__main__":
    url = 'https://yslp.qq.com/yyh5/guess2020.htm?ownerId=o04Jg03VTcW_MqP3W5LmFgXGYAcw'
    nickname, tags = get_tags(url)
    items =  get_items(tags)
    print('{}选择的愿望是: '.format(nickname))
    print(items)
