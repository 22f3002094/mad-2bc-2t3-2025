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
            <input type="text" class="form-control" v-model="subjectdata.name" id="floatingName">
            <label for="floatingName">Subject Name</label>
          </div>
          <div class="form-floating">
            <input type="text" class="form-control" v-model="subjectdata.description" id="floatingDescription">
            <label for="floatingDescription">Description</label>
          </div>
          <button type="submit" class="btn btn-primary mt-3" @click="sub_id?edit():create()">{{ sub_id ? 'Edit' : "Create" }}</button>
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
      subjectdata: {
        name: "",
        description: ""
      },
      errorMessage: "",
      successMessage: "",
      sub_id: ""
    }
  },
  async mounted() {
    console.log("sdkfjsdfsd")
    this.sub_id = this.$route.params.id
    console.log(this.sub_id)
    if (this.sub_id) {
      try {
        const response = await fetch(`http://127.0.0.1:5000/subject?sub_id=${this.sub_id}`,
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
          
          this.subjectdata=data
          console.log(this.subjectdata)
        }
      }
      catch (e) {
        this.errorMessage = "something went wrong, Try again"
      }
    }

  },

  methods: {
    async create() {

      try {
        const response = await fetch("http://127.0.0.1:5000/subject",
          {
            method: "POST",
            body: JSON.stringify(this.subjectdata),
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
          this.successMessage = "Subject is created"
          setTimeout(() => {
            this.$router.push("/admin/dashboard")
          }, 2000);

        }
      }
      catch (e) {
        this.errorMessage = "something went wrong, Try again"
      }

    },
    async edit () {

      try {
        const response = await fetch("http://127.0.0.1:5000/subject",
          {
            method: "PUT",
            body: JSON.stringify(this.subjectdata),
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
          this.successMessage = "Subject is updated"
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
