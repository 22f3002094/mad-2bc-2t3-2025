<template>
    <div class="hello">
        <div class="d-flex justify-content-center align-items-center vh-100">
            <div class="card" style="width: 50rem;">
                <div class="card-body">
                    <div v-if="errorMessage" class="alert alert-danger" role="alert">
                        {{ errorMessage }}
                    </div>
                    <div v-if="successMessage" class="alert alert-success" role="alert">
                        {{ successMessage }}
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control" v-model="quizdata.title" id="floatingtitle" required>
                        <label for="floatingtitle">Quiz Title</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control" v-model="quizdata.description" id="floatingdesc" required>
                        <label for="floatingdesc">Quiz Description</label>
                    </div>

                    <div class="card mb-3">
                        <div class="card-header">
                            <div class="d-flex">
                                <h5>Questions</h5>
                                <button class="btn btn-primary ms-auto" data-bs-toggle="modal"
                                    data-bs-target="#question">Create</button>
                            </div>


                        </div>
                        <div class="card-body">
                            <div v-for="(question, index) in quizdata.questions" :key="index" class="card mb-2">
                                <div class="card-body">
                                    <div class="d-flex">
                                        <p class="fs-5 text-muted">Q{{ index + 1 }}. {{ question.statement }} </p>
                                        <div class="ms-auto d-flex gap-2">
                                            <button class="btn btn-primary" @click="showeditquestion(index)">Edit</button>
                                            <button class="btn btn-primary" @click="deletequestion(index)">Delete</button>

                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="date" class="form-control" v-model="quizdata.date" id="floatingdate">
                        <label for="floatingdate">Quiz Date</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control" v-model="quizdata.duration" id="floatingduration" required>
                        <label for="floatingduration">Quiz Duration</label>
                    </div>
                    <button class="btn btn-primary" @click="quiz_id?editquiz() : createquiz()">{{ quiz_id?"Edit" : "Create" }}</button>

                </div>




                <!-- Modal -->
                <div class="modal fade" id="question" tabindex="-1" aria-labelledby="exampleModalLabel"
                    aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h1 class="modal-title fs-5" id="exampleModalLabel">{{question.mode ? 'Edit Question' :'Create Question'}}</h1>
                                <button type="button" class="btn-close" data-bs-dismiss="modal"
                                    aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" v-model="question.statement" required
                                        id="floatingduration">
                                    <label for="floatingduration">Question Statement</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" v-model="question.option_a" required
                                        id="floatingduration">
                                    <label for="floatingduration">Option A</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" v-model="question.option_b" required
                                        id="floatingduration">
                                    <label for="floatingduration">Option B</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" v-model="question.option_c" required
                                        id="floatingduration">
                                    <label for="floatingduration">Option C</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" v-model="question.option_d" required
                                        id="floatingduration">
                                    <label for="floatingduration">Option D</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" v-model="question.correct_option" required
                                        id="floatingduration">
                                    <label for="floatingduration">correct_option</label>
                                </div>
                                <div class="form-floating mb-3">
                                    <input type="text" class="form-control" v-model="question.marks" required
                                        id="floatingduration">
                                    <label for="floatingduration">Marks</label>
                                </div>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="button" class="btn btn-primary" @click="question.mode ?editquestion() : addquestion()">{{question.mode ? 'Edit Question' :'Create Question'}}</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>


export default {
    name: 'SubForm',
    data() {
        return {
            quizdata: {
                title: "",
                description: "",
                total_marks: "",
                date: "",
                duration: "",
                questions: [
                ]
            },
            question: {
                "statement": "",
                "option_a": "",
                "option_b": "",
                "option_c": "",
                "option_d": "",
                "correct_option": "",
                "marks": ""
            },
            errorMessage: "",
            successMessage: "",
            subname: "",
            modalinstance:null,
            quiz_id :null
        }
    },
    async mounted() {
    
        this.subname = this.$route.params.subname
        this.quiz_id = this.$route.params.quiz_id
        console.log(this.quiz_id)
        if (this.quiz_id) {
          try {
            const response = await fetch(`http://127.0.0.1:5000/quiz?quiz_id=${this.quiz_id}`,
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

              this.quizdata=data
            }
          }
          catch (e) {
            this.errorMessage = "something went wrong, Try again"
          }
        }

      },

    methods: {
        addquestion(){
            this.quizdata.questions.push(this.question)
            

            const modalElement = document.getElementById('question');
            const modal = window.bootstrap.Modal.getInstance(modalElement);
            this.question = {
                "statement": "",
                "option_a": "",
                "option_b": "",             
                "option_c": "",
                "option_d": "",
                "correct_option": "",


                "marks": ""
            }
            
            modal.hide()
        },
        deletequestion(index){
            this.quizdata.questions.splice(index,1)
        },
        showeditquestion(index){
            const modalElement = document.getElementById('question');
            this.modalinstance = new window.bootstrap.Modal(modalElement);
            this.question = { ...this.quizdata.questions[index] }
            this.question.mode = "edit"
            this.question.index=index
            this.modalinstance.show()

        },
        editquestion(){
            console.log(this.question)
            this.quizdata.questions[this.question.index] = { ...this.question }
            this.question   = {
                "statement": "",
                "option_a": "",
                "option_b": "",             
                "option_c": "",
                "option_d": "",
                "correct_option": "",


                "marks": ""
            }
    
            this.modalinstance.hide()
        },
        async createquiz() {

            try {
                const response = await fetch(`http://127.0.0.1:5000/quiz?sub_name=${this.subname}`,
                    {
                        method: "POST",
                        body: JSON.stringify(this.quizdata),
                        headers: {
                            "Content-Type": "application/json",
                            "Authentication-Token": localStorage.getItem("token")
                        }
                    }
                )
                const data = response.json()
                if (response.status == 409) {
                    this.errorMessage = data.message
                }
                else if (response.status === 401) {
                    this.$router.push("/login")
                }
                else if (response.status === 500) {
                    new Error("internal server error")
                }
                else if (response.status === 201) {
                    this.successMessage = "Quiz is created"
                    setTimeout(() => {
                        this.$router.push(`/admin/${this.subname}/quizes`)
                    }, 2000);

                }
            }
            catch (e) {
                this.errorMessage = "something went wrong, Try again"
            }

        },
        async editquiz() {

          try {
            const response = await fetch("http://127.0.0.1:5000/quiz?quiz_id="+this.quiz_id,
              {
                method: "PUT",
                body: JSON.stringify(this.quizdata),
                headers: {
                  "Content-Type": "application/json",
                  "Authentication-Token": localStorage.getItem("token")
                }
              }
            )
            const data = response.json()
            if (response.status == 409) {
              this.errorMessage = data.message
            }
            else if (response.status === 404) {
              this.$router.push("/admin/dashboard")
            }
            else if (response.status === 401) {
              this.$router.push("/login")
            }
            else if (response.status === 500) {
              new Error("internal server error")
            }
            else if (response.status === 200) {
              this.successMessage = "Quiz is updated"
              setTimeout(() => {
                this.$router.push("/admin/dashboard")
              }, 2000);

            }
          }
          catch (e) {
            this.errorMessage = "something went wrong, Try again"
          }

        },

    }

}
</script>
