<template>
  <div class="small">
    <div>
    </div>
    <div class="chart-container" :id="this.id"></div>
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
    id: String,
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
        toolTip:{
          contentFormatter: function(e){
            return "<b style='color: blue'>"+parseFloat(e.entries[0].dataPoint.x).toFixed(3)+"</b>"+": "+parseFloat(e.entries[0].dataPoint.y).toFixed(3);
          }
        },
        animationEnabled: true,
        data: [
          {
            type: this.type,
            dataPoints: this.calcDataPoints(),
            name: this.name,
          }					
        ]
      }
    }
  },
  watch: {
    data: async function(){
      console.log('changed');
      const Tp = this.$parent.$data.Tp;//this.$parent.$children.find(child => { return child.$options.name === "VariablesSettingBox" });
      console.log(Tp);
      this.chart.options.data[0].dataPoints = this.calcDataPoints(Tp);
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
    this.chart = new CanvasJS.Chart(this.id, this.chartOptions);
    this.chart.render();
  }
}
</script>

<style scoped lang="scss">
@import "@/scss/variables.scss";

  .small {
      max-width: 500px;
      margin: 5% auto;

      .singleChart & {
        right: 40%;
      }

    @media (max-width: $break-mobile) {
      max-width: 350px;
      // right: 400px;

      .singleChart &{
        right: 400px;
      }
    }

    @media (min-width: $break-desktop) {
      max-width: 500px;
      margin: 5% 5%;

      .singleChart & {
        position: absolute;
      }
    }

    @media (min-width: $break-big-desktop) {
      max-width: 700px;
      // position: absolute;
      margin: 5% 15%;
      // right: 30%;

      .singleChart & {
        right: 30%;
      }
    }
  }
  
  .chart-container {
    width: 100%;
    height: 400px;
    margin: none;
  }
</style>