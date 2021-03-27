<template>
    <footer class="element">
        <div id='footer-container'>
            <v-card>
                <v-tabs centered background-color="red">
                    <b>
                    <v-tab v-for="item in items"
                        
                        :key="item.tab"
                        :disabled="item.disabled"
                        @click="openApp(item.href)"> 
                        {{ item.tab }}</v-tab>
                    </b>
                </v-tabs>  
            </v-card>
            <b-tooltip v-for="(item, index) in items" :key="index" :disabled="!item.disabled" :target="item.tab">{{ item.tab }}</b-tooltip>
            <!-- <AppButton title='Apka 1'/>
            <AppButton title='Apka 2'/>
            <AppButton title='Apka 3'/> --> 
        </div>
    </footer>
</template>

<script>
// import AppButton from './appButton'

export default {
    name: 'AppFooter',
    components: {
        // AppButton    
    },
    props: {
        title: {
            type: String,
            default: 'eluwino'
        }
    },
    data(){
        return {
            items: [
                { tab: 'Apka 1', disabled: false, href: 'localhost:8080/apka_1'},
                { tab: 'Apka 2', disabled: false, href: 'localhost:8080/apka_2' },
                { tab: 'Apka 3', disabled: true, href: 'localhost:8080/apka_3'}
            ]
        }
    },
    methods: {
        openApp(link){
            console.log(link);
            // tutaj AJAX
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