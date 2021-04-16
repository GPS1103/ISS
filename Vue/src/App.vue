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
    // async function main(){
    //     await loadPyodide({
    //       indexURL : "https://cdn.jsdelivr.net/pyodide/v0.17.0a2/full/"
    //     });
    //     console.log(pyodide.runPython(`
    //         import sys
    //         sys.version
    //     `));
    //     console.log(pyodide.runPython("print(1 + 2)"));
    // }
    // main();
  },
  methods: {
    loadScript(){
      brython();
    },
    simulat(component, A, Beta, Qd, H, Tp, SimulationLength, hMax){
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
      
    },
    simulate(component, A, Beta, Qd, H, Tp, SimulationLength, hMax){
      let x = pyodide.runPython(`
      import math
      import time
      A = ${A}
      #runoff coefficient, in m^(5/2)/s
      Beta = ${Beta}
      #Flow in in m^3/s, our input variable
      Qd = ${Qd}
      #Liquid height during steps, h(0) is the starting condition, in m
      h = [${H}]
      #Sampling time/step time
      Tp = ${Tp}
      #in hours
      SimulationLength = ${SimulationLength}
      #constraints
      hMax = ${hMax}  

      def run():
          #print(A, Beta, Qd, H, Tp, SimulationLength, hMax)
          iterations = int((3600 * SimulationLength) / Tp)
     
          print(iterations)
          tic = time.time()
          for n in range(iterations + 1):
              #print("Value: ", n)  #yay, works, 36k iterations
              #skip step n = 0
              if (n == 0):
                  continue
              hNext = 1/A*(-1*Beta*math.sqrt(h[n-1])+Qd)*Tp+h[n-1]
              if hNext > hMax:
                  print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n*Tp, ' s.')
                  break
                  #raise ValueError('Try setting different parameters')
              h.append(hNext)
              #if(round(hNext,2) > round(h[n-1],2)):
              #    print(round(hNext,2))
              if(n == iterations):
                  toc = time.time()
                  print("Run script: ", toc - tic, ' s')
                  print('finisz') 
                  #print(h) 
                  return h
      #run(A, Beta, Qd, 5, Tp, SimulationLength, hMax)
      x = run();
      print('WaterContainer1.py loaded!')`);

      console.log((pyodide.globals.get('x')).toJs());
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
