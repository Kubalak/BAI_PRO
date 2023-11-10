<script setup>
import Footer from './components/Footer.vue';
import api from './getAxios';
import SideMenu from './components/SideMenu.vue';
import {ref, onMounted} from 'vue';

const renderSidebar = ref(true);
</script>
<template>
    <SideMenu v-if="renderSidebar"></SideMenu>
    <router-view></router-view>
    <Footer></Footer>
</template>

<script>

export default {
  name: "App",
  //TODO: Sprawdzić czy faktycznie działą

  setup() {
    const router = useRouter();
  
    onBeforeRouteUpdate((to, from, next) => {
      const shouldRenderSidebar = to.path !== '/login';
      renderSidebar.value = shouldRenderSidebar;
      console.log(router.currentRoute)
      next();
    }),

    onMounted(() => {
      renderSidebar.value = router.currentRoute.value.path !== '/login';
    });
  },

  mounted() {
    console.log()
    api.get('main/islogin/')
      .then(response => {
        return response.data
      })
      .then(data => {
        if (!data.authenticated && this.$route.path != '/login')
          this.$router.push('/login')
      })
      .catch(error => {
        console.error(error)
      })
  },
}
</script>
