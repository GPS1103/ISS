<template>
    <div class="web-content">
      <h1 class="pageTitle">NAPEŁNIANIE ZBIORNIKA</h1>
      <section>
        <VariablesSettingBox @simulate="simulate"/>
        <div class='singleChart'>
        <CustomeChart title="Wykres poziomu cieczy od czasu" type="spline" id="container-volume" :data="volume" axisX="Czas symulacji [h]" axisY="Wysokość poziomu wody [m]"/>
        </div>
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
      volume: Array,
      Tp: 1
    }
  },
  methods: {
    simulate(parametersArray){
      console.log(this.$options.name);
      console.log(parametersArray);
      this.$emit("simulateApp", this.$options.name, parametersArray);
    }
  }
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