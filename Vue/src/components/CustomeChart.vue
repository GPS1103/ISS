<template>
  <div class="small">
    <div>
    <button class="button" @click="changeUi()">Wysokość</button>
    <button class="button" @click="fillData(2)">Objętość</button>
    </div>
    <line-chart :data="dataChart" :label="labelChart" :options="{elements: {point:{radius: 0}},animation: false, responsive: false, maintainAspectRatio: false}"></line-chart>
  </div>
</template>

<script>
  import LineChart from './LineChart'
  export default {

    name: "CustomeChart",
    props: {
      x: Number,
      y: Array
    },
    components: {
      LineChart
    },

    data () {
      return {
        dataChart: null,
        labelChart: null,
        optionsChart: null
        //choosenGraphId: 1,
      }
    },

    watch: {
      y: function(){
        console.log('zmianka');
        this.dataChart = this.y;
        this.labelChart = Array.from(Array(this.x).keys());
      },
    },
  }
</script>

<style>
  .small {
    max-width: 600px;
    margin: auto;
  }
</style>