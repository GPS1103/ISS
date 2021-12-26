
import { ColumnChart } from 'canvasjs'
//const { reactiveProp } = mixins;
//CanvasJS = CanvasJS.Chart ? CanvasJS : window.CanvasJS;

export default {
extends: ColumnChart,
//mixins: [reactiveProp],
name: 'CanvasLineChart',
data: {
    chartOptions: {
        title: {
        text: "CanvasJS Chart in Vue.js"
      },
      data: [
        {
          type: "column",
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
    },
    chart : null
  },
  mounted: function () {
		this.chart = new CanvasJS.Chart("chartContainer", this.chartOptions);
    this.chart.render();
  }
}