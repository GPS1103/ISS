<template>
  <div class="small">
    <div>
    <button class="button" @click="fillData(1)">Wysokość</button>
    <button class="button" @click="fillData(2)">Objętość</button>
    </div>
    <line-chart :chart-data="datacollection"></line-chart>
  </div>
</template>

<script>
  import LineChart from './LineChart'
  import { CHARTS_SETTINGS } from '../consts.js'
  import get from 'lodash/get';

  export default {
    name: "CustomeChart",
    components: {
      LineChart
    },
    data () {
      return {
        datacollection: null,
        choosenGraphId: 1,
      }
    },
    methods: {
      fillData (id) {
        this.choosenGraphId = id;
        this.datacollection = get(CHARTS_SETTINGS, this.choosenGraphId);
      }
    },
    mounted () {
      this.fillData(this.choosenGraphId);
    }
  }
</script>

<style>
  .small {
    max-width: 600px;
    margin: auto;
  }
</style>