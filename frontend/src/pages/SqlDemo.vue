<template>
    <div>
    <VueSidebarMenuAkahon 
        isUsedVueRouter=true
        isMenuOpen=true
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
    <h1 class="text-center mt-3 mb-2 pb-2 border-bottom border-2">SQL Injection demo</h1>
</div>


</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import api from '../getAxios.js';
export default {
        name: "Dashboard",
        components: {VueSidebarMenuAkahon},
        data() {
            return {
                usersList: [],
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