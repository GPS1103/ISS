<template>
  <div class='sliderContainer'>
    <vue-slider v-bind="options" v-model="value" :min="min" :max="max" :data="data" :interval="interval"/>
    <div class='sliderName'>{{ name }}</div>
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
    }  
  },
  // watch: {
  //   value(range) {
  //     console.log(range, this.name);
  //     console.log(this.initialValue);
  //   }
  // }
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

</style>