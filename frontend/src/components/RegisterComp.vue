<template>
    <div class="hello">
        <div class="d-flex justify-content-center align-items-center vh-100">
            <div class="card" style="width: 18rem;">
                <div class="card-body">
                    <div v-if="errorMessage" class="alert alert-danger" role="alert">
                        {{ errorMessage }}
                    </div>
                    <div v-if="successMessage" class="alert alert-success" role="alert">
                        {{ successMessage }}
                    </div>
                    <div class="form-floating mb-3">
                        <input type="text" class="form-control" v-model="registerdata.name" id="floatingInput">
                        <label for="floatingInput">Name</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input type="email" class="form-control" v-model="registerdata.email" id="floatingInput"
                            placeholder="name@example.com" name="email">
                        <label for="floatingInput">Email address</label>
                    </div>
                    <div class="form-floating">
                        <input type="password" class="form-control" v-model="registerdata.password"
                            id="floatingPassword" placeholder="Password" name="password">
                        <label for="floatingPassword">Password</label>
                    </div>
                    <button type="submit" class="btn btn-primary mt-3" @click="register">Register</button>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
export default {
    name: "RegisterComp",
    data() {
        return {
            registerdata: {
                name: "",
                email: "",
                password: "",
            },
            errorMessage: "",
            successMessage: ""
        }
    },
    methods: {
        async register() {
            try {
                const response = await fetch("http://127.0.0.1:5000/register",
                                                {
                                                    method: "POST",
                                                    body: JSON.stringify(this.registerdata),
                                                    headers: {
                                                        "Content-Type": "application/json"
                                                    }
                                                }
                                            )
                const data =  await response.json()
                if(response.status==400){
                    this.errorMessage=data.message
                }
                else if(response.status==409){
                    this.errorMessage=data.message
                }
                else if(response.status == 201){
                    this.successMessage = data.message
                    setTimeout(() => {
                        this.$router.push("/login")
                    }, 2000);
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