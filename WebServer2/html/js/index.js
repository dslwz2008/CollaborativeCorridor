/**
 * Item Name :
 * Creater : peijiqiu
 * Email : peijiqiu@gmail.com
 * Created Date : 17/8/19.
 */
var app = new Vue({
  el: '#app',
  data: {
    title: '在线虚拟协同群组实验报名及调查问卷',
    loginname: '',
    questions: [
      {
        title: '用户名(英文与数字,长度6-20)：',
        type: 'text',
        val:'',
        checkuser: true
      },
      {
        title: '您的年龄：',
        type: 'select',
        val:'',
        options: [
          {
            text: '<=15',
            val: '1'
          },
          {
            text: '16-20',
            val: '2'
          },
          {
            text: '21-25',
            val: '3'
          },
          {
            text: '26-30',
            val: '4'
          },
          {
            text: '31-35',
            val: '5'
          },
          {
            text: '36-40',
            val: '6'
          },
          {
            text: '41-45',
            val: '7'
          },
          {
            text: '46-50',
            val: '8'
          },
          {
            text: '>50',
            val: '9'
          }
        ]
      },
      {
        title: '您的性别：',
        type: 'radio',
        name: 'gender',
        val: '',
        options: [
          {
            id: 'male',
            text: '男',
            val: '1'
          },
          {
            id: 'female',
            text: '女',
            val: '2'
          }
        ]
      },
      {
        title: '前进方向上遇到一个多人同伴群（如旅游团），当遇到的同伴群人数越多，您是否越想远离？',
        type: 'radio',
        name: 'ques1',
        val: '',
        options: [
          {
            id: 'ques1-1',
            text: '是',
            val: '1'
          },
          {
            id: 'ques1-2',
            text: '否',
            val: '2'
          }
        ]
      },
      {
        title: '前进方向上遇到一个多人同伴群，您会从这个同伴群两侧绕过还是从同伴群内部穿过？',
        type: 'radio',
        name: 'ques2',
        val: '',
        options: [
          {
            id: 'ques2-1',
            text: '两侧绕过',
            val: '1'
          },
          {
            id: 'ques2-2',
            text: '内部穿过',
            val: '2'
          }
        ]
      },
      {
        title: '您处于一个同伴群内，此时需要避让另外一个同伴群，您会怎么做？',
        type: 'radio',
        name: 'ques3',
        val: '',
        options: [
          {
            id: 'ques3-1',
            text: '先缩小与同伴间的距离，当仍然无法避让时，再调整同伴群结构',
            val: '1'
          },
          {
            id: 'ques3-2',
            text: '先调整同伴群结构，当仍然无法避让时，再缩小与同伴间的距离',
            val: '2'
          }
        ]
      },
      {
        title: '避让结束后，是否会恢复到避让前的同伴间距和结构？',
        type: 'radio',
        name: 'ques4',
        val: '',
        options: [
          {
            id: 'ques4-1',
            text: '是',
            val: '1'
          },
          {
            id: 'ques4-2',
            text: '否',
            val: '2'
          }
        ]
      },
      {
        title: '如何保持同伴群紧凑性？',
        type: 'radio',
        name: 'ques5',
        val: '',
        options: [
          {
            id: 'ques5-1',
            text: '所有成员向同伴群中心靠拢',
            val: '1'
          },
          {
            id: 'ques5-2',
            text: '所有成员向某个成员靠拢',
            val: '2'
          },
          {
            id: 'ques5-3',
            text: '保持同排成员紧凑，前后排紧凑性由后排成员控制',
            val: '3'
          },
          {
            id: 'ques5-4',
            text: '只保持同排成员紧凑，无需保持前后排成员紧凑',
            val: '4'
          }
        ]
      },
      {
        title: '多人的同伴群在行走过程中，需要考虑的因素有哪些？（多选）',
        type: 'checkbox',
        name: 'ques6',
        val: [],
        options: [
          {
            id: 'ques6-1',
            text: '每个成员都有可交流的邻近同伴，不被孤立',
            val: '1'
          },
          {
            id: 'ques6-2',
            text: '保持团队紧凑性',
            val: '2'
          },
          {
            id: 'ques6-3',
            text: '形成易于同伴群前进的结构',
            val: '3'
          },
          {
            id: 'ques6-4',
            text: '群内成员保持相近的行走速度',
            val: '4'
          }
        ]
      },
      {
        title: '选出您认为在现实场景中容易感知到的特征。（多选）',
        type: 'checkbox',
        name: 'ques7',
        val: [],
        options: [
          {
            id: 'ques7-1',
            text: '形状',
            val: '1'
          },
          {
            id: 'ques7-2',
            text: '大小',
            val: '2'
          },
          {
            id: 'ques7-3',
            text: '纹理',
            val: '3'
          },
          {
            id: 'ques7-4',
            text: '颜色',
            val: '4'
          },
          {
            id: 'ques7-5',
            text: '结构',
            val: '5'
          },
          {
            id: 'ques7-6',
            text: '距离',
            val: '6'
          },
          {
            id: 'ques7-7',
            text: '文字',
            val: '7'
          },
          {
            id: 'ques7-8',
            text: '光线',
            val: '8'
          },
          {
            id: 'ques7-9',
            text: '其他',
            val: '9'
          }
        ]
      }
    ],
    validuser: false,
    checkUserUrl: 'http://119.23.128.14:9934/checkUsername',
    uploadQuesUrl: 'http://119.23.128.14:9934/uploadQuestionaire'
  },
  methods: {
    checkUserName: function(name, e) {
      var root = this;
      var reg = /^[\da-zA-Z]{6,20}/;
      if(!reg.test(name)) {
        alert('用户名采用英文与数字,长度6-20');
        e.target.style.borderColor = 'red';
        root.validuser = false;
        return
      }
      this.$http.get(this.checkUserUrl, {username:name}).then(function(res){
        if(!res.body.code == 0) {
          alert('该用户名已存在,请更换');
          e.target.style.borderColor = 'red';
          root.validuser = false;
        } else {
          e.target.style.borderColor = '#dbdbdb';
          root.loginname = name;
          root.validuser = true;
        }
      },function(res){
        alert('error');
      });
    },

    submitQuestion: function() {
      if(!this.validuser) {
        alert('用户名已存在,请重新填写');
        return;
      }

      var flag = true;
      var dataArr = [];
      var data = '';
      for(var i=0; i < this.questions.length; i++) {

        if(this.questions[i].type === 'radio' || this.questions[i].type === 'text' || this.questions[i].type === 'select') {
          var answer = this.questions[i].val.replace(/(^\s*)|(\s*$)/g, "");
          if(!answer) {
            flag = false;
            break;
          } else {
            dataArr.push(answer);
          }
        } else if(this.questions[i].type === 'checkbox') {
          if(!this.questions[i].val.length) {
            flag = false;
            break;
          } else {
            dataArr.push(this.questions[i].val.join(','));
          }
        }
      }


      if(!flag) {
        alert('您还有未填写的试题,请填写完整');
      } else {
        this.$http.post(this.uploadQuesUrl, {"data":dataArr.join(';')},
          {emulateJSON:true,headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).then(function(res){
          if(res.body.code == 0) {
            location.href = 'result.html?name='+this.loginname+'&pwd='+ res.body.password;
          } else {
            alert('error')
          }
        },function(res){
          alert('error');
        });
      }
    }
  }
});