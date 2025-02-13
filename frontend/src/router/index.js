import { createRouter, createWebHistory } from 'vue-router';
import Login from '@/views/Login.vue';
import Register from '@/views/Register.vue';
import Restaurants from '@/views/Restaurants.vue';
import Profile from '@/views/Profile.vue'; 
import FastFood from '@/views/FastFood.vue';
import ElegantDine from '@/views/ElegantDine.vue';






const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/restaurants', name: 'Restaurants', component: Restaurants },
  { path: '/profile', name: 'Profile', component: Profile },
  { path: '/restaurant-fastfood', name: 'FastFood', component: FastFood },
  { path: '/restaurant-elegant', name: 'ElegantDine', component: ElegantDine }



];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
