<template>
    <div class="web-content">
      <h1 class="pageTitle">NAPEŁNIANIE ZBIORNIKA</h1>
      <section>
        <VariablesSettingBox @simulate="simulate"/>
        <div class='singleChart'>
        <CustomeChart title="" type="spline" id="container-volume" :data="volume" axisX="Czas symulacji [h]" axisY="Wysokość poziomu cieczy [m]"/>
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
      if(parametersArray[3] <= parametersArray[4]){
        this.$emit("simulateApp", this.$options.name, parametersArray);
      }
      else {
        alert("Aktualna lub zadana wysokość zbiornika nie może być większa od maksymalnej wysokości zbiornika");
      }
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