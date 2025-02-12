import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/views/Login.vue';
import Register from '@/views/Register.vue';
import Restaurants from '@/views/Restaurants.vue';
import Profile from '@/views/Profile.vue'; // Importamos la nueva vista




const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/restaurants', name: 'Restaurants', component: Restaurants },
  { path: '/profile', name: 'Profile', component: Profile } // Agregamos la ruta de perfil


];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
