# -*-coding:utf-8-*-
# Authoe: Shen Shen
# Email: dslwz2002@163.com
__author__ = 'Shen Shen'

import sqlite3
import os
import sys
import math
import random

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
DBNAME = os.path.join(PROJECT_ROOT, 'participants.db')

def check_user(username, password):
    con = sqlite3.connect(DBNAME)
    with con:
        cur = con.cursor()
        cur.execute("select Username,Password,GroupID,GroupSize,Leader,Gender,Speed from participants where Username=?", (username,))
        record = cur.fetchone()
        # this user does not exists
        if record is None:
            return 1, None
        else:
            # wrong password
            if record[1] != password:
                return 2, None
            else:
                return 0, record

def write_evac_time(groupID, username, userEvacTime, groupEvacTime):
    con = sqlite3.connect(DBNAME)
    try:
        with con:
            cur = con.cursor()
            updateSql = "update participants set UserEvacTime=?,GroupEvacTime=? where GroupID=? and Username=?"
            cur.execute(updateSql, (userEvacTime, groupEvacTime, groupID, username))
            return True
    except:
        return False

def insert_user_answers(answers):
    con = sqlite3.connect(DBNAME)
    try:
        with con:
            cur = con.cursor()
            insertSql = "insert into questionaire values (?,?,?,?,?,?,?,?,?,?,?,?)"
            cur.execute(insertSql, tuple(answers))
            return True
    except Exception,err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return False

def check_username(username):
    con = sqlite3.connect(DBNAME)
    try:
        with con:
            cur = con.cursor()
            cur.execute("select * from questionaire where Username=?",(username,))
            return True if len(cur.fetchall()) == 0 else False
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return False

def update_group(groupIDs, groupSizes, leaders):
    con = sqlite3.connect(DBNAME)
    try:
        with con:
            cur = con.cursor()
            selectLeaderSql = "select Username from participants"
            cur.execute(selectLeaderSql)
            usernames = cur.fetchall()
            updateSql = "update participants set GroupID=?,GroupSize=?,Leader=? where Username=?"
            # shuffle once
            random.shuffle(usernames)
            for idx,name in enumerate(usernames):
                cur.execute(updateSql, (groupIDs[idx],groupSizes[idx],leaders[idx],name[0]))
            return True
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        return False

if __name__ == "__main__":
    # print(check_user('admin', 'admin'))
    # print(write_evac_time(1, 'test', 1234.4, 43.00))
    # print(insert_user_answers(['1','2','3','4','5','6','7','8','9','10',
    #                            '11','12','13','14','15','16','17','18','19','20',
    #                            '21','22','23','24','25']))
    # print(check_username('aa'))
    # print(check_username('1'))
    gdis = [17, 18, 19, 20, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6]
    gsizes = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]
    leaders = [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
    update_group(gdis, gsizes, leaders)
