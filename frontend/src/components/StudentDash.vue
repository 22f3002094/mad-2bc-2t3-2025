<template>
    <Navbar></Navbar>
    <SubjectsComp></SubjectsComp>
    
</template>
<script>
import Navbar from './Navbar.vue';
import SubjectsComp from './SubjectsComp.vue';
export default {
    name:"StudentDash",
    data(){
        return {
            greetings : "Welcome to Student dashboard"
        }
    },
    components:{
        Navbar,
        SubjectsComp
    }
}

</script>