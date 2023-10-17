<template>
    <div>
    <VueSidebarMenuAkahon 
        isUsedVueRouter=true
        isMenuOpen=false
        menuTitle='Demo Panel'
        profileName="Patryk Jaworski"
        :menuItems="[{'link':'../dashboard/sqldemo', 'name':'Sql Injection', 'icon':''},
                     {'link':'../dashboard/xssdemo', 'name':'XSS', 'icon':''},
                     {'link':'../dashboard/corsdemo', 'name':'CORS', 'icon':''},
                     {'link':'../dashboard/csrfdemo', 'name':'CSRF', 'icon':''}]"/>
    </div>
<div>
    Test SQL!
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
        }
    }
</script>