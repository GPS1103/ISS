<template>
    <footer class="element">
        <div id='footer-container'>
            <b-tooltip v-if="!this.$parent.$children.find( child => { return child.$options.name == 'AppHeader'}).$data.user" target="xx" triggers="hover">
                Zaloguj się aby odblokować pozostałe aplikacje
            </b-tooltip>
            <v-tabs id='xx' v-model="active_tab" fixed-tabs dark background-color="#6e6658" color="#FFF">
                <!-- <v-tabs-slider color="#a074c4"></v-tabs-slider> -->
                <v-tab v-for="item in items"
                    :key="item.tab"
                    :disabled="item.disabled"
                    @click="goToPage(item.page)" > 
                    {{ item.tab }}
                </v-tab> 
            </v-tabs> 
        </div>
    </footer>
</template>
<script>

export default {
    name: 'AppFooter',
  
    mounted(){
        this.active_tab = this.$route.meta.number;
    },
    data: ()=>({
        active_tab: 0,
        items: [
            { tab: 'Apka 1', disabled: false, page: 'WaterContainer1'},
            { tab: 'Apka 2', disabled: true, page: 'WaterContainer2' },
            { tab: 'Apka 3', disabled: true, page: 'WaterContainer3'},
            { tab: 'Apka 3_1', disabled: true, page: 'WaterContainer3_1'},
            { tab: 'Apka 4', disabled: true, page: 'WaterContainer4'},
            { tab: 'Apka 5', disabled: true, page: 'WaterContainer5'}
        ]
    }),
    methods: {
        goToPage(page){
            if(page !== this.$route.name){ 
                const pages = this.items.reduce((res, value) => {
                    res.push(value.page);
                    return res;
                }, [])
                console.log(![1,2,3].includes(pages.indexOf(page)));
                console.log(this.$root.$children[0].$data.logged);

                if(pages.indexOf(page) == 0 || this.$parent.$children.find( child => { return child.$options.name == 'AppHeader'}).$data.user){
                    this.$router.push({name: page})
                }
                else {
                    this.$router.push({name: "WaterContainer1"});
                    this.active_tab = 0;
                    alert('Aby skorzystać z tej aplikacji musisz być zalogowany');
                    
                }
            }
        }
    }
}
</script>

<style scoped lang="scss">
@import "@/scss/variables.scss";

footer {
    position: absolute;
    flex-shrink: 0;
    margin: 0;
    bottom: 0;
    height: 50px;
    width: 100%;
    background-color: $secondary-color;
    z-index: 5;
}
#footer-container {
    padding: 2px 0px 2px 0px;
    width: 100%;
    height: 100%;
    display: inline-block;
    flex-wrap: nowrap;

    @media (min-width: $break-desktop) {
      width: 80%;
    }
}
</style>