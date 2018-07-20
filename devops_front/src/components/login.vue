<template>
  <div class="main">
    <div class="login">
    <h1>应用管理系统</h1>
      <div class="inset"  >
  <el-form class="el-form" ref="form" >
      <h2>管理登录</h2>
    <el-form-item label="用户"  prop="name">
        <el-input type="text" auto-complete="off" class=input_text v-model="authInfo.username" placeholder="请输入用户名"></el-input>
    </el-form-item>
    <el-form-item label="密码"  prop="password">
        <el-input type="password"  class=input_text auto-complete="off" v-model="authInfo.password" placeholder="请输入密码"></el-input>
    </el-form-item>
    <el-form-item>
      <div class="sign">
        <!-- 点击进行登录提交 -->
        <el-button  class="submit" type="primary" @click="submit" >登录</el-button>
        <div style="color: red">{{req.msg}}</div>
        <!-- 点击重置表单 -->
    </div>
    </el-form-item>
</el-form>
    </div>
</div>
    </div>
</template>
<style >
/* reset */
html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, dl, dt, dd, ol, nav ul, nav li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video,input {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
	font-family: "Segoe UI", "Lucida Grande", Helvetica, Arial, "Microsoft YaHei", FreeSans, Arimo, "Droid Sans", "wenquanyi micro hei", "Hiragino Sans GB", "Hiragino Sans GB W3", FontAwesome, sans-serif;}
article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section {
	display: block;
}
ol, ul {
	list-style: none;
	margin: 0px;
	padding: 0px;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after, q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
/* start editing from here */
a {
	text-decoration: none;
}
img {
	max-width: 100%;
}
/*end reset*/
/****-----start-body----****/
body {
	background-color: #BFEFFF ;
}
.main {
	margin: 5em auto 0;
	width: 22%;
}
h1 {
	font-size: 3.2em;
	padding-bottom: 28px;
	color: #595959;
	text-align: center;
}
h2 {
	font-size: 2.2em;
	padding-bottom: 28px;
	color: #0091e6;
	text-align: center;
}
.login {
	padding: 2em 0;
}
.inset {
	position: relative;
	background: #fff;
	padding: 2.5em;
	border-radius: 0.3em;
	-webkit-border-radius: 0.3em;
	-o-border-radius: 0.3em;
	-moz-border-radius: 0.3em;
	box-shadow: 0px 0px 15px #545454;
}
.el-form {
	display: block;
	font-size: 1.0em;
	color: #333;
	font-weight: 400;
}
.textbox{
  font-size: 2.0em
}
.input_text {
	padding: 0px;
	width: 93.4%;
	font-size: 1.3em;
	color: #666666;
	background: #f0f0f0;
	border: none;
	font-weight:400;
	outline: none;
	-webkit-transition: all 0.3s ease-out;
	-moz-transition: all 0.3s ease-out;
	-ms-transition: all 0.3s ease-out;
	-o-transition: all 0.3s ease-out;
	transition: all 0.3s ease-out;
	border-radius: 0.2em;
	-webkit-border-radius: 0.2em;
	-o-border-radius: 0.2em;
	-moz-border-radius: 0.2em;
}
input[type="text"]:hover, input[type="Password"]:hover, #active {
	border: none;
	outline: none;
}
.sign {
	padding: 10px 0 0;
	text-align: center;
}
.submit {
  text-align: center;
	background:#0091e6;
	border: none;
	outline: none;
	padding:8px 30px;
	cursor: pointer;
	color: #FFF;
	font-size: 1.4em;
	border-radius: .3em;
	-webkit-border-radius: .3em;
	-moz-border-radius: .3em;
	-o-border-radius: .3em;
	transition: 0.5s all;
	-webkit-transition: 0.5s all;
	-moz-transition: 0.5s all;
	-o-transition: 0.5s all;
	font-weight: 600;
	margin: 0 auto;
}
.submit:hover {
	background: #C5C5C5;
}
.copy-right {
	text-align: center;
	width: 97%;
	margin: 10em auto 0em;
}
.copy-right p {
	color: #FFF;
	font-size: 1em;
}
.copy-right p a {
	font-size: 1em;
	font-weight: 600;
	color: #1567A5;
	-webkit-transition: all 0.3s ease-out;
	-moz-transition: all 0.3s ease-out;
	-ms-transition: all 0.3s ease-out;
	-o-transition: all 0.3s ease-out;
	transition: all 0.3s ease-out;
}
.copy-right p a:hover {
	color: #fff;
}
/*----start-responsive design-----*/
@media (max-width:1440px) {
.main {
	width: 25%;
}
h1 {
	font-size: 2.2em;
}
.copy-right {
	margin: 5em auto 2em;
}
}
@media (max-width:1080px) {
.main {
	width: 31%;
	margin: 5em auto 0;
}
.copy-right {
	width: 97%;
	margin: 3em auto 1em;
}
}
@media (max-width:1024px) {
.main {
	width: 31%;
	margin: 5em auto 0;
}
.copy-right {
	width: 97%;
	margin: 3em auto 1em;
}
}
@media (max-width:991px) {
h1 {
	font-size: 2em;
}
}
@media (max-width:800px) {
.main {
	width: 39%;
}
}
@media (max-width:768px) {
.main {
	width: 42%;
	margin: 11em auto 0;
}
}
@media (max-width:640px) {
.main {
	width: 48%;
}
h1 {
	font-size: 2.1em;
}
}
@media (max-width:600px) {
h1 {
	font-size: 2em;
}
}
@media (max-width:480px) {
.main {
	width: 70%;
}
}
@media (max-width:320px) {
.main {
	width: 95%;
	margin: 1em auto 0;
}
.copy-right {
	margin: 1em auto 0;
}
.inset {
	padding: 2em;
}
h1 {
	font-size: 1.9em;
}
.login {
	padding: 2em 0 0;
}
}
</style>
<script>
  import { mapActions } from 'vuex'
