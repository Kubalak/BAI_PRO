import Register from './pages/Register.vue';
import Index from './pages/Index.vue';
import Login from './pages/Login.vue';
import Dashboard from './pages/Dashboard.vue';


const routes = [
    {
        path: "/",
        name: 'index',
        component: Index
    },
    {
        path: "/login",
        name: "login",
        component: Login
    },
    {
        path: "/register",
        name: "register",
        component: Register
    },
    {
        path: "/dashboard",
        name: "dashboard",
        component: Dashboard
    }
]


export default routes;