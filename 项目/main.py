from PyQt5.QtWidgets import *
from PyQt5 import uic
from Lib.SIC import SIC
import requests
import pymysql
import images_rc
class Win_Login:
    def __init__(self):
        self.ui = uic.loadUi('login.ui')
        self.ui.btn_login.clicked.connect(self.onSignIn)
        self.ui.edt_password.returnPressed.connect(self.onSignIn)
        self.ui.btn_register.clicked.connect(self.register)
        self.ui.btn_return.clicked.connect(self.returned)
        self.ui.label_ewmjs.setOpenExternalLinks(True)
        self.ui.label_ewmjs.setText(
            u'<a href="http://www.weather.com.cn/" style="color:#0000ff; text-decoration:none">中国天气网</a>')


    def onSignIn(self):
        username = self.ui.edt_username.text().strip()
        password = self.ui.edt_password.text().strip()

        # 获取数据库账号密码
        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", port=3306, db='login',
                               charset="utf8")
        cursor = conn.cursor()
        sql = "SELECT * FROM users"
        # 使用execute()方法执行SQL语句
        cursor.execute(sql)
        # 使用fetchall()方法获取全部数据
        result = cursor.fetchall()
        cursor.close()
        flag =0
        for i in range(len(result)):
            # print(result[i][0])
            # print(result[i][1])
        # 登录验证
            if username == result[i][0] and password ==result[i][1]:
                flag = 1
                QMessageBox.information(self.ui, '正确', '恭喜您，登陆成功！')
                SIC.mainWin = Win_Main()
                SIC.mainWin.ui.show()
                self.ui.edt_password.setText('')
                self.ui.hide()
                # 将登录界面隐藏
                return None
            else:
                flag = 0
        if flag == 0:
            QMessageBox.warning(self.ui, '警告', '用户名或密码输入错误，请重新输入！')

    def returned(self):
        QMessageBox.information(self.ui, '成功', '退出成功！欢迎下次使用！！！')
        self.ui.close()

    def register(self):
        SIC.mainWin = Win_Register()
        SIC.mainWin.ui.show()
        self.ui.hide()

# 注册窗口
class Win_Register:
    def __init__(self):
        self.ui = uic.loadUi('register.ui')
        self.ui.reg_button.clicked.connect(self.onRegiest)
        self.ui.cancel_button.clicked.connect(self.onCancel)
        self.ui.label_ewmjs.setOpenExternalLinks(True)
        self.ui.label_ewmjs.setText(
            u'<a href="http://www.weather.com.cn/" style="color:#0000ff; text-decoration:none">中国天气网</a>')

    def onRegiest(self):
        # 获取输入的用户名和密码
        reg_username = self.ui.reg_username.text().strip()
        reg_password = self.ui.reg_password.text().strip()
        reg_cert_password = self.ui.edt_password_cert.text().strip()

        conn = pymysql.connect(host="localhost", user="root", passwd="12345678", port=3306, db='login',
                               charset="utf8")
        cursor = conn.cursor()
        sql = "SELECT * FROM users"
        # 使用execute()方法执行SQL语句
        cursor.execute(sql)
        # 使用fetchall()方法获取全部数据
        result = cursor.fetchall()
        # 将数据用字典形式存储于result
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in result]
        # 关闭连接
        cursor.close()
        # print(result)
        ulist = []
        for i in result:
            ulist.append(i['reg_username'])
        # print(ulist)

        if reg_password=="" or reg_username == "":
            QMessageBox.warning(self.ui, "警告", "用户名或密码不能为空！！！")
        elif reg_username in ulist:
            QMessageBox.warning(self.ui, "警告", "用户名已存在")
        elif reg_cert_password == reg_password:
            QMessageBox.information(self.ui, "成功", "恭喜您，注册成功！")
            # 连接数据库
            conn = pymysql.connect(host="localhost", user="root", passwd="12345678", port=3306, db='login',
                                   charset="utf8")
            cursor = conn.cursor()
            # 添加账号密码到数据库
            sql2 = "insert into users(reg_username,reg_password) values(" + "'" + reg_username + "'" + ",'" + reg_password + "'"")"
            cursor.execute(sql2)
            conn.commit()
            conn.close()

            SIC.mainWin = Win_Login()
            SIC.mainWin.ui.show()
            self.ui.hide()
        else:
            QMessageBox.critical(self.ui, "错误", "两次密码输入不一样，请重新输入！！！")

    def onCancel(self):
        SIC.mainWin.ui.hide()
        SIC.loginWin.ui.show()

