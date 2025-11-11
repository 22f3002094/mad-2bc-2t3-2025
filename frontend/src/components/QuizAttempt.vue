<template>
    <div v-if="message" class="d-flex justify-content-center align-items-center vh-100">
        <QuizAttemptWarning :msg="message"></QuizAttemptWarning>
    </div>
    <div v-else>

        <div class="text-center">
            <h3>{{ quiz_data.title }}</h3>
            <p class="text-muted">Total Marks : {{ quiz_data.total_marks }}</p>
        </div>
        <div v-for="(question, index) in quiz_data.questions" class="card shadow-lg mt-3 ms-5 me-5" :key="index">
            <div class="card-body">
                <div class="d-flex">
                    <p class="fs-4"><strong>Q.{{ index + 1 + " " + question.statement }}</strong></p>
                    <p class="fs-5 ms-auto">Marks : {{ question.marks }}</p>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" v-model="attempt_data.options_selected[index]"
                        value="1" :id="`radioDefault-${index}1`">
                    <label class="form-check-label" :for="`radioDefault-${index}1`">
                        {{ question.option_a }}
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" v-model="attempt_data.options_selected[index]"
                        value="2" :id="`radioDefault-${index}2`">
                    <label class="form-check-label" :for="`radioDefault-${index}2`">
                        {{ question.option_b }}
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" v-model="attempt_data.options_selected[index]"
                        value="3" :id="`radioDefault-${index}3`">
                    <label class="form-check-label" :for="`radioDefault-${index}3`">
                        {{ question.option_c }}
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" v-model="attempt_data.options_selected[index]"
                        value="4" :id="`radioDefault-${index}4`">
                    <label class="form-check-label" :for="`radioDefault-${index}4`">
                        {{ question.option_d }}
                    </label>
                </div>


            </div>

        </div>
        <div class="d-flex justify-content-center mt-5">
            <button class="btn btn-primary" @click="submitquiz">Submit</button>
        </div>
    </div>

</template>
<script>
import QuizAttemptWarning from './QuizAttemptWarning.vue';
export default {
    name: "AdminDash",
    data() {
        return {
            quiz_data: {},
            message: "",
            quiz_id: "",
            attempt_data: {}

        }
    },
    components: {
        QuizAttemptWarning
    },
    async mounted() {
        this.quiz_id = this.$route.params.quiz_id
        try {
            const response = await fetch("http://127.0.0.1:5000/quiz/attempt?quiz_id=" + this.quiz_id,
                {
                    "method": "GET",
                    "headers": {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    }

                }
            )
            const data = await response.json()
            if (response.status == 200) {
                this.quiz_data = data
                this.attempt_data.quiz_id = this.quiz_data.id
                this.attempt_data.options_selected = Array(this.quiz_data.questions.length).fill(0)
                console.log(this.attempt_data)
            }
            if (response.status == 403) {
                this.message = data.message
            }
            if (response.status == 401) {
                this.$router.push("/login")
            }
            if (response.status == 500) {
                new Error("Server Error")
            }
            if (response.status == 404) {
                this.$router.push("/student/dashboard")
            }

        }
        catch (e) {
            console.log(e)
            this.$router.push("/student/dashboard")
        }

    },
    methods: {
        async submitquiz() {
            console.log(this.attempt_data)
            try {
                const response = await fetch("http://127.0.0.1:5000/quiz/attempt?quiz_id=" + this.quiz_id,
                    {
                        "method": "POST",
                        "body": JSON.stringify(this.attempt_data),
                        "headers": {
                            "Content-Type": "application/json",
                            "Authentication-Token": localStorage.getItem("token")
                        }

                    }
                )
                const data = await response.json()
                if (response.status == 201) {
                    
                    this.$router.push("/student/dashboard")
                }
                if (response.status == 403) {
                    this.message = data.message
                }
                if (response.status == 401) {
                    this.$router.push("/login")
                }
                if (response.status == 500) {
                    new Error("Server Error")
                }
                if (response.status == 404) {
                    this.$router.push("/student/dashboard")
                }

            }
            catch (e) {
                console.log(e)
                this.$router.push("/student/dashboard")
            }

        }
    }


}
</script>