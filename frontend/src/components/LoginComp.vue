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
            <input type="email" class="form-control" v-model="formdata.email" id="floatingInput"
              placeholder="name@example.com" name="email">
            <label for="floatingInput">Email address</label>
          </div>
          <div class="form-floating">
            <input type="password" class="form-control" v-model="formdata.password" id="floatingPassword"
              placeholder="Password" name="password">
            <label for="floatingPassword">Password</label>
          </div>
          <button type="submit" class="btn btn-primary mt-3" @click="login">Login</button>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginComp',
  data() {
    return {
      formdata: {
        email: "",
        password: ""
      },
      errorMessage: "",
      successMessage: ""
    }
  },
  methods: {
    login() {
      fetch("http://127.0.0.1:5000/login",
        {
          method: "POST",
          body: JSON.stringify(this.formdata),
          headers: {
            "Content-Type": "application/json"
          }
        }
      ).then(
        (res) => this.onloginfullfil(res),
        (rej) => this.onloginreject(rej)
      )

    },
    onloginfullfil(response) {
      response.json().then(
        (data) => {
          if (response.status == 400) {
            this.errorMessage = data.message
          }
          else if (response.status == 404) {
            this.errorMessage = data.message
          }
          else if (response.status == 401) {
            this.errorMessage = data.message
          }
          else if (response.status == 200) {
            localStorage.setItem("token", data.token)
            localStorage.setItem("name", data.name)

            this.successMessage = data.message
            setTimeout(() => {
              this.$router.push("/admin/dashboard")
            }, 2000);

          }
          else {
            this.onloginreject()
          }
        }
      )


    },
    onloginreject() {

      this.errorMessage = "Something went wrong. Please try again"
    }
  }

}
</script>
