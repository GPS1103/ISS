<template>
  <div class="small">
    <div>
      <button class="button" @click="changeUi()">Wysokość</button>
      <button class="button" @click="fillData(2)">Objętość</button>
    </div>
    <!-- <line-chart :data="dataChart" :label="labelChart" :options="{elements: {point:{radius: 0}},animation: false, responsive: false, maintainAspectRatio: false}"></line-chart> -->
    <!-- <ChartComponent /> -->
    <div id="chart-container"></div>
  </div>
</template>

<script>
  // // import LineChart from './LineChart'
  // import ChartComponent from './ChartComponent.vue';

  // export default {

  //   name: "CustomeChart",
  //   props: {
  //     x: Number,
  //     y: Array
  //   },
  //   components: {
  //     // LineChart,

  //     ChartComponent
  //   },

  //   data () {
  //     return {
  //       dataChart: null,
  //       labelChart: null,
  //       optionsChart: null
  //       //choosenGraphId: 1,
  //     }
  //   },


  //   watch: {
  //     y: function(){
  //       console.log('zmianka');
  //       this.dataChart = this.y;
  //       this.labelChart = Array.from(Array(this.x).keys());
  //     },
  //   },
  // }
  var CanvasJS = require('../plugins/canvasjs.min.js');
CanvasJS = CanvasJS.Chart ? CanvasJS : window.CanvasJS;

export default {
  name: 'ChartComponent',
   props: {
    data: {
      Array,
      default: []
      
    },
    title: String,
    type: {
      String,
      default: 'spline'
    }
  },
  data() {
    return {
      chart: null,
      chartOptions: {
        title: {
          text: this.title
        },
        animationEnabled: true,
        data: [
          {
            type: this.type,
            dataPoints: this.calcDataPoints()
          }					
        ]
      }
    }
  },
  watch: {
    data: function(){
      this.chart.options.data[0].dataPoints = this.calcDataPoints();
      this.chart.render();
    },
  },
  methods: {
    calcDataPoints(){
      return Array.from(this.data)
      .reduce((res, value, index)=>{
          res.push({
          x: index,
          y: value
        });    
        return res;
      },[])
    }
  },
  mounted: function () { 
    this.chart = new CanvasJS.Chart('chart-container', this.chartOptions);
    this.chart.render();
  }
}
</script>

<style scoped lang="scss">
@import "@/scss/variables.scss";

  .small {
      width: fit-content;
      margin: 5% auto;

    @media (min-width: $break-desktop) {
      max-width: 600px;
    }
  }
  #chart-container {
  width: 100%;
  height: 400px;
  margin: none
}
</style>