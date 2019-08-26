import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog

import json
import base64
import urllib
import urllib.request

""" 你的 APPID AK SK """
# http://ai.baidu.com/docs#/OCR-Pricing/top 申请地址

# API_KEY 为官网获取的AK， SECRET_KEY 为官网获取的SK


API_KEY = ''#官网获取的AK
SECRET_KEY = ''#官网获取的SK


class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(724, 489)
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(96, 140, 311, 301))
        self.image.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0);")
        self.image.setObjectName("image")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(110, 50, 221, 31))
        self.widget.setObjectName("widget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)

        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(96, 90, 318, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        # 新建按钮
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(450, 50, 201, 401))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setWordWrap(True)

        self.label_3.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像识别工具"))
        self.label.setText(_translate("Form", "选择识别类型："))

        self.comboBox.setItemText(0, _translate("Form", "银行卡"))
        self.comboBox.setItemText(1, _translate("Form", "植物"))
        self.comboBox.setItemText(2, _translate("Form", "动物"))
        self.comboBox.setItemText(3, _translate("Form", "通用票据"))
        self.comboBox.setItemText(4, _translate("Form", "营业执照"))
        self.comboBox.setItemText(5, _translate("Form", "身份证"))
        self.comboBox.setItemText(6, _translate("Form", "车牌号"))
        self.comboBox.setItemText(7, _translate("Form", "驾驶证"))
        self.comboBox.setItemText(8, _translate("Form", "行驶证"))
        self.comboBox.setItemText(9, _translate("Form", "车型"))
        self.comboBox.setItemText(10, _translate("Form", "Logo"))

        self.label_2.setText(_translate("Form", "选择要识别的图片："))
        self.pushButton.setText(_translate("Form", "选择..."))
        self.label_3.setText(_translate("Form", "显示识别结果"))
        self.pushButton_2.setText(_translate("Form", "复制到剪切版"))
        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.copyText)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.label_3.text())

    def openfile(self):
        self.download_path = QFileDialog.getOpenFileName(self.widget1, "选择要识别的图片", "/", "Image Files(*.jpg *.png)")

        if not self.download_path[0].strip():
            pass
        else:

            self.lineEdit.setText(self.download_path[0])
            pixmap = QPixmap(self.download_path[0])
            scaredPixmap = pixmap.scaled(QSize(311, 301), aspectRatioMode=Qt.KeepAspectRatio)
            self.image.setPixmap(scaredPixmap)
            self.image.show()
            self.typeTp()
            pass

    def typeTp(self):
        # 银行卡识别
        if self.comboBox.currentIndex() == 0:
            self.get_bankcard(self.get_token())
            pass
        # 植物识别
        elif self.comboBox.currentIndex() == 1:
            self.get_plant(self.get_token())
            pass
        # 动物识别
        elif self.comboBox.currentIndex() == 2:
            self.get_animal(self.get_token())
            pass
        #通用票据识别识别
        elif self.comboBox.currentIndex() == 3:
            self.get_vat_invoice(self.get_token())
            pass
        # 营业执照识别
        elif self.comboBox.currentIndex() == 4:
            self.get_business_licensev(self.get_token())
            pass
        # 身份证识别
        elif self.comboBox.currentIndex() == 5:
            self.get_idcard(self.get_token())
            pass
        # 车牌号识别
        elif self.comboBox.currentIndex() == 6:
            self.get_license_plate(self.get_token())
            pass
        # 驾驶证识别
        elif self.comboBox.currentIndex() == 7:
            self.get_driving_license(self.get_token())
            pass
        # 行驶证识别
        elif self.comboBox.currentIndex() == 8:
            self.get_vehicle_license(self.get_token())
            pass
        # 车型识别
        elif self.comboBox.currentIndex() == 9:
            self.get_car(self.get_token())
            pass
        # Logo识别
        elif self.comboBox.currentIndex() == 10:
            self.get_logo(self.get_token())
            pass
        pass


    def get_token(self):

        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_KEY + '&client_secret=' + SECRET_KEY
        request = urllib.request.Request(host)
        request.add_header('Content-Type', 'application/json; charset=UTF-8')
        response = urllib.request.urlopen(request)
        content = response.read()
        if (content):
            print(content)
            print(json.loads(content)['access_token'])
            self.access_token = json.loads(content)['access_token']
            return self.access_token
    # 0 银行卡识别
    def get_bankcard(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/bankcard"
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            bankcards = json.loads(content)
            strover = '识别结果：\n'
            try:
                # 判断银行卡类型
                if bankcards['result']['bank_card_type']==0:
                    bank_card_type='不能识别'
                elif bankcards['result']['bank_card_type']==1:
                    bank_card_type = '借记卡'
                elif bankcards['result']['bank_card_type'] == 2:
                    bank_card_type = '信用卡'
                strover += '  卡号：{} \n  银行：{} \n  类型：{} \n'.format(bankcards['result']['bank_card_number'], bankcards['result']['bank_name'],bank_card_type)

            except BaseException:
                error_msg = bankcards['error_msg']
                strover += '  错误：\n {} \n '.format(error_msg)

            self.label_3.setText(strover)
    # 1植物识别
    def get_plant(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"

        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            plants = json.loads(content)
            strover = '识别结果：\n'
            try:
                i = 1
                for plant in plants['result']:
                    strover += '{} 植物名称：{} \n'.format(i, plant['name'])
                    i += 1
            except BaseException:
                error_msg = plants['error_msg']
                strover += '  错误：\n {} \n '.format(error_msg)
            self.label_3.setText(strover)
    # 2动物识别
    def get_animal(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img, "top_num": 6}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            animals = json.loads(content)
            strover = '识别结果：\n'
            try:
                i = 1
                for animal in animals['result']:
                   strover += '{} 动物名称：{} \n'.format(i, animal['name'])
                   i += 1
            except BaseException:
                error_msg = animals['error_msg']
                strover += '  错误：\n {} \n '.format(error_msg)
            self.label_3.setText(strover)
    # 3 通用票据识别
    def get_vat_invoice(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/receipt"
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            receipts = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result=receipts['words_result']
                for word_result in words_result:
                    #票据内容
                    InvoiceType =word_result['words']
                    strover += ' {} '.format(InvoiceType)
            except BaseException:
                error_msg = receipts['error_msg']
                strover += '  错误：\n {} \n '.format(error_msg)
            self.label_3.setText(strover)
    # 4 营业执照识别
    def get_business_licensev(self,access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/business_license"

        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            business_licenses = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result=business_licenses['words_result']

                Unit_name = words_result['单位名称']['words']
                strover += '  单位名称：\n  {} \n '.format(Unit_name)

                legal_person = words_result['法人']['words']
                strover += '  法人：{} \n '.format(legal_person)

                Term_of_validity = words_result['有效期']['words']
                strover += '  有效期：{} \n '.format(Term_of_validity)

                ID_number = words_result['证件编号']['words']
                strover += '  证件编号：{} \n '.format(ID_number)

                Social_Credit_Code = words_result['社会信用代码']['words']
                strover += '  社会信用代码：{} \n '.format(Social_Credit_Code)

                address = words_result['地址']['words']
                strover += '  地址：\n{}\n '.format(address)
            except BaseException:
                error_msg = business_licenses['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    #5 身份证识别
    def get_idcard(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img, "id_card_side": "front"}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            idcards = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result = idcards['words_result']

                Citizenship_number = words_result['公民身份号码']['words']
                strover += '  公民身份号码：\n{} \n '.format(Citizenship_number)

                Nation = words_result['民族']['words']
                strover += '  民族：{} \n '.format(Nation)

                Full_name = words_result['姓名']['words']
                strover += '  姓名：{} \n '.format(Full_name)
                # 住址
                address = words_result['住址']['words']
                strover += '  住址：\n{} \n '.format(address)
            except BaseException:
                error_msg = idcards['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)

            self.label_3.setText(strover)
    #6 车牌号识别
    def get_license_plate(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"

        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            license_plates = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result = license_plates['words_result']

                number = words_result['number']
                strover += '  车牌号：{} \n '.format(number)
            except BaseException:
                error_msg = license_plates['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)
    #7 驾驶证识别
    def get_driving_license(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/driving_license"
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            driving_licenses = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result = driving_licenses['words_result']
                Citizenship_number = words_result['证号']['words']
                strover += '  证号： {} \n '.format(Citizenship_number)

                Full_name = words_result['准驾车型']['words']
                strover += ' 准驾车型：{} \n '.format(Full_name)

                name = words_result['姓名']['words']
                strover += ' 姓名： {} \n '.format(name)

                nationality = words_result['国籍']['words']
                strover += ' 国籍： {} \n '.format(nationality)

                date_of_birth = words_result['出生日期']['words']
                strover += ' 出生日期： {} \n '.format(date_of_birth)

                sex = words_result['性别']['words']
                strover += ' 性别： {} \n '.format(sex)

                first_certificate_date = words_result['初次领证日期']['words']
                strover += ' 初次领证日期： {} \n '.format(first_certificate_date)

                Nation = words_result['有效期限']['words']

                to = words_result['至']['words']
                strover += ' 有效期限：{}至{}\n '.format(Nation,to)

                address = words_result['住址']['words']
                strover += ' 住址：\n{} \n '.format(address)
            except BaseException:
                error_msg = driving_licenses['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    #8 行驶证识别
    def get_vehicle_license(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_license"
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            vehicle_licenses = json.loads(content)
            strover = '识别结果：\n'
            try:
                words_result = vehicle_licenses['words_result']
                brand_model = words_result['品牌型号']['words']
                strover += '  品牌型号： {} \n '.format(brand_model)

                date_of_certification = words_result['发证日期']['words']
                strover += ' 发证日期：{} \n '.format(date_of_certification)

                use_nature = words_result['使用性质']['words']
                strover += ' 使用性质： {} \n '.format(use_nature)

                engine_number = words_result['发动机号码']['words']
                strover += ' 发动机号码： {} \n '.format(engine_number)

                date_of_registration = words_result['注册日期']['words']
                strover += ' 注册日期： {} \n '.format(date_of_registration)

                number_number = words_result['号牌号码']['words']
                strover += ' 号牌号码： {} \n '.format(number_number)

                vehicle_identification = words_result['车辆识别代号']['words']
                strover += ' 车辆识别代号： {} \n '.format(vehicle_identification)

                vehicle_type = words_result['车辆类型']['words']
                strover += ' 车辆类型： {} \n '.format(vehicle_type)
                owner = words_result['所有人']['words']
                strover += ' 所有人：\n{} \n '.format(owner)

                address = words_result['住址']['words']
                strover += ' 住址：\n{} \n '.format(address)
            except BaseException:
                error_msg = vehicle_licenses['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    # 9获取车型信息
    def get_car(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"image": img, "top_num": 5}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            cars = json.loads(content)
            strover = '识别结果：\n'
            try:
                i = 1
                for car in cars['result']:
                    strover += '{} 车型：{} \n  年份：{} \n'.format(i, car['name'], car['year'])
                    i += 1
            except BaseException:
                error_msg = cars['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    # 10获取logo信息
    def get_logo(self, access_token):
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/logo"
        f = self.get_file_content(self.download_path[0])
        img = base64.b64encode(f)
        params = {"custom_lib": False, "image": img}
        params = urllib.parse.urlencode(params).encode('utf-8')
        request_url = request_url + "?access_token=" + access_token
        request = urllib.request.Request(url=request_url, data=params)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        response = urllib.request.urlopen(request)
        content = response.read()
        if content:
            logos = json.loads(content)
            strover = '识别结果：\n'
            try:
                i = 1
                for logo in logos['result']:
                    strover += '{} Logo名称：{} \n'.format(i, logo['name'])
                    i += 1
            except BaseException:
                error_msg = logos['error_msg']
                strover += '  错误：\n  {} \n '.format(error_msg)
            self.label_3.setText(strover)

    # 读取图片
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
