<template>
    <section class="container-fluid">
        <div class="container">
                <div class="login-panel">
                    <div class="alert alert-primary" role="alert" :style="{opacity: isAlertShow ? 1 : 0, 'background-color': isError ? '#b00808 !important' : '#007BFF'}">
                        <span :style="{display: isLoggingIn ? 'block' : 'none'}">Jesteś zarejestrowany! <br><small>Nastąpi przekierowanie do strony logowania</small></span>                        
                        <span :style="{display: isError ? 'block' : 'none'}">Błąd podczas rejestracji! <br><small>{{ errorMessage }}</small></span>                        
                    </div>
                    <h1 class="display-5 font-weight-bold">Zarejestruj konto i korzystaj w pełni!</h1>
                    <p class="font-weight-bold">Konto umożliwia dostęp do pozostałych aplikacji!</p>
                    <br>
                    <form  action="">
                        <div class="form-group">
                            <label class="input-label">Nazwa</label>
                            <input type="login" @click="clickInput()" class="form-control" placeholder="Nazwa użytkownika" v-model="name">
                            <span class="register-info">{{ error.name }}</span>
                        </div>
                        <div class="form-group">
                            <label class="input-label">Email</label>
                            <input type="email" @click="clickInput()" class="form-control" placeholder="Email" v-model="email">
                            <span class="register-info">{{ error.email }}</span>
                        </div>
                        <div class="form-group">
                            <label class="input-label">Hasło</label>
                            <input type="password" @click="clickInput()" class="form-control" placeholder="Hasło" v-model="password">
                            <span class="register-info">{{ error.password }}</span>
                        </div>
                        <div class="form-group">
                            <label class="input-label">Powtórz hasło</label>
                            <input type="password" @click="clickInput()" class="form-control" placeholder="Powtórz hasło" v-model="password2">
                            <span class="register-info">{{ error.password2 }}</span>
                        </div>
                        <br>
                        <div class="form-group d-flex justify-content-center">
                            <button class="button" id="register" @click.prevent="register" v-if="!isLoggingIn">Zarejestruj</button>
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
            name: "",
            email: "",
            password: "",
            password2: "",
            isLoggingIn: false,
            isError: false,
            isAlertShow: false,
            error: {
                name: null,
                email: null,
                password: null,
                password2: null
            },
            errorMessage: null
        }
    },
    mounted(){
        const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
        if(appHeader.$data.user) this.$router.push({name: 'WaterContainer1'});
    },
    methods: {
        register() {
            this.isError = false;
            this.isLoggingIn = false;
            this.errorMessage = null;
            this.isAlertShow = false;
            if(!this.validate()) return;
            
            axios.post('https://iss-server-app.herokuapp.com/api/register', { 
                name: this.name, email: this.email, password: this.password, password_confirmation: this.password2 })
                .then(
                    ()=> {
                        //console.log(res);
                        this.isLoggingIn = true;
                        this.isAlertShow = true;
                        setTimeout(() => this.redirect('Login'), 2000);
                    }
                )
                .catch( (err) => {
                    if(err.response.status == 422){
                        this.errorMessage = err.response.data.errors.email[0];
                    }
                    this.isAlertShow = true
                    this.isError = true;
                    //console.log(err.response);

                    })
        },
        redirect(pageName) {
            this.$router.push({name: pageName})
        },
        validate(){
            console.log(this.name);
            if(this.name.length <= 2){
                this.error.name = "Nazwa musi mieć więcej niż 2 znaki";
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
            this.required_name = false;
            this.required_password = false;
            this.error.name = "";
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
    padding: 100px 0;
    .alert {
        opacity: 0;
        position: absolute;
        width: 100%;
        top: 10px;
        transition: all .5s;
        right: 0%;
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