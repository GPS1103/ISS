<template>
  <div id="chart-container"></div>
</template>

<script>
var CanvasJS = require('../plugins/canvasjs.min.js');
CanvasJS = CanvasJS.Chart ? CanvasJS : window.CanvasJS;

export default {
  name: 'ChartComponent',
  data() {
    return {
      chart: null,
      chartOptions: {
        title: {
          text: 'CanvasJS Chart in Vue.js'
        },
        animationEnabled: true,
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
    this.chart = new CanvasJS.Chart('chart-container', this.chartOptions);
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
