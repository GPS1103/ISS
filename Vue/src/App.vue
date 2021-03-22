<template>
  <div id="app">
    <button
      type="button"
      class="btn"
      @click="showModal"
    >
      Open Modal!
    </button>
    <ModalForAdrian v-show="isModalVisible" @close="closeModal"/>
  </div>
</template>

<script>
import Vue from 'vue'
import VueConfetti from 'vue-confetti'
import ModalForAdrian from './components/ModalForAdrian.vue'

Vue.use(VueConfetti)

export default {
  name: 'App',
  components: {
    ModalForAdrian
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
  margin-top: 60px;
}

.btn {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
    padding: 10px
  }
</style>
