<template>
    <div class="text-center bg-success min-vh-100">
        <h1>Hello there it's index</h1>
        <router-link to="/login" class="text-warning"><i class="bi bi-box-arrow-in-left"></i> Login page</router-link><br/>
        <router-link to="/register" class="text-warning"><i class="bi bi-plus-circle"></i> Register page</router-link><br/>
        <router-link to="/dashboard" class="text-warning"><i class="bi bi-arrow-bar-down"></i> Axios example</router-link>

    </div>
</template>

<script>

    export default{
        name: "Index",
        data() {

        },
        methods:{

        }
    }
 
</script>