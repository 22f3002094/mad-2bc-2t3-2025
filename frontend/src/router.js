import {createWebHistory, createRouter } from 'vue-router'
import AdminDash from "./components/AdminDash.vue";
import HomeComp from "./components/HomeComp.vue";
import LoginComp from "./components/LoginComp.vue";
import RegisterComp from "./components/RegisterComp.vue";
import StudentDash from './components/StudentDash.vue';
import SubForm from './components/SubForm.vue';
import QuizesComp from './components/QuizesComp.vue';
const routes = [
    {
        path: "/", component: HomeComp
    },
    {
        path: "/login", component: LoginComp
    },
    {
        path: "/register", component: RegisterComp
    },
    {
        path : "/admin/dashboard" , component: AdminDash
    },
    {
        path : "/student/dashboard" , component: StudentDash
    },
    {
        path: "/admin/createsubject" , component: SubForm
    },
    {
        path: "/admin/editsubject/:id" , component: SubForm
    },
    {
        path: "/admin/:subject/quizes" , component: QuizesComp

    }


    
]

const router = createRouter({
    history: createWebHistory(),
    routes
}
)


export default router