<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <slot name="header">
          Ola Amigo Adrian!
        </slot>
        <button
          type="button"
          class="btn-close"
          @click="close"
        >
          x
        </button>
      </header>
      <section class="modal-body">
        <slot name="body">
          <img alt="Adrian z dyplomem" src="../assets/adi.png">
        </slot>
      </section>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import VueConfetti from 'vue-confetti'

Vue.use(VueConfetti)

  export default {
    name: 'ModalForAdrian',
    methods: {
      close() {
        this.$emit('close');
        this.$confetti.stop();
      }
    },
  };
</script>

<style scoped>
  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header {
    padding: 15px;
    display: flex;
    font-size: 24px;
    align-items: center;
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #037a64;
    justify-content: space-between;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  .btn-close {
    position: absolute;
    top: 0;
    right: 0;
    border: none;
    font-size: 20px;
    padding: 10px;
    cursor: pointer;
    font-weight: bold;
    color: #c6fff5;
    background: transparent;
  }

</style>