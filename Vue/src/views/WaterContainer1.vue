<template>
    <div class="web-content">
        <section>
          <CustomeChart />
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
  }
};
</script>

<style>
  section {
    display: flex;
  }
</style>