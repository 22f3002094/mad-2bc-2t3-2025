<template>
    <Navbar></Navbar>
    <div class="d-flex gap-2 mt-2">
        <h2>{{ greetings }}</h2>
        <button class="btn btn-primary ms-auto me-5" @click="download_csv">Download CSV</button>
    </div>

    <SubjectsComp></SubjectsComp>
    <UserComp></UserComp>

</template>
<script>
import Navbar from './Navbar.vue';
import SubjectsComp from './SubjectsComp.vue';
import UserComp from './UserComp.vue';

export default {
    name: "AdminDash",
    data() {
        return {
            greetings: "Welcome to Admin dashboard"
        }
    },
    components: {
        Navbar,
        SubjectsComp,
        UserComp
    },
    methods: {
        async download_csv() {
            try {
                const response = await fetch("http://127.0.0.1:5000/admin/export_csv",
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
                    this.errorMessage = data.message
                }
                else if (response.status == 500) {
                    this.errorMessage = data.message
                }
                else if (response.status == 200) {
                    console.log(data.task_id)
                    const task_id = data.task_id
                    let count = 0
                    const interval = setInterval(async () => {
                        console.log(count++)
                        const res = await fetch("http://127.0.0.1:5000/admin/download_csv?task_id=" + task_id,
                            {
                                method: "GET",
                                headers: {
                                    "Content-Type": "application/json",
                                    "Authentication-Token": localStorage.getItem("token")
                                }
                            }
                        )
                        
                        if (res.status == 202) {
                            console.log("CSV generation in progress...")
                        }
                        else if (res.status == 200) {

                            clearInterval(interval)
                            window.location.href="http://127.0.0.1:5000/admin/download_csv?task_id="+ task_id
                        }


                    } , 2000)

                }
            } catch (error) {
                console.log("Error:", error)
                this.$router.push('/admin/dashboard')
            }
        }
    }
}
</script>
