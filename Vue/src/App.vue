<template @click="click">
  <div id="app">
      <AppHeader /> 
       <child @simulate="simulate"></child>
        <router-view />
      <AppFooter />
  </div>
</template>

<script></script>
<script>
import Vue from 'vue'
import VueConfetti from 'vue-confetti'
import AppHeader from './components/AppHeader'
import AppFooter from './components/AppFooter'
import Vuetify from 'vuetify'
import { BIconX, BootstrapVue, IconsPlugin } from 'bootstrap-vue'
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
  mounted(){
    this.loadScript();
  },
  methods: {
    loadScript(){
      brython();
    },
    simulate(component, A, Beta, Qd, H, Tp, SimulationLength, hMax){
      if(component === "WaterContainer1"){
        __BRYTHON__.imported.WaterContainer1.run(A, Beta, Qd, H, Tp, SimulationLength, hMax);
      }
      else if(component === "WaterContainer2"){
        __BRYTHON__.imported.test_python.test(y, z);
      }
      else if(component === "WaterContainer3"){
        __BRYTHON__.imported.test_python.test(y, z);
      }
      else if(component === "WaterContainer4"){
        __BRYTHON__.imported.test_python.test(y, z);
      }
      
    }
  } 
}
</script>

<style>
:root {
  --primary-color: #88bdbc;
  --primary-color-dark: #254e58;
  --text-color: #112d32;
  --secondary-color-dark: #4f4a41;
  --secondary-color: #6e6658;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  min-height: 100%;
  min-width: 100%;
  margin: 0px;
}

.element {
  background-color: var(--secondary-color);
}

.web-content {
  display: block;
}

section {
  margin-top: 10%;
}

.title {
  font-size: 24px;
  font-weight: 600;
  text-align: center;
  color: var(--text-color);
}

</style>
