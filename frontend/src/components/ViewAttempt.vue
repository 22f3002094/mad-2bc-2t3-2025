<template>


    <div class="text-center">
        <h3>{{ quiz_data.title }}</h3>
        <p class="text-muted">Marks Scored : {{ quiz_data.user_score }}/{{ quiz_data.total_marks }}</p>
    </div>
    <div v-for="(question, index) in quiz_data.questions" class="card shadow-lg mt-3 ms-5 me-5" :key="index">
        <div class="card-body">
            <div class="d-flex">
                <p class="fs-4"><strong>Q.{{ index + 1 + " " + question.statement }}</strong></p>
                <p class="fs-5 ms-auto">Marks : {{ question.marks }}</p>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" v-model="quiz_data.user_attempt[index]"  value="1"
                    :id="`radioDefault-${index}1`" disabled>
                <label class="form-check-label" :for="`radioDefault-${index}1`">
                    <div v-html="getoptionlabel(question.correct_option, question.option_a, quiz_data.user_attempt[index] , opt_num=1)"></div>
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" v-model="quiz_data.user_attempt[index]"  value="2"
                    :id="`radioDefault-${index}2`" disabled>
                <label class="form-check-label" :for="`radioDefault-${index}2`">
                    <div v-html="getoptionlabel(question.correct_option, question.option_b, quiz_data.user_attempt[index], opt_num=2)"></div>
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" v-model="quiz_data.user_attempt[index]"  value="3"
                    :id="`radioDefault-${index}3`" disabled>
                <label class="form-check-label" :for="`radioDefault-${index}3`">
                    <div v-html="getoptionlabel(question.correct_option, question.option_c, quiz_data.user_attempt[index], opt_num=3)"></div>
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio"    v-model="quiz_data.user_attempt[index]"  value="4"
                    :id="`radioDefault-${index}4`" disabled>
                <label class="form-check-label" :for="`radioDefault-${index}4`">
                    <div v-html="getoptionlabel(question.correct_option, question.option_d, quiz_data.user_attempt[index], opt_num=4)"></div>
                </label>
            </div>


        </div>

    </div>


</template>
<script>
export default {
    name: "ViewAttempt",
    data() {
        return {
            quiz_data: {},
            message: "",
            score_id: "",
            
        }
    },
    methods:{
        getoptionlabel(correct_option,option , user_selected, opt_num){
            if(user_selected == correct_option && opt_num == correct_option){
                return `<span class="text-success fw-bold">${ option } </span>`
            }
            else if(user_selected != correct_option && opt_num == user_selected){
                return `<span class="text-danger fw-bold">${ option } </span>`
            }
            else{
                if(opt_num == correct_option){
                    return `<span class="text-success fw-bold">${ option } </span>`
                }
                return option
            }
        }
    },
   
    async mounted() {
        this.score_id = this.$route.params.score_id
        try {
            const response = await fetch("http://127.0.0.1:5000/score?score_id=" + this.score_id,
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
</script>