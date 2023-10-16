<template>
        
    <div class="d-flex justify-content-center align-items-center text-center vh-100 registerForm">  
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
            <router-link to="/" class="icon-link text-success"><i class="bi bi-arrow-left"></i> Home</router-link> 
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
    