<template>
    <section class="container-fluid">
        <div class="container">
                <div class="login-panel">
                    <div class="alert alert-primary" role="alert" :style="{display: isSuccessAlertShow ? 'block' : 'none'}">
                        Jesteś zalogowany!<br><small>Oczekiwanie na przekierowanie</small>
                    </div>
                    <div class="alert alert-error" role="alert" :style="{display: isFailAlertShow ? 'block' : 'none'}">
                        Niewłaściwy adres email, bądź hasło
                    </div>
                    <h1 class="display-4 font-weight-bold">Logowanie</h1>
                    <br>
                    <form action="">
                        <div class="form-group">
                            <label class="input-label">Email</label>
                            <input type="email" @click="clickInput()" class="form-control" placeholder="Email" v-model="email">
                            <span class="email-validate" v-if="required_email">{{ email_error}}</span>
                        </div>
                        <div class="form-group">
                            <label class="input-label">Hasło</label>
                            <input type="password" @click="clickInput()" class="form-control" placeholder="Hasło" v-model="password">
                            <span class="email-validate" v-if="required_password">To pole jest wymagane</span>
                        </div>
                        <br>
                        <div class="form-group d-flex justify-content-center">
                            <button class="button" id="login" @click.prevent="logUser">Zaloguj</button>
                            <button class="button" id="register" @click="redirect('Registration')">Zarejestruj</button>
                        </div>
                    </form>
                </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios'

//import { setTimeout } from 'timers';
export default {
    data() {
        return {
            email: null,
            password: null,
            isLoggingIn: false,
            isSuccessAlertShow: false,
            isFailAlertShow: false,
            required_password: false,
            required_email: false,
            email_error: "To pole jest wymagane"
        }
    },
    mounted(){
        const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
        if(appHeader.$data.user) this.$router.push({name: 'WaterContainer1'});
    },
    methods: {
        logUser() {
            const emailRequired = this.isRequired("email");
            const passwordRequired = this.isRequired("password");
            // if(this.login == "test" && this.password == "test"){
            //     const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
            //     appHeader.$data.user = "test"
            //     this.isSuccessAlertShow = true;      
            //     setTimeout(() => {
            //         const appFooter = this.$parent.$children.find(child => { return child.$options.name === "AppFooter"})
            //         appFooter.$data.items.forEach( item => item.disabled = false);
            //         this.redirect('WaterContainer1')
            //     }, 2000);
            // }
            if(!emailRequired && !passwordRequired){
                this.required_email = false;
                this.required_password = false;

                if(!this.validateEmail(this.email)){
                    this.email_error = "Wprowadz poprawny adres email";
                    this.required_email = true;
                    return;
                }
                axios.post('https://iss-server-app.herokuapp.com/api/login',{
                    email: this.email,
                    password: this.password
                }). then(
                    res => {
                        this.isSuccessAlertShow = true;
                        //console.log(res.data.token);
                        document.getElementsByClassName('alert-primary')[1].style.opacity="1"
                        localStorage.setItem('tokenWaterControl', res.data.token);
                        const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
                        appHeader.$data.user = res.data.data.name;
                        console.log(appHeader.$data, appHeader.$data.user );
                        const appFooter = this.$parent.$children.find(child => { return child.$options.name === "AppFooter"})
                        appFooter.$data.items.forEach( item => item.disabled = false);
                        setTimeout(() => {
                            this.$parent.$children.find( child => { return child.$options.name == 'AppFooter'}).$data.active_tab = 0;
                            this.redirect('WaterContainer1')
                        }, 2000);
                    }
                ).catch( (err) => {
                    this.isFailAlertShow = true;
                    document.getElementsByClassName('alert-error')[0].style.opacity="1"
                    console.log(err.response)}
                );
            }
        },
        redirect(pageName) {
            this.$router.push({name: pageName})
        },
        isRequired(name) {
            if(eval("this."+name) == null || eval("this."+name) == ""){
                eval("this.required_" + name + "= true");
                return true;
            }
            return false;
        },
        clickInput(){
            this.error_message = "To pole jest wymagane";
            this.isFailAlertShow = false;
            this.required_email = false;
            this.required_password = false;
        },
        validateEmail(email) {
            const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        },
    }
}
</script>

<style lang="scss" scoped>
@import "@/scss/variables.scss";
section {
  margin-top: 0;
}
.form-group {
  text-align: left;
}
.container{
  justify-content: center;

    @media (min-width: $break-desktop) {
        width: 40%;
    }
}
.widget {
    margin: 0;
    height: unset;
}
.email-validate {
    color: red;
}
.login-panel {
    position: relative;
    padding: 100px 0;

    .alert {
        position: absolute;
        width: 100%;
        top: 10px;
        right: 0;
        opacity: 0;
        transition: opacity 2s linear;
        
        &.alert-primary {
            background-color: #007BFF;
            color: #fff;
            font-size: 18px;
            border: none;
        }
        &.alert-error {
            background-color: #b00808;
            color: #fff;
            font-size: 18px;
            border: none;
        }
        .widget {
            position: absolute;
            right: 5px;
            top: 0;
            margin: 10px;
        }
    }
}
button {
  width: 40%;

    @media (min-width: $break-desktop) {
        width: 40%;
    }
}
</style>