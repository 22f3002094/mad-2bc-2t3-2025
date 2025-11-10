<template>
    <Navbar></Navbar>
    <div class="card ms-4 me-4 mt-4">
        <div class="card-header ">
            <div class="d-flex">
                <h3>{{ sub_name }} Quizzes</h3>
                <router-link v-if="role === 'Admin'" :to="'/admin/'+sub_name+'/createquiz'" class="btn btn-primary ms-auto"><i class="bi bi-patch-plus"></i>
                    Create</router-link>
            </div>

        </div>
        <div class="card-body">
            <div class="row">
                <div v-for="(quiz, index) in quizzes" class="col-3 mb-3" :key="index">
                    <div class="card text-center">
                        <div class="card-body">
                            <h5>{{ quiz.title }}</h5>
                            <p class="text-muted">Date : {{ quiz.date }}</p>
                            <div class="d-flex gap-2 ">
                                <router-link :to="role==='Admin' ? '/admin/'+sub_name+'/viewquiz' : '/student/attemptquiz/'+ quiz.id" class="btn btn-primary">View</router-link>
                                <router-link v-if="role === 'Admin'" :to="'/admin/editquiz/'+ quiz.id" class="btn btn-info">Edit</router-link>

                                <button v-if="role === 'Admin'" class="btn btn-danger">Delete</button>
                            </div>

                        </div>
                    </div>

                </div>



            </div>

        </div>
    </div>


</template>


<script>
import Navbar from './Navbar.vue';
export default {
    name: "HomeComp",
    data() {
        return {
            greetings: "Welcome to quiz master",
            sub_name: "",
            quizzes: [],
            role: "",
        }
    },
    async mounted() {
        this.sub_name = this.$route.params.subname
        this.role= localStorage.getItem("role")
        if (this.sub_name) {
            try {
                const response = await fetch(`http://127.0.0.1:5000/quiz?subname=${this.sub_name}`,
                    {
                        method: "GET",
                        headers: {
                            "Content-Type": "application/json",
                            "Authentication-Token": localStorage.getItem("token")
                        }
                    }
                )
                const data = await response.json()
                if (response.status == 404) {
                    this.$router.push("/admin/dashboard")
                }
                else if (response.status === 401) {
                    this.$router.push("/login")
                }
                else if (response.status === 500) {
                    new Error("internal server error")
                }
                else if (response.status === 200) {

                    this.quizzes = data
                    

                }
            }
            catch (e) {
                this.errorMessage = "something went wrong, Try again"
                this.$router.push("/admin/dashboard")
            }
        }
    },
    components: {
        Navbar
    }

}
</script>