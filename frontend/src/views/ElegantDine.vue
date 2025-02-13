<template>
    <div class="restaurant-profile">
      <h1 class="title">Elegance Dine 🍷</h1>
      <img src="https://source.unsplash.com/600x400/?fine-dining,restaurant" alt="Elegant Dining" class="restaurant-image" />
      <p class="description">
        Indulge in a luxurious dining experience at Elegance Dine. Fine wines, gourmet dishes, and an ambiance that exudes sophistication.
      </p>
  
      <h2>Gallery</h2>
      <div class="gallery">
        <img src="https://source.unsplash.com/200x150/?wine" alt="Wine" />
        <img src="https://source.unsplash.com/200x150/?steak" alt="Steak" />
        <img src="https://source.unsplash.com/200x150/?restaurant" alt="Interior" />
      </div>
  
      <h2>Signature Dishes</h2>
      <ul class="menu-list">
        <li>🥩 Grilled Wagyu Steak - $49.99</li>
        <li>🍷 French Red Wine - $29.99</li>
        <li>🦞 Lobster Thermidor - $39.99</li>
      </ul>
  
      <h2>Customer Reviews</h2>
      <div class="review">
        <p><strong>Michael Brown:</strong> "Absolutely stunning atmosphere and the steak was perfection!" ⭐⭐⭐⭐⭐</p>
      </div>
      <div class="review">
        <p><strong>Emily Davis:</strong> "A wonderful place for a romantic dinner. Loved the wine selection!" ⭐⭐⭐⭐⭐</p>
      </div>
  
      <button @click="goBack">Back to Restaurants</button>
    </div>
  </template>
  
  <script>
  import { useRouter } from 'vue-router';
  
  export default {
    name: "ElegantDine",
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
    background-color: #faf3e0;
    min-height: 100vh;
  }
  
  .title {
    font-size: 36px;
    font-weight: bold;
    color: #8b0000;
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
    color: #333;
    margin-bottom: 20px;
  }
  
  h2 {
    color: #8b0000;
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
    background-color: #8b0000;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    margin-top: 20px;
  }
  
  button:hover {
    background-color: #6b0000;
  }
  </style>
  