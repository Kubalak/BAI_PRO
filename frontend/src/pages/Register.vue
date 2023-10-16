<template>
<!--div> /* Może przyda się w przyszłości dlatego zostawione */
    <ul class="nav nav-pills nav-fill nav-css">
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeLink === true}" @click="changeFormType('register')"> Register </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeLink === false}" @click="changeFormType('login')"> Login </a>
      </li>
    </ul>
</div-->
    
<div class="d-flex justify-content-center align-items-center text-center vh-100 registerForm">  
<form @submit.prevent="submitForm" class="container-mt5">
    <h1>User Register</h1>
    <div class="form-group">
      <label for="username">Username:</label>
      <input type="text" v-model="user.username" id="username" class="form-control"/>
    </div>
    <div v-if="formType === 'register'">
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
