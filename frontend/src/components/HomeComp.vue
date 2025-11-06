<template>
    <div>
        <h2>{{ greetings }}</h2>
        <button class="btn btn-primary" @click="buttonclick"> Click here</button>
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