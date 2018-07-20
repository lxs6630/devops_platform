import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex);
export default  new Vuex.Store({
  state: JSON.parse(localStorage.getItem('user')) || {},
  mutations: {
    Login(state, user) {
      localStorage.setItem('user', JSON.stringify(user));
      Object.assign(state, user)
    },
    Logout(state) {
      localStorage.removeItem('user');
      Object.keys(state).forEach(k => Vue.delete(state, k))
    }
  },
  actions: {
    login({commit}, user) {
      commit("Login", user)
    },
    logout({commit}) {
      commit("Logout")
    }
  }
})
