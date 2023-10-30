<template>
    <div>
    <VueSidebarMenuAkahon 
        :isUsedVueRouter=true
        :isMenuOpen=true
        menuTitle='Demo Panel'
        profileName="Patryk Jaworski"
        :menuItems="[{'link':'sqldemo', 'name':'Sql Injection', 'icon':''},
                     {'link':'xssdemo', 'name':'XSS', 'icon':''},
                     {'link':'corsdemo', 'name':'CORS', 'icon':''},
                     {'link':'csrfdemo', 'name':'CSRF', 'icon':''},
                     {'link':'../dashboard', 'name':'Index', 'icon':''}]"
        @button-exit-clicked="handleLogout"/>
    </div>
<div class="min-vh-100">
    <h1 class="text-center mt-3 pb-2 mb-2 border-bottom border-2">CSRF vulnerability demo</h1>
    <div class="d-flex flex-column justify-content-center text-center">
        <div class="mb-2"><button @click="show = !show" class="btn btn-primary">Click here to {{show ? 'hide': 'view'}} &#128293; photos!</button><br/></div>
        <img v-if="show" style="max-width: 10rem; max-height: 10rem;" class="position-relative start-50 translate-middle-x" :src="base+'/main/subscribe/'" alt="Cat photo">
    </div>
</div>


</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import api from '../getAxios.js';
import { baseURL } from '../getAxios.js';
export default {
        name: "Dashboard",
        components: {VueSidebarMenuAkahon},
        data() {
            return {
                show: false,
                base: baseURL,
            }
        },
        methods: {
            handleLogout() {
                const formDataLogout = new FormData();
                formDataLogout.append('csrfmiddlewaretoken', this.$cookies.get('csrftoken'))
                api.post('main/logout/', formDataLogout, {
                headers:{
                    'Content-Type': 'multipart/form-data',
                    'X-CSRFToken': this.$cookies.get('csrftoken')
                }
                }).then(response => {
                    console.log('Logged out successfully.', response.data);
                    this.$router.push("/login");
                })
                .catch(error => {
                console.error('Error logging out:', error);
                });
        }
      }
    }
</script>