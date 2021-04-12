import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
import WaterContainer1 from '../views/WaterContainer1'
import WaterContainer2 from '../views/WaterContainer2'
import WaterContainer3 from '../views/WaterContainer3'
import WaterContainer4 from '../views/WaterContainer4'
import Login from '../components/Auth/Login'
import Registration from '../components/Auth/Registration'

const routes = [
    {
        path: "/WaterContainer4",
        name: "WaterContainer4",
        component: WaterContainer4,
        meta: {
            number: 4
        }
    },
    {
        path: "/WaterContainer3",
        name: "WaterContainer3",
        component: WaterContainer3,
        meta: {
            number: 3
        }
    },
    {
        path: "/WaterContainer2",
        name: "WaterContainer2",
        component: WaterContainer2,
        meta: {
            number: 2
        }
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
        meta: {
            number: 5
        }
    },
    {
        path: "/registration",
        name: "Registration",
        component: Registration,
        meta: {
            number: 6
        }
    },
    {
        path: "*",
        name: "WaterContainer1",
        component: WaterContainer1,
        meta: {
            number: 1
        }
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router;
 