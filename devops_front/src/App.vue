<template>
  <div id="app">
    <keep-alive>
      <router-view/>
    </keep-alive>
  </div>
</template>

<script>
export default {
  name: 'App'
//    data(){
//    return{
//      userName: sessionStorage.userName
//    }
//  },
//
//  methods:{
//    //子组件(register)将用户名传过来
//    userSignIn(userName){
//      sessionStorage.userName = userName;
//      this.userName = sessionStorage.userName;
//    }
//  }
}
//@userSignIn="userSignIn"
</script>

<!--<style src="../../static/bootstrap/css/bootstrap.css">-->

<!--</style>-->
