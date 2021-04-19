<template>
    <div class="web-content">
      <h1 class="pageTitle">FIRST APPLICATION</h1>
      <section>
        <CustomeChart title="Superancki wykresik" type="spline" :data="volume" />
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

<style scoped  lang="scss">
@import "@/scss/variables.scss";

  section {
    display: block;
    margin-bottom: 70px;

    @media (min-width: $break-desktop) {
      display: flex;
    }
  }
</style>