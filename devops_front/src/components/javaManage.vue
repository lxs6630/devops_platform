<template>
  <div class="order-wrap">
    <h3>java项目</h3>
    <div class="order-list-choose">
      <div class="order-list-option">
        ip：
        <input  type="text"  class="order-query" placeholder="请输入IP" v-model="appInfo.ip"/>
      </div>
      <div class="order-list-option">
        项目名：
       <input type="text"   class="order-query" placeholder="请输入项目名" v-model="appInfo.project"/>
      </div>
      <div class="order-list-option">
        操作:
      </div>
      <el-button type="primary" round >启动</el-button>
      <el-button type="primary"  round>重启</el-button>
      <el-button type="danger"  round>停止</el-button>
      <el-button type="primary"  round @click=start>log</el-button>
      <el-dialog
        title="java应用日志"
        :visible.sync="centerDialogVisible"
        width="60%"
        center
         >
        <pre style="white-space: pre-wrap; word-wrap: break-word;">{{ret.msg}}</pre>
       </el-dialog>
    </div>
    <!--<div class="order-list-table">-->
      <!--<table>-->
        <!--<tr>-->
          <!--<th v-for="head in tableHeads" @click="changeOrderType(head)" :class="{active:head.active}">{{ head.label }}</th>-->
        <!--</tr>-->
        <!--<tr v-for="item in tableData" :key="item.period">-->
          <!--<td v-for="head in tableHeads">{{ item[head.key] }}</td>-->
        <!--</tr>-->
      <!--</table>-->
    <!--</div>-->
  </div>
</template>
<style scoped>
.order-wrap {
  width: 1200px;
  min-height: 800px;
  margin: 20px auto;
  overflow: hidden;
}
.order-wrap h3 {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 20px;
}
.order-query {
  height: 25px;
  line-height: 25px;
  border: 1px solid #e3e3e3;
  outline: none;
  text-indent: 10px;
}
.order-list-option {
  display: inline-block;
  padding-left: 15px;
}
.order-list-option:first-child {
  padding-left: 0;
}
.order-list-table {
  margin-top: 20px;
}
.order-list-table table {
  width: 100%;
  background: #fff;
}
.order-list-table td,
.order-list-table th {
  border: 1px solid #e3e3e3;
  text-align: center;
  padding: 10px 0;
}
.order-list-table th {
  background: #4fc08d;
  color: #fff;
  border: 1px solid #4fc08d;
  cursor: pointer;
}
.order-list-table th.active {
  background: #35495e;
}
</style>
<script>
  export default {
    data() {
      return {
        centerDialogVisible: false,
        appInfo: {
          ip: null,
          project: null,
          action: null
        },
        ret: {
          msg: null,
        },
        form: {
          user: null
        }
      }
    },
    methods: {
      start() {
        this.centerDialogVisible = true;
        this.appInfo.action = 'start';
        let sendDate = JSON.stringify(this.appInfo);
        this.ret.msg=null;
        this.$http.post('http://www.devops.com:10000/api/java_manage', sendDate).then((response) => {
          // success callback
          this.ret.msg = response.data.log;
//          console.log(response.data.log);
//          if (this.req.respCode === "0000") {
//            this.form.user = response.data.username;
//            this.$store.dispatch("login", this.form);
//            console.log(this.$store.state.user);
//            this.$router.push({path: '/manage'});
//          }
        }, (response) => {
//               console.log("error");
          // error callback
        });
      },
      stop() {
        this.appInfo.action = 'stop';
        let sendDate = JSON.stringify(this.appInfo);
        this.ret.msg=null;
        this.$http.post('http://www.devops.com:10000/api/java_manage', sendDate).then((response) => {
          // success callback
          this.ret.msg = response.data.log;
//          console.log(response.data.log);
//          if (this.req.respCode === "0000") {
//            this.form.user = response.data.username;
//            this.$store.dispatch("login", this.form);
//            console.log(this.$store.state.user);
//            this.$router.push({path: '/manage'});
//          }
        }, (response) => {
//               console.log("error");
          // error callback
        });
      }
    }
  }
</script>
