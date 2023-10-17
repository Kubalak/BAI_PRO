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
                     {'link':'dashboard/csrfdemo', 'name':'CSRF', 'icon':''}]"
        @button-exit-clicked="handleLogout"/>
    </div>
    <div class="bg-success min-vh-100 p-4 text-center">
        <h1 class="">This is dashboard</h1>
        <div v-for="user in usersList">
            {{ user }}
        </div>
        <router-link to="/" class="text-warning"> <i class="bi bi-house"></i> Go home</router-link>
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
                usersList: [],
            }
        },
        mounted() {
            api.get('main/test/')
            .then(response => {
                return response.data
            })
            .then(data => {
                this.usersList = data.data
                console.log(data)
            })
            .catch(error => {
                console.error(error)
            })

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