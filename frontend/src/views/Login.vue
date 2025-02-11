<template>
  <div class="login-page">
    <h1 class="title">ReserveNow</h1>
    <div class="login-container">
      <h2>Login</h2>
      <LoginForm />
      <button class="register-btn" @click="goToRegister">Register</button>
    </div>
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue';
import { useRouter } from 'vue-router';

export default {
  name: "Login",
  components: { LoginForm },
  setup() {
    const router = useRouter();
    
    const goToRegister = () => {
      router.push('/register'); // Redirige a la URL de registro
    };

    return { goToRegister };
  }
};
</script>

<style scoped>
.login-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f4f4f4;
}

.title {
  font-size: 48px;
  font-weight: bold;
  color: #42b983;
  margin-bottom: 20px;
}

.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 320px;
}

.register-btn {
  margin-top: 10px;
  padding: 10px;
  width: 100%;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.register-btn:hover {
  background-color: #0056b3;
}
</style>
