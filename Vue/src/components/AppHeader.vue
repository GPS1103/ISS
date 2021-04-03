<template>
    <header class="element">
        <div>{{ title }}</div>
        <div id="widgets">
            <VueSpeedometer 
                :forceRender="true"
                :maxSegmentLabels="1"
                :customSegmentStops="[0, 777, 1000]"
                :segmentColors='["#5959ac", "#AAA"]'
                needleColor="#b4b8b5"
                :currentValueText='"Current Value: \${value}"'
                :value="toggle ? 333 : 555"
                textColor="${textColor}"
                :width="200"
                :height="200"
            />
            <VueSpeedometer 
                :forceRender="true"
                :maxSegmentLabels="1"
                :customSegmentStops="[0, 777, 1000]"
                :segmentColors='["#5959ac", "#AAA"]'
                needleColor="#b4b8b5"
                :currentValueText='"Current Value: \${value}"'
                :value="toggle ? 333 : 555"
                textColor="${textColor}"
                :width="200"
                :height="200"
            />
        </div>
    </header>
</template>

<script>
import VueSpeedometer from "vue-speedometer"

export default {
    name: 'AppHeader',
    components: {
       VueSpeedometer
    },
    created(){
        setInterval( ()=>(this.toggle =! this.toggle), 1111);
    },
    data(){
        return {
            toggle: false,
        }
    },
    props: {
        title: {
            type: String,
        }
    }
}
</script>

<style>
    header {
        position: absolute;
        flex-shrink: 0;
        margin: 0;
        top: 0;
        height: 130px;
        width: 100%;
    }

    #widgets {
        display: flex;
        justify-content: space-around;
        width: 100%;
        height: 50px;
    }
    .segment-value, .current-value{
        font-size: 10px !important;
    }
</style>