# 1、发送请求，获取数据
import requests
url = f'http://wthrcdn.etouch.cn/weather_mini?citykey={"101010100"}'
res = requests.get(url)
res.encoding = 'utf-8'
res_json = res.json()

# 2、数据格式化
data = res_json['data']
city = f"城市：{data['city']}\n"
# 字符串格式化的一种方式 f"{}" 通过字典传递值

today = data['forecast'][0]
date = f"日期：{today['date']}\n"  # \n 换行
now = f"实时温度：{data['wendu']}度\n"
temperature = f"温度：{today['high']} {today['low']}\n"
fengxiang = f"风向：{today['fengxiang']}\n"
type = f"天气：{today['type']}\n"
tips = f"贴士：{data['ganmao']}\n"

result = city + date + now + temperature + fengxiang + type + tips

print(result)
