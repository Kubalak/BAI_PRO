<template>
    <div class="text-center">
        <h1>Hello there it's index</h1>
        <router-link to="/login">Login page</router-link><br/>
        <router-link to="/register">Register page</router-link><br/>
        <router-link to="/dashboard">Axios example</router-link>

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