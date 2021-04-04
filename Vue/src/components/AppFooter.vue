<template>
    <footer class="element">
        <div id='footer-container'>
            <v-tabs v-model="tab" fixed-tabs dark slider-size="4" show-arrows background-color="#6e6658" color="#FFF">
                <!-- <v-tabs-slider color="#a074c4"></v-tabs-slider> -->
                <v-tab v-for="item in items"
                    :key="item.tab"
                    
                    :disabled="item.disabled"
                    @click="goToPage(item.page)"> 
                    {{ item.tab }}</v-tab> 
            </v-tabs>  
        </div>
    </footer>
</template>
<script>

export default {
    name: 'AppFooter',
    data: ()=>({
        active_tab: 1,
        items: [
            { tab: 'Apka 1', disabled: false, page: 'WaterContainer1'},
            { tab: 'Apka 2', disabled: false, page: 'WaterContainer2' },
            { tab: 'Apka 3', disabled: false, page: 'WaterContainer3'},
            { tab: 'Apka 4', disabled: false, page: 'WaterContainer4'},
        ]
    }),
    methods: {
        goToPage(page){
            if(page !== this.$route.name) this.$router.push({name: page});
        }
    }
}
</script>

<style scoped>
    footer {
        position: absolute;
        flex-shrink: 0;
        margin: 0;
        bottom: 0;
        height: 50px;
        width: 100%;
        background-color: var(--secondary-color);
    }
    #footer-container {
        padding: 2px 0px 2px 0px;
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: space-between;
        flex-wrap: nowrap;
    }
</style>