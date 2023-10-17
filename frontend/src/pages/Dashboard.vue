<template>
    <div>
    <VueSidebarMenuAkahon 
        isUsedVueRouter=true
        isMenuOpen=true
        menuTitle='Demo Panel'
        profileName="Patryk Jaworski"
        :menuItems="[{'link':'dashboard/sqldemo', 'name':'Sql Injection', 'icon':''},
                     {'link':'dashboard/xssdemo', 'name':'XSS', 'icon':''},
                     {'link':'dashboard/corsdemo', 'name':'CORS', 'icon':''},
                     {'link':'dashboard/csrfdemo', 'name':'CSRF', 'icon':''},
                     {'link':'dashboard', 'name':'Index', 'icon':''}]"
        @button-exit-clicked="handleLogout"/>
    </div>
    <div class="bg-success min-vh-100 text-center">
        <h1 class="text-center pt-3 mb-2 pb-2 border-bottom border-2">This is dashboard</h1>
        <router-link to="/login" class="text-warning"><i class="bi bi-box-arrow-in-left"></i> Login page</router-link><br/>
        <router-link to="/register" class="text-warning"><i class="bi bi-plus-circle"></i> Register page</router-link><br/>
        <button @click="genComments" class="btn btn-primary mt-2">Generate comments</button>
    </div>
</template>

<script>
    import api from '../getAxios.js';
    import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
    export default {
        name: "Dashboard",
        components: {VueSidebarMenuAkahon},
        data() {
            return {
                
            }
        },
        mounted() {
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
        },
        genComments() {
                api.post('main/comments/gen/')
                .then(response => {
                    return response.data
                })
                .then(data => {
                    alert(data.message);
                })
                .catch(error => {
                    console.warn(error);
                })
            }
      }
    }
</script>