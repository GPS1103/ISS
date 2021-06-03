<template>
    <div class="container">
        <div class="title">Ustawienia czynników:</div>
        <div v-for="item in items" :key="item.name">
            <Slider :name="item.name" :initialValue="item.initialValue" :min="item.min" :max="item.max" :data="item.data" :interval="item.interval"/>
        </div>
        <button class="button" @click="simulate()">
            Symuluj
            <b-icon-gear></b-icon-gear>
        </button>
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
            default: function() { return SETTINGS_FIELDS }
        }
    },
    data(){
        return {
            Tp: 1
        }
    },
    methods: {
        simulate(){
            const child = this.$children;
            if(child[3].$data.value > child[4].$data.value){
                alert("Aktualna wysokość poziomu wody nie może być wyższa od maksymalnej wysokości zbiornika");
            }
            else {
                this.Tp = child[5].$data.value;
                this.$parent.$parent.simulate(this.$parent.$options.name,
                    child[0].$data.value, 
                    child[1].$data.value, 
                    child[2].$data.value, 
                    child[3].$data.value, 
                    child[4].$data.value, 
                    child[5].$data.value, 
                    child[6].$data.value);
            }
        }
    },
}
</script>

<style scoped lang="scss">
@import "@/scss/variables.scss";

    .container {
        width: 70%;
        margin: 3% auto;
        position: relative;
        background-color: $primary-color;
        border-radius: 3%;
        box-shadow: 5px 7px 20px -7px rgba(0,0,0,0.69);
        padding-bottom: 70px;

        @media (min-width: $break-desktop) {
            width: 40%;
            margin: 3% 5%;
            position: absolute;
            left: 0;
            padding-bottom: 10px;
        }

        @media (min-width: $break-big-desktop) {
            width: 35%;
            margin: 3% 10%;
        }
    }
    .title {
        font-size: 20px;
        margin: 5% auto;
    }

    .button {
        // background-color: whitesmoke;
        // border-color: rgb(171,171,171);
        // color: black;
        margin-left: 25%;
        width: 50%;
    }
</style>