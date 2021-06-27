<template>
  <div class='sliderContainer'>
    <vue-slider v-bind="options" v-model="value" :min="min" :max="max" :data="data" :interval="interval" />
    <div class='sliderName'>{{ name }}</div>
    <div class="sliderComponents" >
      <div class='sliderValue'>{{ value }}</div>
      <div class='sliderUnit'>
        <p v-html="units"></p>
      </div>
    </div>
  </div>
</template>
 
<script>
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/antd.css'
 
export default {
  name: 'Slider',
  components: {
    VueSlider
  },
  data () {
    return {
      options: {
        width: '60%',
      },
      value: this.initialValue
    }
  },
  props: {
    name:{
      type: String,
      default: ''
    },
    min: { 
      type: Number,
      default: 3
    },
    max: { 
      type: Number,
      default: 3
    },
    data: {
      type: Array
    },
    interval: {
      type: Number
    },
    initialValue: {
      type: Number
    },
    units: {
      type: String
    }  
  },
}
</script>

<style lang="scss">
@import "@/scss/variables.scss";

    .sliderContainer {
      display: flex;
      margin: 2% 5%;
    }

    .vue-slider-process {
      background-color: $secondary-color;
    }

    .vue-slider {
      width: 40% !important;
    }

    .sliderName {
      margin-left: 5%;
      width: 50% !important;
      display: flex;
    }
    
    .sliderComponents{
      display: flex;
      flex-wrap: nowrap;
      min-width: 80px;
      justify-content: center;
      right: 0;
      margin-left: 0px;
    }

    .sliderUnit {
      margin-left: 4px;
      min-width: 40px;
      text-align: center;
    }

    .sliderValue {
      font-weight: bold;
      text-align: center;
      min-width: 40px;
      
    }

</style>