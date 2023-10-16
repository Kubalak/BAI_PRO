<template>
    <div>
        This is dashboard ->
        <router-link to="/">Go home</router-link>
        <div v-for="user in usersList">
            {{ user }}
        </div>
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