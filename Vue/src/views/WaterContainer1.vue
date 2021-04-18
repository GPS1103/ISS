<template>
    <div class="web-content">
        <section>
          <CustomeChart :y="y" :x="x"/>
          <VariablesSettingBox />
        </section>
    </div>
</template>

<script>
import VariablesSettingBox from '../components/VariablesSettingBox'
import CustomeChart from '../components/CustomeChart'

export default {
  name: 'WaterContainer1',
  components: {
    VariablesSettingBox,
    CustomeChart
  },
  data(){
    return {
      x: Number,
      y: Array
    }
  },
  watch: {
    x: function(){
      console.log('test');
    }
  },
};
</script>

<style>
  section {
    display: flex;
  }
</style>