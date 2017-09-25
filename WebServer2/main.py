# coding:utf-8
from flask import Flask, session, redirect, url_for, escape, request, jsonify
import db
import os
import os.path
import sys
import json

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(PROJECT_ROOT, 'logs')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return jsonify({'hello':'world'})


@app.route('/login', methods=['POST'])
def login_handler():
    if request.method == 'POST':
        result = dict()
        username = request.form['username']
        password = request.form['password']
        ret = db.check_user(username, password)
        # error
        if ret[0] != 0:
            result['code'] = 1
            result['msg'] = 'error'
        else:
            result['code'] = 0
            result['msg'] = 'passed'
            result['groupID'] = ret[1][2]
            result['groupSize'] = ret[1][3]
            result['leader'] = ret[1][4]
            result['gender'] = ret[1][5]
            result['speed'] = ret[1][6]
        return jsonify(result)


@app.route('/updateResults',methods=['POST'])
def upload_results():
    if request.method == 'POST':
        result = dict()
        groupID = int(request.form['groupID'])
        username = request.form['username']
        userEvacTime = float(request.form['userEvacTime'])
        groupEvacTime = float(request.form['groupEvacTime'])
        ret = db.write_evac_time(groupID, username, userEvacTime, groupEvacTime)
        if ret:#success
            result['code'] = 0
        else:
            result['code'] = 1
        return jsonify(result)


@app.route('/uploadLogfile',methods=['POST'])
def upload_logfile():
    if request.method == 'POST':
        result = dict()
        try:
            filename = request.form['fileName']
            fileData = request.form['fileData']
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            with open(filePath, 'w') as fp:
                fp.writelines(fileData)
            result['code'] = 0
        except Exception,err:
            sys.stderr.write('ERROR: %s\n' % str(err))
            result['code'] = 1
        return jsonify(result)


@app.route('/uploadQuestionaire',methods=['POST'])
def upload_questionair():
    if request.method == 'POST':
        result = dict()
        try:
            dataStr = request.form['data']
            answers = dataStr.split(';')
            answers.insert(0,'1')#预留时间字段
            # 取用户名生成密码
            username = answers[1]
            password = abs(hash(username))%(10**4)
            # 把密码加到数组最后一个
            answers.append(password)
            # 插入数据库
            if db.insert_user_answers(answers):
                result['code'] = 0
                result['password'] = password
            else:
                result['code'] = 1
        except Exception,err:
            sys.stderr.write('ERROR: %s\n' % str(err))
            result['code'] = 1

        return jsonify(result)


@app.route('/checkUsername',methods=['GET'])
def check_username():
    if request.method == 'GET':
        result = dict()
        try:
            username = request.args.get('username')
            if db.check_username(username):# valid
                result['code'] = 0
            else:
                result['code'] = 1
        except Exception,err:
            sys.stderr.write('ERROR: %s\n' % str(err))
            result['code'] = 1
        return jsonify(result)


# 重新分配组
@app.route('/reassignGroup', methods=['GET'])
def reassign_group():
    if request.method == 'GET':
        result = dict()
        try:
            groupConf = request.args.get('groupConf').split(',')
            groupIDs, groupSizes, leaders = groupFromConfig(groupConf)
            if db.update_group(groupIDs, groupSizes, leaders):
                result['code'] = 0
                result['message'] = 'success'
            else:
                result['code'] = 1
        except Exception, err:
            sys.stderr.write('ERROR: %s\n' % str(err))
            result['code'] = 1
        return jsonify(result)


def groupFromConfig(groupConf):
    numInGroups = [int(gno) * (idx + 1) for idx, gno in enumerate(groupConf)]
    groupIDs = []
    leaders = []
    groupSizes = []

    # 生成单人组，id从17开始，leader都是1
    startID = 17
    for i in range(numInGroups[0]):
        leaders.append(1)
        groupSizes.append(1)
        groupIDs.append(startID)
        startID += 1

    # 多人组，id从1开始，每组第一个人是leader
    startID = 0
    for idx, no in enumerate(numInGroups[1:]):
        for i in range(no):
            if i % (idx + 2) == 0:  # 每组第一个人
                startID += 1
                leaders.append(1)
            else:
                leaders.append(0)
            groupIDs.append(startID)
            groupSizes.append(idx + 2)

    return groupIDs, groupSizes, leaders

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=9034)
