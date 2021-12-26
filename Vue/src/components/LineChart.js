// import { Line, mixins } from 'vue-chartjs'
// const { reactiveProp } = mixins

// export default {
//   extends: Line,
//   mixins: [reactiveProp],
//   props: ['options'],
//   mounted () {
//     // this.chartData is created in the mixin.
//     // If you want to pass options please create a local options object
//     this.renderChart(this.chartData, this.options)
//   }
//}

import {Line, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins;

export default {
    extends: Line,
    mixins: [reactiveProp],
    props: ['data', 'label', 'options'],// recieving props
    mounted() {
        this.renderLineChart();
    },
    computed: {
        chartData: function() {
            return this.data;
        },
        labelData: function(){
            return this.label;
        }
    },
    methods: {
      renderLineChart: function() {
         this.renderChart({
            labels: this.labelData,
            datasets: [{
               label: 'Data One',
               backgroundColor: '#505464',
               hoverBackgroundColor: '#2196f3',
               data: this.chartData
                        }
                    ]
            },
            { elements: {
                point:{
                    radius: 0
                }
                },
                animation: false,
                responsive: false,
                maintainAspectRatio: false,
                spanGaps: true,
                tooltips: {
                    enabled: false
                },
                //hover: {mode: null}
                events: []
            }
            );
        }
    },
    watch: {
        data: function() {
          console.log('restart graph');
            //this._chart.destroy();
            this.renderLineChart();
           
        }
    }
}
