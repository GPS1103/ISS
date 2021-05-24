<template>
    <div class="web-content">
        <section>
          <div>eluwino po raz 3</div>
        </section>
    </div>
</template>

<script>

export default {
  name: 'WaterContainer3',
  mounted(){
    const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
    if(!appHeader.$data.user) this.$router.push({name: 'Login'});
  }
};
</script>
