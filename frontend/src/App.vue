<script setup>

</script>

<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>

import api from './getAxios';
  export default {
    name: "App",
    mounted() {
      api.get('main/islogin/')
      .then(response => {
        return response.data
      })
      .then(data => {
        if(!data.authenticated)
        this.$router.push('/login')
      })
      .catch(error => {
        console.error(error)
      })
    }
  }
</script>
