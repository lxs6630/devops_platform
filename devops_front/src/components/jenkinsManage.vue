<template>
  <div class="order-wrap">
    <h3>jenkins项目</h3>
    <div class="order-list-choose">
      <div class="order-list-option">
      <el-autocomplete
      v-model="appInfo.project"
      :fetch-suggestions="querySearchAsync"
      placeholder="请输入内容"
      @select="handleSelect"
      ></el-autocomplete>
      </div>
      <div class="order-list-option">
        操作:
      </div>
      <el-button type="primary" round >启动</el-button>
      <el-button type="danger"  round>停止</el-button>
      <el-button type="primary"  round @click=log>log</el-button>
      <el-dialog
        title="jekins日志"
        :visible.sync="centerDialogVisible"
        width="90%"
        center
         >
        <pre style="white-space: pre-wrap; word-wrap: break-word;">{{ret.msg}}</pre>
       </el-dialog>
    </div>
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
        restaurants: [],
        state4: '',
        timeout:  null,
        appInfo: {
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
        this.$http.post('http://www.devops.com:10000/api/jekins_manage', sendDate).then((response) => {
          // success callback
          this.ret.msg = response.data.log;
        }, (response) => {
//               console.log("error");
          // error callback
        });
      },
      log() {
        this.centerDialogVisible = true;
        this.appInfo.action='log';
        let sendDate = JSON.stringify(this.appInfo);
        this.ret.msg=null;
        this.$http.post('http://www.devops.com:10000/api/jenkins_manage', sendDate).then((response) => {
          // success callback
          this.ret.msg = response.data.log;
        }, (response) => {
//               console.log("error");
          // error callback
        });
      },
      querySearchAsync(queryString, cb) {
        let restaurants = this.restaurants;
        let results = queryString ? restaurants.filter(this.createStateFilter(queryString)) : restaurants;
        clearTimeout(this.timeout);
        this.timeout = setTimeout(() => {
          cb(results);
        }, 100 * Math.random());
      },
      createStateFilter(queryString) {
        return (state) => {
          return (state.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      handleSelect(item) {
//        console.log(item);
      },
    },
          mounted() {
      this.$http.get('http://www.devops.com:10000/api/get_jobs').then(response => {
          this.restaurants=response.data.jobs;
//          console.log(this.restaurants);
        }//, response => {
//          console.log("error");}
        );
    }
  }
</script>
