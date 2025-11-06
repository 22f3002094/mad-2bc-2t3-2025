import {createWebHistory, createRouter } from 'vue-router'
import AdminDash from "./components/AdminDash.vue";
import HomeComp from "./components/HomeComp.vue";
import LoginComp from "./components/LoginComp.vue";
import RegisterComp from "./components/RegisterComp.vue";
const routes = [
    {
        path: "/", component: HomeComp
    },
    {
        path: "/login", component: LoginComp
    },
    {
        path : "/admin/dashboard" , component: AdminDash
    },
    {
        path: "/register", component: RegisterComp
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
}
)


export default router