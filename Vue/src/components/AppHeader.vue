<template>
    <header class="element">
        <h6 v-if="user">Witaj, {{user}}</h6>
        <h6 v-if="!user">Nie jesteś zalogowany!</h6>
        <button v-if="this.$route.name != 'Login' && !user" class="button" @click="login()">Zaloguj się</button>
        <button v-if="this.$route.name != 'Login' && user" class="button" @click="logout()">Wyloguj się</button>
    </header>
</template>

<script>
import axios from 'axios'
export default {
    name: 'AppHeader',
    data(){
        return {
            user: null
        }
    },
    created(){
        this.checkUser();
        console.log(this.$route.name);
    },
    methods: {
        login(){
            console.log('losgin');
            this.$router.push({name: "Login"})
        },
        checkUser(){
            axios.get('user')
                .then( res =>{ 
                    console.log(res);
                    this.user = res.user;
                })
                .catch( err => {
                    console.log(err);
                    //for test
                    // this.user = 'test';
                    // const appFooter = this.$parent.$children.find(child => { return child.$options.name === "AppFooter"})
                    // appFooter.$data.items.forEach( item => item.disabled = false);
                    
                })
        },
        logout(){
            localStorage.removeItem('token');
            this.user = null; 
            this.$router.push("WaterContainer1");
            const appFooter = this.$parent.$children.find(child => { return child.$options.name === "AppFooter"})
            appFooter.$data.items.forEach( (item, index) => { if(index != 0) item.disabled = true; });
            appFooter.$data.active_tab = 0;
        }
    }
}
</script>

<style>
    header {
        display: flex;
        flex-wrap: nowrap;
        margin: 0;
        top: 0;
        height: 60px;
        /* width: 100%; */
    }
    .segment-value, .current-value{
        font-size: 10px !important;
    }

    .button.header{
        margin: auto 10px  !important;
        transform: scale(1.3) !important;
        line-height: initial;
        height: fit-content;
    }
</style>