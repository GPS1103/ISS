<template>
  <div class='sliderContainer'>
    <vue-slider v-bind="options" v-model="value" />
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
        max: 100,
        width: '60%',
      }
    }
  },
    props: {
        value: {
            type: Number,
            default: 0
        },
        name: {
            type: String,
        }
    },
  watch: {
    value(range) {
      console.log(range, this.name);
    }
  }
}
</script>

<style>
    .sliderContainer {
      display: flex;
      margin: 2% 5%;
    }

    .vue-slider-process {
      background-color: var(--secondary-color);
    }

    .sliderName {
      margin-left: 5%;
    }

</style>