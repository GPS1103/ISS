<template>
    <div class="web-content">
      <h1 class="pageTitle">SYMULACJA NAPEŁNIANIA</h1>
      <section>
        <VariablesSettingBox @simulate="simulate"/>
        <div class='singleChart'>
        <CustomeChart title="Wykres poziomu cieczy od czasu" type="spline" id="container-volume" :data="volume" axisX="Czas symulacji [h]" axisY="Wysokość poziomu cieczy [m]"/>
        </div>
      </section>
    </div>
</template>


<script>
import VariablesSettingBox from '../components/VariablesSettingBox'
import CustomeChart from '../components/CustomeChart'

export default {
  name: 'WaterContainer5',
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
        if(parametersArray[3] <= parametersArray[4] && parametersArray[5] <= parametersArray[4]){
            console.log(this.$options.name);
            console.log(parametersArray);
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