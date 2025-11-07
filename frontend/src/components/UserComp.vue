<template>
    <div class="card ms-4 me-4 mt-4">
        <div class="card-header ">
            <div class="d-flex">
                <h3>Students</h3>
                
            </div>

        </div>
        <div class="card-body">
            <table class="table table-bordered">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Student Name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Status</th>
                        <th scope="col">Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(student,index) in students" :key="student.id">
                        <th scope="row">{{ index+1 }}</th>
                        <td>{{ student.name }}</td>
                        <td>{{ student.email }}</td>
                        <td>{{ student.status }}</td>

                        <td>
                            <div class="d-flex gap-3">
                                <button class="btn btn-primary">Flag</button>
                                <button class="btn btn-primary">View</button>
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
            students: []
        }
    },
    async mounted() {

        try {
            const response = await fetch("http://127.0.0.1:5000/student?query_type=all",
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
                this.students = data
                console.log(this.students)
            }
        }
        catch (e) {
            console.log(e.message)
            this.errorMessage = "Something went wrong, try again!! "

        }
    }

}

</script>