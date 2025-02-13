<template>
  <form class="login-form" @submit.prevent="loginUser">
    <input v-model="email" type="email" placeholder="Email" required />
    <input v-model="password" type="password" placeholder="Password" required />
    <button type="submit">Ingresar</button>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </form>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { API_AUTH_URL } from "../config.js"; 

export default {
  setup() {
    const email = ref("");  // Captura el correo del usuario
    const password = ref("");  // Captura la contraseña
    const errorMessage = ref("");  // Mensaje de error
    const router = useRouter();

    // Función para iniciar sesión
    const loginUser = async () => {
      try {
        const response = await fetch(`${API_AUTH_URL}/login`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email: email.value,
            password: password.value
          }),
        });

        const data = await response.json();

        if (response.ok) {
          localStorage.setItem("authToken", data.token); // Guardar el token en localStorage
          alert("Login exitoso");
          router.push("/restaurants"); // Redirigir a la página de restaurantes
        } else {
          errorMessage.value = data.message || "Credenciales incorrectas";
        }
      } catch (error) {
        errorMessage.value = "No se pudo conectar con el servidor.";
        console.error("Error en el login:", error);
      }
    };

    return { email, password, errorMessage, loginUser };
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
.error {
  color: red;
  margin-top: 10px;
}
</style>
