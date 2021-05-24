<template @click="click">
  <div id="app">
    <AppHeader />
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
import LoadScript from 'vue-plugin-load-script'
import WaterContainer1Vue from './views/WaterContainer1.vue'
import CustomeChartVue from './components/CustomeChart.vue'
import axios from 'axios'
Vue.use(VueConfetti)
Vue.use(Vuetify)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(LoadScript)

export default {
  name: 'App',
  components: {
    AppHeader,
    AppFooter
  },
  created(){
    this.loadPythonScript();
    this.preventButtonFuction();
  },
  emits: ['updateChart'],
  data(){
    return {
      freezeButtons: true,
      logged: false,
      user: null
    }
  },
  methods: {
    loadPythonScript(){
      const sleep = ms => {
        return new Promise(resolve => setTimeout(resolve, ms));
      }
      const asyncLoop = async _ => {
    
        for (let index = 0; index < 10; index++) {
          const res = await sleep(500).then(()=> { return typeof pyodide });
          if(res === "object") break;
        }
      } 
      // get script in asynchronous loop
      this.$loadScript('https://cdn.jsdelivr.net/pyodide/v0.17.0a2/full/pyodide.js')
      .then(()=> {
        asyncLoop().then(()=> {
          fetch('/python/WaterContainer1.py')
            .then(res => res.text())
            .then((text) => pyodide.runPython(text))
            this.freezeButtons = false;
        });
      })
      .catch(()=>{ alert('Błąd podczas ładowania pliku. Wczytaj stronę ponownie')});
    },
    simulate(component, A, Beta, Qd, H, hMax, Tp, SimulationLength){
      // run method from python script
      this.freezeButtons = true;
      console.log(A, Beta, Qd, H, hMax, Tp, SimulationLength);
      pyodide.runPythonAsync(`run${component}(${A}, ${Beta}, ${Qd}, ${H}, ${hMax}, ${Tp}, ${SimulationLength})`)
        .then((res)=>{ 
          const result = this.$children.find(child => { return child.$options.name === component });
          if(component === "WaterContainer1") result.$data.volume = res.toJs();
        })
    },
    preventButtonFuction(){
      document.addEventListener("click", e => {
        if(this.freezeButtons) {
          e.stopPropagation();
          e.preventDefault();
        }
      }, true);

      document.body.style.opacity = 0.6;
    },
    disableButtons(value){
      var buttons = document.querySelectorAll('button');
      [].forEach.call(buttons, function(button) {
        button.disabled = value;
      });
    }
  },
  watch:{
    freezeButtons: function(){
      if(this.freezeButtons){
        document.body.style.opacity = 0.6;
        this.disableButtons(true);
      }
      else {
        document.body.style.opacity = 1;
        this.disableButtons(false);
      }
    }
  }
}
</script>

<style lang="scss">
@import "@/scss/variables.scss";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  margin: 0px;
}

.element {
  background-color: $secondary-color;
}

.web-content {
  display: block;
  height: 100%;
  overflow: auto;
}

.title {
  font-size: 24px;
  font-weight: 600;
  text-align: center;
  color: $text-color;
}

.button {
  background: $buttons-color;
  border-radius: 28px;
  color: #ffffff;
  font-size: 18px;
  padding: 10px 20px;
  margin: 5px 10px;
  border: 1px solid $buttons-color-dark;
}

.pageTitle {
  font-family: verdana;
  font-variant: small-caps;
  text-align: center;
  font-size: 43px;
  letter-spacing: 5px;
  word-spacing: 10px;
  color: $secondary-color-dark;
  text-shadow: rgb(0, 0, 0) 2px 2px 2px;
  margin: 2% auto;
}
</style>
