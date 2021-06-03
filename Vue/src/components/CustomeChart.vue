<template>
  <div class="small">
    <div>
      <!-- <button class="button" @click="changeUi()">Wysokość</button>
      <button class="button" @click="fillData(2)">Objętość</button> -->
    </div>
    <div id="chart-container"></div>
  </div>
</template>

<script>
 
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
    },
    axisX: String, 
    axisY: String 
  },
  data() {
    return {
      chart: null,
      chartOptions: {
        title: {
          text: this.title
        },
        axisX: {
          title: this.axisX,
        },
        axisY: {
          title: this.axisY
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
    data: async function(){
      console.log('changed');
      const result = this.$parent.$children.find(child => { return child.$options.name === "VariablesSettingBox" });
      console.log(result.$data.Tp);
      this.chart.options.data[0].dataPoints = this.calcDataPoints(result.$data.Tp);
      await this.chart.render();
      this.$root.$children[0].$data.freezeButtons = false;
      console.log('rendered');
    },
  },
  methods: {
    calcDataPoints(Tp){
      return Array.from(this.data)
      .reduce((res, value, index)=>{
          res.push({
          x: index*Tp/3600,
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
      max-width: 500px;
      margin: 5% auto;
      right: 40%;

    @media (max-width: $break-mobile) {
      max-width: 350px;
      right: 400px;
    }

    @media (min-width: $break-desktop) {
      max-width: 500px;
      position: absolute;
      margin: 5% 5%;
    }

    @media (min-width: $break-big-desktop) {
      max-width: 700px;
      position: absolute;
      margin: 5% 15%;
      right: 30%;
    }
  }
  
  #chart-container {
    width: 100%;
    height: 400px;
    margin: none
  }
</style>