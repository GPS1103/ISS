<template>
    <div class="web-content">
        <section>
          <CustomeChart title="Superancki wykresik" type="spline" :data="volume"/>
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
      volume: Array
    }
  },
};
</script>

<style>
  section {
    display: flex;
  }
</style>