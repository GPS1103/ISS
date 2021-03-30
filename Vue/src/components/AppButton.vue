<template>
    <b-button variant="primary" class='app-button'>{{ title }}</b-button>
</template>

<script>

//import 'vuetify/dist/vue'


export default {
    name: 'AppButton',
    // components: {
    //     Vuetify
    // },
    props: {
        title: {
            type: String
        }
    }
}
</script>

<style scoped>
    .app-button {
        /* width: 33.2%; */
        width: 100%;
        margin: 1px;
        height: 100% !important;
        /* background-color: #16384e; */
        color: white;
    }
</style>