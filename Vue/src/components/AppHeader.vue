<template>
    <header class="element">
        <div @click="goBack()">
            <img class="logo" alt="logo" src="../assets/logo2.png">
        </div>
        <!--<h6 v-if="user">Witaj, {{user}}</h6>
        <h6 v-if="!user">Nie jesteś zalogowany!</h6>-->
        <button v-if="this.$route.name != 'Login' && !user" class="button" @click="login()">
            Zaloguj się
            <b-icon-power></b-icon-power>
        </button>
        <button v-if="this.$route.name != 'Login' && user" class="button" @click="logout()">Wyloguj się</button>
        <button class="infoIcon" @click="$emit('showModal')"><b-icon-info-circle></b-icon-info-circle></button>
        <button class="infoString" @click="$emit('showModal')">
            Pomoc
        </button>
    </header>
</template>

<script>
//import axios from 'axios'
export default {
    name: 'AppHeader',
    data(){
        return {
            user: null,
        }
    },
    mounted(){
        this.checkUser();
    },
    methods: {
        goBack(){
            
            if(this.$route.name != "WaterContainer1") {
                this.$parent.$children.find( child => { return child.$options.name == 'AppFooter'}).$data.active_tab = 0;
                this.$router.push({name: "WaterContainer1"})
            }
        },
        login(){
            this.$router.push({name: "Login"})
        },
        checkUser(){
            if(localStorage.getItem('tokenWaterControl')){
                this.user = 'user';
                const appFooter = this.$parent.$children.find(child => { return child.$options.name === "AppFooter"})
                appFooter.$data.items.forEach( (item, index) => { if(index != 0) item.disabled = false; });
            }
        },
        logout(){
            localStorage.removeItem('tokenWaterControl');
            this.user = null; 
            this.$router.push("WaterContainer1");
            const appFooter = this.$parent.$children.find(child => { return child.$options.name === "AppFooter"})
            appFooter.$data.items.forEach( (item, index) => { if(index != 0) item.disabled = true; });
            appFooter.$data.active_tab = 0;
            this.$emit('clicked', true);
        }
    }
}
</script>

<style lang="scss">
@import "@/scss/variables.scss";

    header {
        display: flex;
        flex-wrap: nowrap;
        margin: 0;
        top: 0;
        height: 60px;
        padding: 0 2%;
        /* width: 100%; */
    }
    .segment-value, .current-value {
        font-size: 10px !important;
    }

    .infoString,
    .infoIcon {
        letter-spacing: 2px;
        color: #babbc9 !important;
        margin: 10px;
        float: right;
    }

    .infoString {
        padding: 10px;

        @media (max-width: $break-mobile) {
            display: none;
        }
    }

    .infoIcon {
        padding: 7px;

        svg {
            height: 25px;
            width: 25px;
        }

        @media (min-width: $break-mobile) {
            display: none;
        }
    }

    .button {
        float: right;
        box-shadow: none !important;

        @media (max-width: $break-desktop) {
            padding: 10px !important;
        }
    }

    // .button.header {
    //     margin: auto 10px  !important;
    //     transform: scale(1.3) !important;
    //     line-height: initial;
    //     height: fit-content;
    // }

    .logo {
        float: left;
        height: 50px;
    }

    .logo:hover{
        cursor: pointer;
    }
</style>