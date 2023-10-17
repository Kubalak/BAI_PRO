<template>
    <div>
    <ul class="nav nav-pills nav-fill nav-css">
      <li class="nav-item">
        <router-link to="/register" class="nav-link" active-class="active"><i></i>Register</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/login" class="nav-link" active-class="active"><i></i>Login</router-link>
      </li> 
    </ul>
    </div>

    <div class="d-flex justify-content-center min-vh-100 align-items-center text-center registerForm">  
    <form @submit.prevent="submitForm" class="container-mt5">
        <h1>User Login</h1>
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" v-model="user.username" id="username" class="form-control"/>
        </div>
        <div>
          <label for="password1">Password:</label>
          <input type="password" v-model="user.password" id="password1" class="form-control"/>
        </div>
        <div class="mt-3">
        <button type="submit" class="btn btn-outline-secondary btn-lg">
            Login
        </button>
          <div class="mt-3"> 
          </div>
        </div>
      </form>
    </div> 
    </template>
    
    <script>
    import api from '../getAxios.js';
    
    export default {
      name: "Register",
      
      data() {
        return {
          user: {
            username: '',
            password: '',
          },
          activeLink: true,
        };
      },
      methods: {
    
        submitForm() {
            this.login();
          }
        ,
    
        login() {
        const formDataLogin = new FormData();
        formDataLogin.append('username', this.user.username);
        formDataLogin.append('password', this.user.password);
        formDataLogin.append('csrfmiddlewaretoken', this.$cookies.get('csrftoken'))
    
        console.log('Form data:', formDataLogin);
        api.post('main/login/', formDataLogin, {
            headers:{
                'Content-Type': 'multipart/form-data',
                'X-CSRFToken': this.$cookies.get('csrftoken')
            }
        })
          .then(response => {
            console.log('User logged in successfully:', response.data);
            this.$router.push("/dashboard");
            this.user.username = '';
            this.user.password = '';
          })
          .catch(error => {
            console.error('Error logging in:', error.response.data);
          });
        }
    }
};
</script>
    