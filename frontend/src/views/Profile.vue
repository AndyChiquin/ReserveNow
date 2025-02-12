<template>
  <div class="profile-page">
    <div class="profile-card">
      <img :src="user.avatar" alt="Profile Picture" class="profile-avatar" />
      <h2>{{ user.name }}</h2>
      <p>{{ user.email }}</p>
      <button @click="editProfile">Edit Profile</button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: "Profile",
  setup() {
    const user = ref({
      name: "John Doe",
      email: "johndoe@example.com",
      avatar: "https://i.pravatar.cc/150?img=3" // Imagen de avatar random
    });

    const editProfile = () => {
      alert("Edit Profile clicked! (Feature coming soon)");
    };

    return { user, editProfile };
  }
};
</script>

<style scoped>
.profile-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f4f4f4;
}

.profile-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 300px;
}

.profile-avatar {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 15px;
}

button {
  margin-top: 10px;
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
</style>
