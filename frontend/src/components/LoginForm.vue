<template>
  <form class="login-form" @submit.prevent="redirectToRestaurants">
    <input type="email" placeholder="Email" required />
    <input type="password" placeholder="Password" required />
    <button type="submit">Ingresar</button>
  </form>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  setup() {
    const router = useRouter();

    const redirectToRestaurants = () => {
      router.push('/restaurants'); // Redirige a la página de restaurantes sin autenticación
    };

    return { redirectToRestaurants };
  }
};
</script>

<style scoped>
.login-form {
  display: flex;
  flex-direction: column;
  width: 300px;
  padding: 20px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
input {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
button {
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}
button:hover {
  background-color: #379b72;
}
</style>
