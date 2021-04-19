<template>
    <div class="container">
        <div class="title">Ustawienia czynników:</div>
        <div v-for="item in items" v-bind:key="item.name">
            <Slider :value="item.value" :name="item.name" />
        </div>
        <button class="button" @click="simulate()">Symuluj</button>
    </div>
</template>

<script>
import Slider from './Slider'
import { SETTINGS_FIELDS } from '../consts.js'

export default {
    name: 'VariablesSettingBox',
    components: {
        Slider,
    },
    props: {
        items: {
            type: Array,
            default: SETTINGS_FIELDS
        }
    },
    methods: {
        simulate(){
            this.$parent.$parent.simulate(this.$parent.$options.name, 10, 0.005, 0.05, 5, 0.01, 1, 20);
        }
    }
}
</script>

<style scoped lang="scss">
@import "@/scss/variables.scss";

    .container {
        width: 80%;
        margin: 5% auto;
        position: relative;
        background-color: $primary-color;
        border-radius: 3%;
        box-shadow: 5px 7px 20px -7px rgba(0,0,0,0.69);

        @media (min-width: $break-desktop) {
            width: 40%;
            float: right;
            margin: 5% 10%;
        }
    }
    .title {
        font-size: 20px;
        margin: 5% auto;
    }
    .button {
        background-color: whitesmoke;
        border-color: rgb(171,171,171);
        color: black;
        width: 50%;
    }
</style>