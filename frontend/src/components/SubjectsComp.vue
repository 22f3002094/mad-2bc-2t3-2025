<template>
    <div class="card ms-4 me-4 mt-4">
        <div class="card-header ">
            <div class="d-flex">
                <h3>Subjects</h3>
                <router-link to="/admin/createsubject" class="btn btn-primary ms-auto"><i class="bi bi-patch-plus"></i> Create</router-link>
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
                    <tr v-for="(subject,index) in subjects" :key="subject.id">
                        <th scope="row">{{ index +1 }}</th>
                        <td>{{ subject.name }}</td>
                        <td>{{ subject.description }}</td>
                        <td>
                            <div class="d-flex gap-3">
                                <router-link :to="'/admin/editsubject/'+subject.id" class="btn btn-primary">Edit</router-link>
                                <button class="btn btn-danger">Delete</button>
                                <router-link :to="'/admin/'+subject.name+'/quizes'" class="btn btn-primary">View</router-link>
                            </div>

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
            subjects: []
        }
    },
    async mounted() {

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
    }

}

</script>