<template>
  <div class="restaurant-profile">
    <h1 class="title">Fast Bites 🍔</h1>
    <img src="https://source.unsplash.com/600x400/?burger,fastfood" alt="Fast Food" class="restaurant-image" />
    <p class="description">
      Welcome to Fast Bites, where we serve the most delicious fast food in town! Enjoy crispy fries, juicy burgers, and refreshing drinks.
    </p>

    <h2>Gallery</h2>
    <div class="gallery">
      <img src="https://source.unsplash.com/200x150/?fries" alt="Fries" />
      <img src="https://source.unsplash.com/200x150/?burger" alt="Burger" />
      <img src="https://source.unsplash.com/200x150/?coke" alt="Drink" />
    </div>

    <h2>Menu Highlights</h2>
    <ul class="menu-list">
      <li>🍔 Classic Cheeseburger - $5.99</li>
      <li>🍟 Crispy French Fries - $2.99</li>
      <li>🥤 Refreshing Soda - $1.99</li>
    </ul>

    <h2>Customer Reviews</h2>
    <div class="review">
      <p><strong>John Doe:</strong> "Amazing burgers! The fries are crispy and tasty. Highly recommend!" ⭐⭐⭐⭐⭐</p>
    </div>
    <div class="review">
      <p><strong>Jane Smith:</strong> "Great fast food spot! Affordable and delicious." ⭐⭐⭐⭐</p>
    </div>

    <button @click="goBack">Back to Restaurants</button>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: "FastFood",
  setup() {
    const router = useRouter();

    const goBack = () => {
      router.push('/restaurants');
    };

    return { goBack };
  }
};
</script>

<style scoped>
.restaurant-profile {
  text-align: center;
  padding: 20px;
  background-color: #f8f9fa;
  min-height: 100vh;
}

.title {
  font-size: 36px;
  font-weight: bold;
  color: #ff5722;
  margin-bottom: 20px;
}

.restaurant-image {
  width: 100%;
  max-width: 600px;
  border-radius: 10px;
  margin-bottom: 20px;
}

.description {
  font-size: 18px;
  color: #555;
  margin-bottom: 20px;
}

h2 {
  color: #ff5722;
}

.gallery {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 20px;
}

.gallery img {
  border-radius: 8px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
}

.menu-list {
  list-style: none;
  padding: 0;
}

.menu-list li {
  font-size: 18px;
  margin: 5px 0;
}

.review {
  background: white;
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
  margin-bottom: 10px;
}

button {
  padding: 10px;
  background-color: #ff5722;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  margin-top: 20px;
}

button:hover {
  background-color: #e64a19;
}
</style>
