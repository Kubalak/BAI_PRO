<template>
    <div class="bg-success min-vh-100 p-4 text-center">
        <h1 class="">This is dashboard</h1>
        <div v-for="user in usersList">
            {{ user }}
        </div>
        <router-link to="/" class="text-warning"> <i class="bi bi-house"></i> Go home</router-link>
    </div>
</template>

<script>
    import api from '../getAxios.js';
    export default {
        name: "Dashboard",
        data() {
            return {
                usersList: [],
            }
        },
        mounted() {
            api.get('main/test/')
            .then(response => {
                return response.data
            })
            .then(data => {
                this.usersList = data.data
                console.log(data)
            })
            .catch(error => {
                console.error(error)
            })

        }
    }
</script>