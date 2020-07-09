import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import store from './store'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false
Vue.prototype.$axios = axios

new Vue({
  vuetify,
  store,
  router,
  axios,
  render: h => h(App)
}).$mount('#app')
