<template>
  <div>
    <el-menu
      router
      default-active="$route.path"
      class="el-menu-demo"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="/manage/javamanage">java应用</el-menu-item>
      <el-menu-item index="/manage/jenkinsmanage" >jekins</el-menu-item>
      <el-menu-item index="" class="floatR" @click="loginOut">注销</el-menu-item>
      <el-menu-item  index="" class="floatR">{{user}}</el-menu-item>
    </el-menu>
    <keep-alive>
      <router-view/>
    </keep-alive>
  </div>
</template>

<style>
  .floatR{
    float: right !important;
}
</style>
<script>
  import { mapState } from 'vuex'
  export default {
//    data() {
//      return {
//        activeIndex: '1',
//        activeIndex2: '1'
//      }
    computed: mapState({ user: state => state.user }),
    data(){
    return{
      userName: sessionStorage.userName
    }
  },
  methods:{
    loginOut() {
  this.$confirm('您确定要退出吗?', '退出管理平台', {
   confirmButtonText: '确定',
   cancelButtonText: '取消'
  }).then(() => {
   const info = {
    'user': sessionStorage.getItem('user')
   };
   this.$store.dispatch('logout', info).then(() => {
    this.$router.push({ path: '/login' })
   }).catch(() => {
   })
  }).catch(() => {

  })
 }

  }
  }
</script>
