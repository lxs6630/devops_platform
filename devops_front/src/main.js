import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import store from './store/store'
Vue.use(ElementUI);
Vue.use(VueResource);
Vue.config.productionTip = false;
Vue.http.get('http://www.devops.com:10000/api/login').then(response => {});
let djangocookie=getCookie('csrftoken');
Vue.http.headers.common['X-CSRFToken'] = djangocookie;//这里设置请求头
router.beforeEach((to, from, next) => {
if (to.path === '/login') {
    next()
  } else {
    if (!store.state.user ) {
      next({ path: '/login' })
    } else {
      next()
    }
  }
});
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});
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

