<template>
    <Navbar></Navbar>
    <SubjectsComp></SubjectsComp>
    <ScoresComp></ScoresComp>
</template>
<script>
import Navbar from './Navbar.vue';
import SubjectsComp from './SubjectsComp.vue';
import ScoresComp from './ScoresComp.vue';
export default {
    name:"StudentDash",
    data(){
        return {
            greetings : "Welcome to Student dashboard"
        }
    },
    components:{
        Navbar,
        SubjectsComp,
        ScoresComp
    }
}

</script>