<template @click="click">
  <div id="app">
    <AppHeader @clicked="showLogoutMessage" @showModal="showModal" />
    <div class="alert alert-primary" role="alert" :style="{opacity: isSuccessAlertShow ? 1 : 0}">
        Zostałeś wylogowany.
    </div>
    <Modal v-if="isModalShow" @close="closeModal" />
    <router-view @simulateApp="simulate"/>
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
import Modal from './components/Modal.vue'
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
    AppFooter,
    Modal
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
      user: null,
      isSuccessAlertShow: false,
      isModalShow: false,
    }
  },
  methods: {
    showModal(){
      this.isModalShow = true;
    },
    closeModal(){
      this.isModalShow = false;
    },
    showLogoutMessage(){
      this.isSuccessAlertShow = true;
      setTimeout(() => {
          this.isSuccessAlertShow = false;
      }, 2000);
    },
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
            .then((text) => pyodide.runPython(text));
        
          fetch('/python/WaterContainer2.py')
                .then(res => res.text())
                .then((text) => pyodide.runPython(text));
          fetch('/python/WaterContainer4.py')
                .then(res => res.text())
                .then((text) => pyodide.runPython(text));

          fetch('/python/WaterContainer5.py')
            .then(res => res.text())
            .then((text) => pyodide.runPython(text));

          fetch('/python/PIDController.py')
            .then(res => res.text())
            .then((text) => pyodide.runPython(text))
            .then(()=>{
              pyodide.loadPackage("pandas")
            .then((res) => {
              fetch('/python/WaterContainer3.py')
                .then(res => res.text())
                .then((text) => pyodide.runPython(text))
                .then(() => { this.freezeButtons = false });
              })
            });
        });
      })
      .catch(()=>{ alert('Błąd podczas ładowania pliku. Wczytaj stronę ponownie')});
    },
    simulate(component, params){
      // run method from python script
      this.freezeButtons = true;
      let invoke = `run${component}(`;
      params.forEach((cur) => {
        invoke += `${cur},`;
      })
      invoke = invoke.slice(0, -1) + ')';
      console.log(invoke);

      pyodide.runPythonAsync(invoke)
        .then((res)=>{ 
          const result = this.$children.find(child => { return child.$options.name === component });
          const calcVal = res.toJs();
          if(component === "WaterContainer1"){ 
            result.$data.volume = calcVal;
          }
          else if(component === "WaterContainer2"){ 
            result.$data.volume = calcVal[0];
            result.$data.concentration = calcVal[1];
          }
          else if(component === "WaterContainer3"){ 
            result.$data.volume = calcVal;
          }
          else if(component === "WaterContainer3_1"){ 
            result.$data.volume = calcVal;
          }
          else if(component === "WaterContainer4"){ 
            result.$data.volume = calcVal[0];
            result.$data.concentration = calcVal[1];
          }
          else if(component === "WaterContainer5"){ 
            result.$data.volume = calcVal;
          }
          //console.log(calcVal);
          this.freezeButtons = false;
        })

      // } 
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
  overflow: hidden;

  @media (max-width: $break-desktop) {
    overflow: auto;
  }
}

.element {
  background-color: $secondary-color;
}

.web-content {
  display: block;
  height: 100%;
  overflow: auto;

  @media (max-width: $break-desktop) {
    padding-bottom: 100px;
  }
}

.title {
  font-size: 24px;
  font-weight: 600;
  text-align: center;
  color: $text-color;
}

.button {
  border-radius: 28px;
  font-size: 18px;
  padding: 10px 20px;
  margin: 5px 10px;
  border: 1px solid $buttons-color-dark;

  background: lighten($buttons-color, 3%);
  border: 1px solid darken($buttons-color, 4%);
  box-shadow: 0px 1px 0 darken(#a4b1b9, 1%), 1px 2px 2px darken(#a4b1b9, 2%);
  font-weight: 500;
  letter-spacing: 2px;
  transition: all 150ms linear;

&:hover {
  background: darken($buttons-color, 20%);
  border: 1px solid rgba(#000, .05);
  box-shadow: 1px 1px 2px rgba(grey, .2);
  color: lighten($buttons-color, 18%);
  text-decoration: none;
  text-shadow: -1px -1px 0 darken($buttons-color, 9.5%);
  transition: all 250ms linear;
}
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

  @media (max-width: $break-mobile) {
    font-size: 30px;
    margin: 8% 3%;
  }
}

.alert {
    opacity: 0;
    position: absolute;
    width: 50%;
    top: 100px;
    right: 25%;
    transition: all .5s;
    &.alert-primary {
        background-color: #007BFF;
        color: #fff;
        font-size: 18px;
        border: none;
    }
    .widget {
        position: absolute;
        right: 5px;
        top: 0;
        margin: 10px;
    }
}
</style>
