<template>
  <div class="restaurants-page">
    <h1 class="title">Choose Your Restaurant</h1>
    <div class="restaurant-list">
      <div class="restaurant-card">
        <img :src="fastFoodImage" alt="Fast Food" class="restaurant-image" />
        <h3>Fast Bites</h3>
        <p>Delicious fast food with amazing flavors.</p>
        <button @click="goToFastFood">View Profile</button>
      </div>
      <div class="restaurant-card">
        <img :src="elegantDineImage" alt="Elegant Dining" class="restaurant-image" />
        <h3>Elegance Dine</h3>
        <p>Luxury dining experience with gourmet dishes.</p>
        <button @click="goToElegantDining">View Profile</button>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
const fastFoodImage = new URL('@/assets/fastfood.jpg', import.meta.url).href;
const elegantDineImage = new URL('@/assets/images.jpg', import.meta.url).href;

export default {
  name: "Restaurants",
  setup() {
    const router = useRouter();

    const goToFastFood = () => {
      router.push('/restaurant-fastfood'); // Redirige a la vista de comida rápida
    };

    const goToElegantDining = () => {
      router.push('/restaurant-elegant'); // Redirige a la vista de comida elegante
    };

    return { goToFastFood, goToElegantDining, fastFoodImage, elegantDineImage };
  }
};
</script>

<style scoped>
.restaurants-page {
  text-align: center;
  padding: 20px;
  background-color: #f4f4f4;
  min-height: 100vh;
}

.title {
  font-size: 36px;
  font-weight: bold;
  color: #42b983;
  margin-bottom: 20px;
}

.restaurant-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.restaurant-card {
  background: white;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 300px;
  text-align: center;
}

.restaurant-image {
  width: 100%;
  max-width: 280px;
  border-radius: 10px;
  margin-bottom: 10px;
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
