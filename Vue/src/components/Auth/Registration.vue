<template>
    <section class="container-fluid">
        <div class="container">
                <div class="login-panel">
                    <div class="alert alert-primary" role="alert" :style="{opacity: isAlertShow ? 1 : 0}">
                        Login successfully. <small>waiting for redirect.</small>
                    </div>
                    <h1 class="display-4 font-weight-bold">Sign up and join us!</h1>
                    <p class="font-weight-bold">With an account you have access to many possibilities!</p>
                    <br>
                    <form  action="">
                        <div class="form-group">
                            <label class="input-label">Login</label>
                            <input type="login" @click="clickInput()" class="form-control" placeholder="Login" v-model="login">
                            <span class="register-info">{{ error.login }}</span>
                        </div>
                        <div class="form-group">
                            <label class="input-label">Email</label>
                            <input type="email" @click="clickInput()" class="form-control" placeholder="Email" v-model="email">
                            <span class="register-info">{{ error.email }}</span>
                        </div>
                        <div class="form-group">
                            <label class="input-label">Password</label>
                            <input type="password" @click="clickInput()" class="form-control" placeholder="Password" v-model="password">
                            <span class="register-info">{{ error.password }}</span>
                        </div>
                        <div class="form-group">
                            <label class="input-label">Password one more time</label>
                            <input type="password" @click="clickInput()" class="form-control" placeholder="Password2" v-model="password2">
                            <span class="register-info">{{ error.password2 }}</span>
                        </div>
                        <br>
                        <div class="form-group d-flex justify-content-center">
                            <button class="button" id="register" @click.prevent="register" v-if="!isLoggingIn">Sign Up</button>
                        </div>
                    </form>
                </div>
        </div>
    </section>
</template>

<script>
//import { setTimeout } from 'timers';
import axios from 'axios'
export default {
    data() {
        return {
            login: "",
            email: "",
            password: "",
            password2: "",
            isLoggingIn: false,
            isAlertShow: false,
            error: {
                login: null,
                email: null,
                password: null,
                password2: null
            }
        }
    },
    mounted(){
        const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
        if(appHeader.$data.user) this.$router.push({name: 'WaterContainer1'});
    },
    methods: {
        register() {
            if(!this.validate()) return;
            else {
                //for test
                this.isAlertShow = true
                setTimeout(() => this.redirect('Login'), 2000);
            }
            this.isLoggingIn = true
            axios.post('register', { login: this.login, email: this.email, password: this.password})
                .then(
                    ()=> {
                        this.isLoggingIn = false
                        this.isAlertShow = true
                        setTimeout(() => this.redirect('Login'), 2000);
                    }
                )
                .catch( err => alert(err.message))
        },
        redirect(pageName) {
            this.$router.push({name: pageName})
        },
        validate(){
            console.log(this.login);
            if(this.login.length <= 6){
                this.error.login = "Login musi mieć więcej niż 6 znaków";
                return false;
            }
            if(!this.validateEmail(this.email)){
                this.error.email = "Wprowadz poprawny adres email";
                return false;
            }
            if(!this.validatePassword(this.password)){
                this.error.password = "Hasło powinno zawierać przynajmniej 8 znaków, jedną cyfrę oraz jedną małą i dużą literę";
                return false;
            }
            if(this.password !== this.password2){
                this.error.password2 = "Hasła nie są jednakowe";
                return false;
            }
            return true; 
        },
        validateEmail(email) {
            const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        },
        validatePassword(password){
            const re = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/;
            return re.test(password);
        },
        clickInput(){
            this.isFailAlertShow = false;
            this.required_login = false;
            this.required_password = false;
            this.error.login = "";
            this.error.email = "";
            this.error.password = "";
            this.error.password2 = "";
        }
    }
}
</script>

<style lang="scss" scoped>
section {
  margin-top: 0;
}
.form-group {
  text-align: left;
}
.container{
  width: 40%;
  justify-content: center;
}
.widget {
    margin: 0;
    height: unset;
}
.register-info {
    color: red;
}
.login-panel {
    position: relative;
    padding: 200px 0;
    .alert {
        opacity: 0;
        position: absolute;
        width: 100%;
        top: 100px;
        transition: all .5s;
        &.alert-primary {
            background-color: #007BFF;
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
  margin: 0 5%;
}
</style>