# 主窗口
class Win_Main:
    def __init__(self):
        self.ui = uic.loadUi('weather.ui')
        self.ui.actionExit.triggered.connect(self.onSignOut)
        self.ui.clearButton.clicked.connect(self.clearResult)
        self.ui.queryButton.clicked.connect(self.queryWeather)
        self.ui.PiccomboBox.currentIndexChanged.connect(self.choicPic)
        self.ui.label_ewmjs.setOpenExternalLinks(True)
        self.ui.label_ewmjs.setText(
            u'<a href="http://www.weather.com.cn/" style="color:#0000ff; text-decoration:none">中国天气网</a>')

    def onSignOut(self):
        SIC.mainWin.ui.hide()
        SIC.loginWin.ui.show()

    def queryWeather(self):
        cityName = self.ui.weatherComboBox.currentText()
        cityCode = self.transCityName(cityName)

        # 1、发送请求，获取数据
        url = f'http://wthrcdn.etouch.cn/weather_mini?citykey={cityCode}'
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
        self.ui.resultText.setText(result)
        print(result)

    def transCityName(self, cityName):
        cityCode = ''
        if cityName == '北京':
            cityCode = '101010100'
        elif cityName == '天津':
            cityCode = '101030100'
        elif cityName == '上海':
            cityCode = '101020100'
        elif cityName == '重庆':
            cityCode = '101040100'
        elif cityName == '哈尔滨':
            cityCode = '101050101'
        elif cityName == '河北':
            cityCode = '101090101'
        elif cityName == '河南':
            cityCode = '101180101'
        elif cityName == '安徽':
            cityCode = '101220101'
        elif cityName == '浙江':
            cityCode = '101210101'
        elif cityName == '福建':
            cityCode = '101230101'
        elif cityName == '甘肃':
            cityCode = '101160101'
        elif cityName == '广东':
            cityCode = '101280101'
        elif cityName == '广西':
            cityCode = '101300101'
        elif cityName == '贵州':
            cityCode = '101260101'
        elif cityName == '云南':
            cityCode = '101290101'
        elif cityName == '内蒙古':
            cityCode = '101080101'
        elif cityName == '江西':
            cityCode = '101240101'
        elif cityName == '湖北':
            cityCode = '101200101'
        elif cityName == '四川':
            cityCode = '101270101'
        elif cityName == '宁夏':
            cityCode = '101170101'
        elif cityName == '青海':
            cityCode = '101150101'
        elif cityName == '山东':
            cityCode = '101120101'
        elif cityName == '陕西':
            cityCode = '101110101'
        elif cityName == '山西':
            cityCode = '101100101'
        elif cityName == '新疆':
            cityCode = '101130101'
        elif cityName == '西藏':
            cityCode = '101140101'
        elif cityName == '台湾':
            cityCode = '101340101'
        elif cityName == '海南':
            cityCode = '101310101'
        elif cityName == '湖南':
            cityCode = '101250101'
        elif cityName == '江苏':
            cityCode = '101190101'
        elif cityName == '黑龙江':
            cityCode = '101050101'
        elif cityName == '吉林':
            cityCode = '101060101'
        elif cityName == '辽宁':
            cityCode = '101070101'

        return cityCode
    # 清除内容
    def clearResult(self):
        print('* clearResult  ')
        self.ui.resultText.clear()

    # 切换resultText中背景图片
    def choicPic(self):
        picNum = self.ui.PiccomboBox.currentText()
        httpPic = ":/background/images/" + picNum
        self.ui.resultText.setStyleSheet("background-image: url(" + httpPic + ");\n""color: rgb(0, 255, 0);")

if __name__ == '__main__':
    app = QApplication([])
    SIC.loginWin = Win_Login()
    SIC.loginWin.ui.show()
    app.exec()
