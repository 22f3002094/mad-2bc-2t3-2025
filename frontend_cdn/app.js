
import router from "./route.js"
new Vue({
    el: '#app',
    template:
    `
    <div>
        <router-view></router-view>
    </div>
    
    `,
    data:{
        appname : "Quizmaster"
    } ,
    router: router
})