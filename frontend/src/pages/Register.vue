<template>
<div>
    <ul class="nav nav-pills nav-fill nav-css">
      <li class="nav-item">
        <router-link to="/" class="nav-link" active-class="active">Home</router-link> 
      </li>
      <li class="nav-item">
        <router-link to="/register" class="nav-link" active-class="active">Register</router-link>
      </li>
      <li class="nav-item">
        <router-link to="/login" class="nav-link" active-class="active">Login</router-link>
      </li>
    </ul>
</div>
    
<div class="d-flex justify-content-center align-items-center text-center min-vh-100 registerForm">  
<form @submit.prevent="submitForm" class="container-mt5">
    <h1>User Register</h1>
    <div class="form-group">
      <label for="username">Username:</label>
      <input type="text" v-model="user.username" id="username" class="form-control"/>
    </div>
    <div>
      <label for="email">Email:</label>
      <input type="email" v-model="user.email" id="email" class="form-control"/>
    </div>
    <div>
      <label for="password1">Password:</label>
      <input type="password" v-model="user.password1" id="password1" class="form-control"/>
    </div>
    <div>
      <label for="password2">Confirm Password:</label>
      <input type="password" v-model="user.password2" id="password2" class="form-control"/>
    </div>
    <div class="mt-3">
    <button type="submit" class="btn btn-outline-secondary btn-lg">
        Register
    </button>
    <div class="pt-3">
      
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
        email: '',
        password1: '',
        password2: '',
      },
    };
  },
  methods: {

    submitForm() {
        this.register();
    },

    register() {
        const formDataRegister = new FormData();
        formDataRegister.append('username', this.user.username);
        formDataRegister.append('email', this.user.email);
        formDataRegister.append('password1', this.user.password1);
        formDataRegister.append('password2', this.user.password2);
        formDataRegister.append('csrfmiddlewaretoken', this.$cookies.get('csrftoken'))

        console.log('Form data:', formDataRegister);
      api.post('main/register/', formDataRegister, {
            headers:{
                'Content-Type': 'multipart/form-data',
                'X-CSRFToken': this.$cookies.get('csrftoken')
            }
        })
        .then(response => {
          console.log('User registered successfully:', response.data);
          //Wyczyszczenie formularza
          this.user.username = '';
          this.user.email = '';
          this.user.password1 = '';
          this.user.password2 = '';
        })
        .catch(error => {
        if (error.response) {
        console.error('Error registering user:', error.response.data);
      } else if (error.request) {
        console.error('No response received:', error.request);
      } else {
        console.error('Error setting up the request:', error.message);
      }
    });
    },

  },
};
</script>
