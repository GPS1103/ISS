<template>
    <section class="container-fluid">
        <div class="container">
                <div class="login-panel">
                    <div class="alert alert-primary" role="alert" :style="{opacity: isAlertShow ? 1 : 0}">
                        Login successfully. <small>waiting for redirect.</small>
                    </div>
                    <h1 class="display-3 font-weight-bold">Login</h1>
                    <br>
                    <form action="">
                        <div class="form-group">
                            <lable class="input-label">Email</lable>
                            <input type="email" class="form-control" placeholder="Email">
                        </div>
                        <div class="form-group">
                            <lable class="input-label">Password</lable>
                            <input type="password" class="form-control" placeholder="Password">
                        </div>
                        <br>
                        <div class="form-group d-flex justify-content-center">
                            <button class="button" id="login" @click.prevent="login" v-if="!isLoggingIn">Login</button>
                            <button class="button" disabled @click.prevent="login" v-if="isLoggingIn">Login</button>
                            <button class="button" id="register" @click="redirect('Registration')" v-if="!isLoggingIn">Sign Up</button>
                        </div>
                    </form>
                </div>
        </div>
    </section>
</template>

<script>
import { setTimeout } from 'timers';
export default {
    data() {
        return {
            isLoggingIn: false,
            isAlertShow: false
        }
    },
    methods: {
        login() {
            this.isLoggingIn = true
            setTimeout(() => {
                this.isLoggingIn = false
                this.isAlertShow = true
                setTimeout(() => this.redirect('WaterContainer1'), 1000)
            }, 1000)
        },
        redirect(pageName) {
            this.$router.push({name: pageName})
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
  width: 25%;
}
</style>