//  import { USER_SIGNIN } from '../store/store'
  import crypto from 'crypto'
  export default {
    data() {
      return {
        DjangoCookie:null,
        books: [],
        authInfo: {
          username: null,
          password: null
        },
        req: {
          msg: null,
        },
        form: {
          user: null
        }
      }
    },
    methods: {
      ...mapActions(["login"]),
      getmd5(pwd) {
        let md5 = crypto.createHash("md5");
        md5.update(pwd);
        let a = md5.digest('hex');
        return a
      },
      submit: function () {
        let pwd = this.authInfo.password;
        this.authInfo.password = this.getmd5(pwd);
        let formData = JSON.stringify(this.authInfo); // 这里才是你的表单数据
        this.$http.post('http://www.devops.com:10000/api/login', formData).then((response) => {
          // success callback
          this.req.msg = response.data.msg;
          this.req.respCode = response.data['resp_code'];
          if (this.req.respCode === "0000") {
            this.form.user = response.data.username;
            this.$store.dispatch("login", this.form);
            this.$router.push({path: '/manage'});
          }
        }, (response) => {
//               console.log("error");
          // error callback
        });
      },
      display() {
        // GET /someUrl URL为django接口地址
        this.$http.get('http://www.devops.com:10000/api/show_books').then(response => {
          this.books = response.data.list;
          console.log(this.books[0].fields.book_name);
          // get body data
          // this.someData = response.body;

        }, response => {
          console.log("error");
        });
      },

    },
//    mounted() {
//      this.$http.get('http://127.0.0.1:8000/api/login').then(response => {
//          console.log(response);
////            this.DjangoCookie=response.data.csrf_cookie;
//          this.DjangoCookie=getCookie('csrftoken');
//           console.log(getCookie('csrftoken'));
////           console.log(this.DjangoCookie);
////          console.log(this.restaurants);
//      }, response => {
//        console.log("error");
//      });
//    }
  }
  function getCookie(name){  //获取cookie函数
    name = name + "=";
    let start = document.cookie.indexOf(name),
        value = null;
    if(start>-1){
        let end = document.cookie.indexOf(";",start);
        if(end === -1){
            end = document.cookie.length;
        }
        value = document.cookie.substring(start+name.length,end);
    }
    return value;
}
</script>
