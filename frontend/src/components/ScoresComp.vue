<template>
    <div class="card ms-4 me-4 mt-4">
        <div class="card-header ">
            <div class="d-flex">
                <h3>Scores</h3>
            </div>

        </div>
        <div class="card-body">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Quiz_title</th>
                        <th scope="col">Score</th>
                        <th scope="col">Date Attempted</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(score, index) in scores" :key="index">
                        <th scope="row">{{ index + 1 }}</th>
                        <td>{{ score.quiz_title }}</td>
                        <td>{{ score.score }}</td>
                        <td>{{ score.date_attempted }}</td>
                        <td>
                            <router-link :to="`/student/viewattempt/${score.id}`" class="btn btn-primary">View Attempt</router-link>

                        </td>
                        
                    </tr>

                </tbody>
            </table>
        </div>
    </div>
    

</template>
<script>

export default {
    name: "SubjectDash",
    data() {
        return {
            scores: [],
        }
    },
    async mounted() {
        
        try {
            const response = await fetch("http://127.0.0.1:5000/score",
                {
                    method: "GET",
                    headers: {
                        "Content-Type": "application/json",
                        "Authentication-Token": localStorage.getItem("token")
                    }
                }
            )
            const data = await response.json()
            if (response.status == 401) {
                this.$router.push("/login")
            }
            else if (response.status == 500) {
                new Error("something went worng")
            }
            else if (response.status == 200) {
                this.scores = data
                console.log(this.scores)
            }
        }
        catch (e) {
            console.log(e.message)
            this.errorMessage = "Something went wrong, try again!! "

        }
    },
    methods: {
        
    }

}

</script>