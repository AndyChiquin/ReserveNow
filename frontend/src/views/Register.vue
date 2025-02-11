<template>
  <div class="register-page">
    <h1 class="title">Create an Account</h1>
    <div class="register-container">
      <h2>Register</h2>
      <form @submit.prevent="handleRegister">
        <input type="text" v-model="name" placeholder="Full Name" required />
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Register</button>
      </form>
      <button class="login-btn" @click="goToLogin">Back to Login</button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: "Register",
  setup() {
    const router = useRouter();
    const name = ref('');
    const email = ref('');
    const password = ref('');

    const handleRegister = () => {
      alert(`User Registered: ${name.value}, ${email.value}`);
      router.push('/login'); // Redirigir al login después del registro
    };

    const goToLogin = () => {
      router.push('/login');
    };

    return { name, email, password, handleRegister, goToLogin };
  }
};
</script>

<style scoped>
.register-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f4f4f4;
}

.title {
  font-size: 36px;
  font-weight: bold;
  color: #42b983;
  margin-bottom: 20px;
}

.register-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 50px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 320px;
}

input {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  width: 100%;
}

button {
  padding: 10px;
  width: 100%;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

button:hover {
  background-color: #379b72;
}

.login-btn {
  margin-top: 10px;
  background-color: #007bff;
}

.login-btn:hover {
  background-color: #0056b3;
}
</style>
