import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import manage from '@/components/manage'
import jenkinsManage from '@/components/jenkinsManage'
import javaManage from '@/components/javaManage'
Vue.use(Router);
// Router.beforeEach((to, from, next) => {
//  // 若userkey不存在并且前往页面不是登陆页面，进入登陆
//  // 若userkey存在并且前往登陆页面，进入主页
//  const userName = localStorage.getItem('userName');
//  if (!userName && to.path !== '/test') {
//   next({
//    path: '/test',
//    query: { redirect: to.fullPath }
//   })
//  } else if (userName && to.path === '/test') {
//   next({ path: '/manage' })
//  } else {
//   next()
//  }
// });
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path:'/',
      redirect:'/manage'
    },
    {
      path:'*',
      redirect:'/manage'
    },
    {
      path:'/manage',
      name:'manage',
      // redirect: '/manage/javamanage',
      component:manage,
      children:[{
          name:'javaManage',
					path: 'javamanage',
					component: javaManage
				},
				{
          name:'jenkinsManage',
					path: 'jenkinsmanage',
					component: jenkinsManage
				}
				]
      }
  ]
})
