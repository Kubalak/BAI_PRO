<script setup>
import Footer from './components/Footer.vue';
</script>
<template>
    <router-view></router-view>
    <Footer></Footer>
</template>

<script>

import api from './getAxios';
export default {
  name: "App",

  //TODO: Sprawdzić czy faktycznie działą
  mounted() {
    console.log()
    api.get('main/islogin/')
      .then(response => {
        return response.data
      })
      .then(data => {
        if (!data.authenticated && this.$route.path != '/login')
          this.$router.push('/login')
      })
      .catch(error => {
        console.error(error)
      })
  }
}
</script>
