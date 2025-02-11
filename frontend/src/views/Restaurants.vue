<template>
  <div class="restaurants-page">
    <h1 class="title">Choose Your Restaurant</h1>
    <div class="restaurant-list">
      <div v-for="restaurant in restaurants" :key="restaurant.id" class="restaurant-card">
        <h3>{{ restaurant.name }}</h3>
        <p>{{ restaurant.description }}</p>
        <button @click="selectRestaurant(restaurant.id)">View Menu</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: "Restaurants",
  setup() {
    const router = useRouter();
    
    const restaurants = ref([
      { id: 1, name: "La Casa del Chef", description: "Fine dining experience with gourmet dishes." },
      { id: 2, name: "Pizzeria Napoli", description: "Authentic Italian pizzas made with fresh ingredients." },
      { id: 3, name: "Sushi Express", description: "Delicious sushi and Japanese cuisine at great prices." }
    ]);

    const selectRestaurant = (id) => {
      alert(`You selected restaurant ID: ${id}`);
      // Aquí podrías redirigir a la página del menú del restaurante
    };

    return { restaurants, selectRestaurant };
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
