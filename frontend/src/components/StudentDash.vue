<template>
    <Navbar></Navbar>
    <h2>{{ greetings }}</h2>
    
</template>
<script>
import Navbar from './Navbar.vue';
export default {
    name:"StudentDash",
    data(){
        return {
            greetings : "Welcome to Student dashboard"
        }
    },
    components:{
        Navbar
    }
}

</script>