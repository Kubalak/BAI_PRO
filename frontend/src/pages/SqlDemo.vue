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
    <input v-model="names" class="shadow rounded position-relative start-50 translate-middle-x mt-3 mb-3 p-1" placeholder="Search for product name"/>
    <input v-model="safe" class="position-relative" id="checkbox" type="checkbox"/>
    <label for="checkbox">&nbsp;Safe search</label>
    <br/>
    <label class="position-relative start-50 translate-middle-x mt-2 mb-3">Current SQL string: <i>{{ sql }}</i></label>
    <div>
        <Product v-for="product in products" :name="product.name" :price="product.price" :thumbnail="product.thumbnail"/>
    </div>

</div>


</template>

<script>
import VueSidebarMenuAkahon from "vue-sidebar-menu-akahon";
import Product from "../components/Product.vue";
import api from '../getAxios.js';
export default {
        name: "Dashboard",
        components: {VueSidebarMenuAkahon, Product},
        data() {
            return {
                products: [],
                names: '',
                safe: false,
                sql: ''
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
        },
        getProducts() {
            api.get('main/sqldemo/', {
                params: {
                    name: this.names,
                    safe: this.safe
                }
            })
            .then(response => {
                return response.data
            })
            .then(data => {
                this.products = data.products
                this.sql = data.query
            })
            .catch(error => {
                console.warn(error)
            })
        }

  },
  mounted() {
    this.getProducts()
  },
  watch: {
    names(val) {
        this.getProducts()
    },
    safe(val){
        this.getProducts()
    }

  }
}
</script>