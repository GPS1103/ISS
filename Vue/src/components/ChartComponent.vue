<template>
  <div :id="this.id"></div>
</template>

<script>
var CanvasJS = require('../plugins/canvasjs.min.js');
CanvasJS = CanvasJS.Chart ? CanvasJS : window.CanvasJS;

export default {
  name: 'ChartComponent',
  props: {
    id: String
  },
  data() {
    return {
      chart: null,
      chartOptions: {
        title: {
          text: 'CanvasJS Chart in Vue.js'
        },
        animationEnabled: false,
       toolTipContent:"<a href = {name}> {label}</a><hr/>Views: {y}",
       toolTip:{
          contentFormatter: function(e){
            return "<b>"+parseFloat(e.entries[0].dataPoint.x).toFixed(2)+"</b>";
          }
        },
        data: [
          {
            type: 'line',
            dataPoints: [
              { x: 10, y: 71 },
              { x: 20, y: 55 },
              { x: 30, y: 50 },
              { x: 40, y: 65 },
              { x: 50, y: 95 },
              { x: 60, y: 68 },
              { x: 70, y: 28 },
              { x: 80, y: 34 },
              { x: 90, y: 14 }
            ]
          }					
        ]
      }
    }
  },
  mounted: function () { 
    this.chart = new CanvasJS.Chart(this.id, this.chartOptions);
    this.chart.render();
  }
}

</script>
<style scoped>
#chart-container {
  width: 100%;
  height: 400px;
  margin: none
}
</style>
