#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
translator - Chinese/English Translation
@author sikasjc(sikasjc@163.com)
@date 2017.7.28
"""

import sys
import json
import urllib.request
import urllib.parse
import random
import hashlib

class Translator:
    appKey = '0b8802eb86c06476'
    api = 'https://openapi.youdao.com/api'
    translatorfrom = 'auto'
    translatorto = 'auto'
    key = 'dsAkIQlO9Pt7ThlmWISu2O8GBgXJbAvu'
    content = None

    def __init__(self, argv):
        q = ''
        if len(argv) > 0:
            q = ' '.join(argv)
            salt = str(random.randint(0, 9))
            sign = self.appKey + q + salt + self.key
            sign = self.keytomd5(sign)
            q = urllib.parse.quote(q.encode('utf-8'))
            self.api = self.api + '?'+ 'q=' + q + '&from=' + self.translatorfrom + \
                       '&to=' + self.translatorto + '&appKey=' + self.appKey + \
                       '&salt=' + salt + '&sign=' + sign
            self.translate()
        else:
            print('Please enter the word or sentence.')

    def keytomd5(self, str):
        m = hashlib.md5()
        m.update(str.encode('utf-8'))
        psw = m.hexdigest()
        return psw

    def translate(self):
        try:
            content = urllib.request.urlopen(self.api).read()
            self.content = json.loads(content.decode('utf-8'))
            self.parse()
        except Exception as e:
            print(e)

    def parse(self):
        errorcode = self.content['errorCode']
        if errorcode == '0': #translate successfully
            query = self.content['query']
            translations =  self.content['translation']

            try:
                us = self.content['basic']['us-phonetic']
                uk = self.content['basic']['uk-phonetic']
            except KeyError:
                uk = None
                us = None

            try:
                phonetic = self.content['basic']['phonetic']
            except KeyError:
                phonetic = None


            try:
                explains = self.content['basic']['explains']
            except KeyError:
                explains = None

            try:
                webexp = self.content['web']
            except KeyError:
                webexp = None

            print('----------translation----------\n')
            l = ''
            for translation in translations:
                l = l + translation
            print('{0}: {1}'.format(query, translation))

            print('\n----------basic explain----------\n')
            if us or uk:
                print('us: [{0}] uk: [{1}]'.format(us, uk))
            elif phonetic:
                print('phonetic: [{0}]'.format(phonetic))

            if explains:
                for explain in explains:
                    print('{0}'.format(explain))

            print('\n----------web explain----------\n')

            if webexp:
                for web in webexp:
                    print('{0}: {1}'.format(web['key'], ','.join(web['value'])))
            print('---------------------------------')
        else:
            print('errorcode: %s' % errorcode)
            print("""----------错误码----------------\n
101 缺少必填的参数，出现这个情况还可能是et的值和实际加密方式不对应
102 不支持的语言类型
103 翻译文本过长
104 不支持的API类型
105 不支持的签名类型
106 不支持的响应类型
107 不支持的传输加密类型
108 appKey无效
109 batchLog格式不正确
110 无相关服务的有效实例
111 开发者账号无效，可能是账号为欠费状态
201 解密失败，可能为DES,BASE64,URLDecode的错误
202 签名检验失败
203 访问IP地址不在可访问IP列表
301 辞典查询失败
302 翻译查询失败
303 服务端的其它异常
401 账户已经欠费停""")

if __name__ == '__main__':
    Translator(sys.argv[1:])
