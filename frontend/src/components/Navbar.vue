<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">QuizMaster</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0 fs-4">
                    <li class="nav-item">
                        <router-link to="/admin/dashboard" class="nav-link active" aria-current="page" >Dashboard</router-link>
                    </li>

                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                            aria-expanded="false">
                            <i class="bi bi-person"></i>
                        </a>
                        <ul class="dropdown-menu dropdown-menu-end">
                            <li><a class="dropdown-item" href="#">LogOut</a></li>
                           
                        </ul>
                    </li>

                </ul>
               
            </div>
        </div>
    </nav>
</template>
<script>
export default {
    name: "AdminDash",
    data() {
        return {
            greetings: "Welcome to Admin dashboard"
        }
    }
}
</script>