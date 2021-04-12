<template>
    <div class="container">
        <div class="title">Ustawienia czynników:</div>
        <div v-for="item in items" v-bind:key="item.name">
            <Slider :value="item.value" :name="item.name" />
        </div>
        <v-btn id='simulation-btn' @click="simulate()">Symuluj</v-btn>

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
            this.$parent.$parent.simulate(this.$parent.$options.name, 10, 0.05, 0.005, 5, 0.01, 1, 20);
        }
    }
}
</script>

<style scoped>
    .container {
        width: 30%;
        height: 400px; /* TODO - RWD compatible */
        position: relative;
        background-color: var(--primary-color);
        float: right;
        margin: 5% 10%;
        border-radius: 3%;
        box-shadow: 5px 7px 20px -7px rgba(0,0,0,0.69);
    }

    .title {
        font-size: 20px;
        margin: 5% auto;
    }
    #simulation-btn {
        position: absolute;
        bottom: 0;
        left: 0;
        margin: 0px 0px 10px 0px;
        width: 100%;
    }
</style>