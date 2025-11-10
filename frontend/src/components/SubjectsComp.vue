<template>
    <div class="card ms-4 me-4 mt-4">
        <div class="card-header ">
            <div class="d-flex">
                <h3>Subjects</h3>
                <router-link v-if="role === 'Admin'" to="/admin/createsubject" class="btn btn-primary ms-auto"><i class="bi bi-patch-plus"></i>
                    Create</router-link>
            </div>

        </div>
        <div class="card-body">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Name</th>
                        <th scope="col">Description</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(subject, index) in subjects" :key="subject.id">
                        <th scope="row">{{ index + 1 }}</th>
                        <td>{{ subject.name }}</td>
                        <td>{{ subject.description }}</td>
                        <td>
                            <div class="d-flex gap-3">
                                <router-link v-if="role === 'Admin'" :to="'/admin/editsubject/' + subject.id"
                                    class="btn btn-primary">Edit</router-link>
                                <button v-if="role === 'Admin'" class="btn btn-danger" @click="showdelete(index)">Delete</button>
                                <router-link :to="role==='Admin' ? '/admin/' + subject.name + '/quizes' : '/student/' + subject.name + '/quizes'"
                                    class="btn btn-primary">View</router-link>
                            </div>

                        </td>
                        
                    </tr>

                </tbody>
            </table>
        </div>
    </div>
    <div class="modal fade" id="deletesub" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Delete {{ tobedeletesub.name
                    }}</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    Are you sure you want to delete {{ tobedeletesub.name }} Subject?
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary" @click="deletesub">Delete</button>
                </div>
            </div>
        </div>
    </div>

</template>
<script>

export default {
    name: "SubjectDash",
    data() {
        return {
            subjects: [],
            tobedeletesub: {},
            modalinstance: null,
            role: "",
        }
    },
    async mounted() {
        this.role = localStorage.getItem("role")
        try {
            const response = await fetch("http://127.0.0.1:5000/subject?query_type=all",
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
                this.subjects = data
                console.log(this.subjects)
            }
        }
        catch (e) {
            console.log(e.message)
            this.errorMessage = "Something went wrong, try again!! "

        }
    },
    methods: {
        showdelete(index) {
            this.tobedeletesub = { ... this.subjects[index] }
            console.log(this.tobedeletesub)
            const modalElement = document.getElementById('deletesub');
            this.modalinstance = new window.bootstrap.Modal(modalElement);
            this.modalinstance.show()
        },
        async deletesub(){
            try {
                const response = await fetch("http://127.0.0.1:5000/subject?sub_id="+this.tobedeletesub.id,
                                                {
                                                    method: "DELETE",
                                                    headers: {
                                                        "Content-Type": "application/json",
                                                        "Authentication-Token": localStorage.getItem("token")
                                                    }
                                                }
                                            )
                const data =  await response.json()
                if(response.status==404){
                    this.errorMessage=data.message
                }
                else if(response.status==401){
                    this.errorMessage=data.message
                }
                else if(response.status == 200){
                    // this.modalinstance.hide()
                    console.log("deleted")
                   this.$router.go(0)
                    
                }
            }
            catch(e){
                console.log(e.message)
                this.errorMessage = "Something went wrong, try again!! "

            }
        }
    }

}

</script>