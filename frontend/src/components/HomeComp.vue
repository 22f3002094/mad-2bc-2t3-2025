<template>
<div class="d-flex justify-content-center align-items-center vh-100">
        <div>
            <h3>{{ greetings }}</h3>
            <div class="d-flex gap-3 mt-3">
                <a href="/login" class="btn btn-primary">Login</a>
                <a href="/register" class="btn btn-primary">Register</a>
            </div>
        </div>
        
    </div>

</template>


<script>
export default {
    name: "HomeComp",
    data() {
        return {
            greetings: "Welcome to quiz master"
        }
    },
    mounted() {
        console.log("i am mounted")
    },
    methods : {
        buttonclick(){
            console.log("button is clicked")
        }
    }
}
</script>