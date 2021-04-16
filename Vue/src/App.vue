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
import LoadScript from 'vue-plugin-load-script'
import WaterContainer1Vue from './views/WaterContainer1.vue'
import CustomeChartVue from './components/CustomeChart.vue'

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
  data() {
    return{
      python: {
        WaterContainer1: {
          x: Array,   // array with data from python method
          y: Number   // number of iteration
        },
        WaterContainer2: {
          x: Array,
          y: Number
        },
        WaterContainer3: {
          x: Array,
          y: Number
        },
        WaterContainer4: {
          x: Array,
          y: Number
        }
      }
    }
  },
  created(){
    this.loadPythonScript();
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
        });

      })
      .catch(()=>{ alert('Błąd podczas ładowania pliku. Wczytaj stronę ponownie')});
    },
    simulate(component, A, Beta, Qd, H, Tp, SimulationLength, hMax){
      // run method from python script
      pyodide.runPythonAsync(`run${component}(${A}, ${Beta}, ${Qd}, ${H}, ${Tp}, ${SimulationLength}, ${hMax})`)
        .then((res)=>{ 
          this.python[`${component}`].x = res.toJs();
          this.python[`${component}`].y = parseInt((3600 * SimulationLength) / Tp);
        })
        .then(()=> {
          console.log(this.python[`${component}`].y, this.python[`${component}`].x)
          //reload chart
          CustomeChartVue.methods.updateData(1);
          //push data to DB
        });
    }
  }, 
}
</script>

<style>
:root {
  --primary-color: #88bdbc;
  --primary-color-dark: #254e58;
  --text-color: #112d32;
  --secondary-color-dark: #4f4a41;
  --secondary-color: #6e6658;
  --buttons-color: #4e85ba;
  --buttons-color-dark: #376087;
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

.button {
  background: var(--buttons-color);
  border-radius: 28px;
  color: #ffffff;
  font-size: 18px;
  padding: 10px 20px;
  margin: 5px 10px;
  border: 1px solid var(--buttons-color-dark);
}

</style>
