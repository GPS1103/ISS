<template>
    <div class="web-content">
      <h1 class="pageTitle">SYMULACJA MIESZANIA</h1>
      <section>
        <VariablesSettingBox @simulate="simulate"/>
        <div class='doubleCharts'>
        <CustomeChart title="Wykres objętości od czasu" type="spline" id="container-volume" :data="volume" axisX="Czas symulacji [h]" axisY="Wysokość poziomu cieczy [m]"/>
        <CustomeChart title="Wykres stężenia od czasu" type="spline" id="container-concentration" :data="concentration" axisX="Czas symulacji [h]" axisY="Stężenie substancji [%]"/>
        </div>
      </section>
    </div>
</template>


<script>
import VariablesSettingBox from '../components/VariablesSettingBox'
import CustomeChart from '../components/CustomeChart'

export default {
  name: 'WaterContainer2',
  components: {
    VariablesSettingBox,
    CustomeChart
  },
  data(){
    return {
      volume: Array,
      concentration: Array,
      Tp: 1
    }
  },
  mounted(){
    const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
    if(!appHeader.$data.user) this.$router.push({name: 'Login'});
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