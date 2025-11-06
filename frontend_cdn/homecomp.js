export default({
    template:
    `
    <div class="d-flex justify-content-center align-items-center vh-100">
        <div>
            <h3>Welcome to Quizmaster</h3>
            <div class="">
                <a href="/login" class="btn btn-primary">Login</a>
                <a href="/register" class="btn btn-primary">Register</a>
            </div>
        </div>
        
    </div>
    `
    data(){
        return {
            greeting: "Welcome to Quizmaster"
        }
    },
    mounted(){
        console.log("Home component mounted")
    },
    methods: {
       greet(){
        console.log(this.greeting)
       }
    }
})