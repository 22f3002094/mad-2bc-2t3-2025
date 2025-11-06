import HomeComp from "./homecomp.js"
import logincomp  from "./logincomp.js"


const routes = [ 
    {
        "path" : "/",
        "component" : HomeComp
    },
    {
        "path" : "/login",
        "component" : logincomp
    }
]

const router = new VueRouter({
    routes
})

export default router