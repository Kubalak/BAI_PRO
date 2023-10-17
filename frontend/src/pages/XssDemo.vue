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
                     {'link':'csrfdemo', 'name':'CSRF', 'icon':''}]"
        @button-exit-clicked="handleLogout"/>
    </div>
<div>
    Test XSS!
</div>


</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
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