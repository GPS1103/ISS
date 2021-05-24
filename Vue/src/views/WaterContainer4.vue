<template>
    <div class="web-content">
        <section>
          <div>eluwino po raz 4</div>
        </section>
    </div>
</template>

<script>

export default {
  name: 'WaterContainer4',
  mounted(){
    const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
    if(!appHeader.$data.user) this.$router.push({name: 'Login'});
  }
};
</script>
