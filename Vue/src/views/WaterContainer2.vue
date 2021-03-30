<template>
    <div class="web-content">
        <AppHeader /> 
        <section>
          <div>eluwino</div>
        </section>
        <AppFooter />
    </div>
</template>

<script>
import AppHeader from '../components/AppHeader'
import AppFooter from '../components/AppFooter'

export default {
  name: 'WaterContainer2',
  components: {
    AppHeader,
    AppFooter
  }
};
</script>
