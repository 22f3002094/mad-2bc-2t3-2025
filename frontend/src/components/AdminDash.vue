<template>
    <Navbar></Navbar>
    <h2>{{ greetings }}</h2>
    <SubjectsComp></SubjectsComp>
    <UserComp></UserComp>
    
</template>
<script>
import Navbar from './Navbar.vue';
import SubjectsComp from './SubjectsComp.vue';
import UserComp from './UserComp.vue';

export default {
    name:"AdminDash",
    data(){
        return {
            greetings : "Welcome to Admin dashboard"
        }
    },
    components:{
        Navbar,
        SubjectsComp,
        UserComp
    }
}

</script>