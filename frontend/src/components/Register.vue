<template>
<div>
    <ul class="nav nav-pills nav-fill nav-css">
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeLink === true}" @click="changeFormType('register')"> Register </a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeLink === false}" @click="changeFormType('login')"> Login </a>
      </li>
    </ul>
</div>
    
<div class="d-flex justify-content-center align-items-center text-center vh-100 registerForm">  
<form @submit.prevent="submitForm" class="container-mt5">
    <h1>{{ formType === 'register' ? 'User Register' : 'User Login' }}</h1>
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
    <div v-if="formType === 'register'">
      <label for="password2">Confirm Password:</label>
      <input type="password" v-model="user.password2" id="password2" class="form-control"/>
    </div>
    <div class="mt-3">
    <button type="submit" class="btn btn-outline-secondary btn-lg">
        {{ formType === 'register' ? 'Register' : 'Login' }}
    </button> 
        
    </div>
  </form>
</div> 
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: {
        username: '',
        email: '',
        password1: '',
        password2: '',
      },
      formType: 'register',
      sucess: 'register',
      activeLink: true,
    };
  },
  methods: {

    submitForm() {
      if (this.formType === 'register') {
        console.log("REGISTER FORM!")
        this.register();
      } else {
        console.log("LOGIN FORM!")
        this.login();
        
      }
    },

    register() {
        const formDataRegister = new FormData();
        formDataRegister.append('username', this.user.username);
        formDataRegister.append('email', this.user.email);
        formDataRegister.append('password1', this.user.password1);
        formDataRegister.append('password2', this.user.password2);

        console.log('Form data:', formDataRegister);
      axios
        .post('http://127.0.0.1:8000/main/register/', formDataRegister)
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

    login() {
    const formDataLogin = new FormData();
    formDataLogin.append('username', this.user.username);
    formDataLogin.append('password', this.user.password1);

    console.log('Form data:', formDataLogin);
    axios.post('http://127.0.0.1:8000/main/login/', formDataLogin)
      .then(response => {
        console.log('User logged in successfully:', response.data);
        this.user.username = '';
        this.user.password1 = '';
      })
      .catch(error => {
        console.error('Error logging in:', error.response.data);
      });
  },
  
  changeFormType(type) {
      this.formType = type;
      this.activeLink = this.formType === 'register'
    },

  },
};
</script>

<style scoped>
.registerForm{
    background-color: #121212;
    color:#42b883;
    font-size: large;
    font-family:monospace
}

.nav-css{
    background-color: #42b883;
    font-size: larger;
    font-family: monospace;
    font-weight: 700;
}

.nav-pills .active {
  background-color: #06c971;
  color: black;
}
</style>