<template>
    <section class="container-fluid">
        <div class="container">
                <div class="login-panel">
                    <div class="alert alert-primary" role="alert" :style="{opacity: isSuccessAlertShow ? 1 : 0}">
                        Login successfully. <small>waiting for redirect.</small>
                    </div>
                    <div class="alert alert-error" role="alert" :style="{opacity: isFailAlertShow ? 1 : 0}">
                        Login error
                    </div>
                    <h1 class="display-3 font-weight-bold">Login</h1>
                    <br>
                    <form action="">
                        <div class="form-group">
                            <label class="input-label">Login</label>
                            <input type="login" @click="clickInput()" class="form-control" placeholder="Login" v-model="login">
                            <span class="login-validate" v-if="required_login">To pole jest wymagane</span>
                        </div>
                        <div class="form-group">
                            <label class="input-label">Password</label>
                            <input type="password" @click="clickInput()" class="form-control" placeholder="Password" v-model="password">
                            <span class="login-validate" v-if="required_password">To pole jest wymagane</span>
                        </div>
                        <br>
                        <div class="form-group d-flex justify-content-center">
                            <button class="button" id="login" @click.prevent="logUser">Login</button>
                            <button class="button" id="register" @click="redirect('Registration')">Sign Up</button>
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
            login: null,
            password: null,
            isLoggingIn: false,
            isSuccessAlertShow: false,
            isFailAlertShow: false,
            required_password: false,
            required_login: false
        }
    },
    mounted(){
        const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
        if(appHeader.$data.user) this.$router.push({name: 'WaterContainer1'});
    },
    methods: {
        logUser() {
            console.log(this.$store);
            const loginRequired = this.isRequired("login");
            const passwordRequired = this.isRequired("password");
            if(this.login == "test" && this.password == "test"){
                const appHeader = this.$parent.$children.find( child => { return child.$options.name == "AppHeader"});
                appHeader.$data.user = "test"
                this.isSuccessAlertShow = true;      
                setTimeout(() => {
                    const appFooter = this.$parent.$children.find(child => { return child.$options.name === "AppFooter"})
                    appFooter.$data.items.forEach( item => item.disabled = false);
                    this.redirect('WaterContainer1')
                }, 2000);
            }
            else if(!loginRequired && !passwordRequired){
                this.required_login = false;
                this.required_password = false;

                axios.post('loginUser',{
                    login: this.login,
                    password: this.password
                }). then(
                    res => {
                        this.isSuccessAlertShow = true;
                        console.log(res);
                        //localStorage.setItem('token') = res.token;
                        setTimeout(() => this.redirect('WaterContainer1'), 2000);
                        }
                ).catch( err => {
                    this.isFailAlertShow = true;
                    console.log(err.message)}
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
            this.isFailAlertShow = false;
            this.required_login = false;
            this.required_password = false;
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
.login-validate {
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
        &.alert-error {
            background-color: #ff0800bb;
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
  width: 25%;
}
</style>