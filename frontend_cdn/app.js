import HomeComp from "./homecomp.js"

new Vue({
    el: '#app',
    template:
    `
    <HomeComp></HomeComp>
    `,
    data:{
        appname : "Quizmaster"
    } ,
    components:{
         HomeComp
    }
})