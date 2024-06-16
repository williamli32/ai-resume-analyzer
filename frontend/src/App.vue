<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>

    <div class="wrapper">
      <form @submit.prevent="handleSubmit">
      <div>
        <textarea v-model="textBox" id="textInput" placeholder="Enter a job description:" rows="40"></textarea>
      </div>
      <div>
        <label for="fileInput">Upload file:</label>
        <input type="file" id="fileInput" @change="handleFileUpload" required />
      </div>
      <button type="submit">Submit</button>
    </form>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

label {
  margin-bottom: 0.5rem;
}

input {
  padding: 0.5rem;
  font-size: 1rem;
}

#textInput {
  width: 140%;
  font-weight: normal;
}

button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  background-color: hsla(160, 100%, 37%, 1);
  color: white;
  border: none;
  cursor: pointer;
  left: 200px;
}

button:hover {
  background-color: hsla(160, 100%, 37%, 0.2);
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
