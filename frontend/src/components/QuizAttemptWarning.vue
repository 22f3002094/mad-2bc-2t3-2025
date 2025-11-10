<template>
    <div class="card shadow-lg  " >
        <div class="card-body">
            <p>{{ msg }}</p>
            <div class="d-flex justify-content-center">
                <router-link to="/student/dashboard" class="btn btn-primary">Go to Dashboard</router-link>  
            </div>
            
        </div>
    </div>
    
</template>
<script>
export default {
    name: "AdminDash",
    props: ['msg'],
}
</script>