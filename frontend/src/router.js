import {createWebHistory, createRouter } from 'vue-router'
import AdminDash from "./components/AdminDash.vue";
import HomeComp from "./components/HomeComp.vue";
import LoginComp from "./components/LoginComp.vue";
import RegisterComp from "./components/RegisterComp.vue";
import StudentDash from './components/StudentDash.vue';
import SubForm from './components/SubForm.vue';
import QuizesComp from './components/QuizesComp.vue';
import QuizForm from './components/QuizForm.vue';
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
        path: "/admin/:subname/quizes" , component: QuizesComp

    },
    {
        path: "/admin/:subname/createquiz" , component: QuizForm

    },
    {
        path: "/admin/editquiz/:quiz_id" , component: QuizForm
    },
    
]

const router = createRouter({
    history: createWebHistory(),
    routes
}
)


export default router