<template>
  <div id="app">
    <AppHeader />
    <AppFooter />
  </div>
</template>

<script>
import Vue from 'vue'
import VueConfetti from 'vue-confetti'
import AppHeader from './components/appHeader'
import AppFooter from './components/appFooter'
import Vuetify from 'vuetify'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.use(VueConfetti)
Vue.use(Vuetify)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter
  },
  data() {
      return {
        isModalVisible: false,
      };
    },
    methods: {
      showModal() {
        this.isModalVisible = true;
        this.$confetti.start();
      },
      closeModal() {
        this.isModalVisible = false;
      }
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  width: 100%;
  margin: 0px;
}
.element {
  background-color: rgba(203, 205, 206, 1) !important;
}
</style>
