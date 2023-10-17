<script setup>
import Footer from './components/Footer.vue';
</script>

<template>
  <div>
    <div>
      <ul class="nav nav-pills nav-fill nav-css">
        <li class="nav-item">
          <router-link to="/" class="nav-link" active-class="active"><i></i>Home</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/register" class="nav-link" active-class="active"><i></i>Register</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/login" class="nav-link" active-class="active"><i></i>Login</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/dashboard" class="nav-link" active-class="active"><i></i>Dashboard</router-link>
        </li>
      </ul>
    </div>
    <router-view></router-view>
    <Footer></Footer>
  </div>
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
