<template>

<div class="modal">
  <div class="modal-background"></div>
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">Modal title</p>
      <button class="delete" aria-label="close"></button>
    </header>
    <section class="modal-card-body">
      {{ isWokeUp }}
    </section>
    <footer class="modal-card-foot">
      <div class="buttons">
        <button class="button is-success">Save changes</button>
        <button class="button">Cancel</button>
      </div>
    </footer>
  </div>
</div>

</template>

<script setup>
import axios from 'axios';
import { onMounted } from 'vue';

const isWokeUp = ref(false)

async function checkDatabase() {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 1000);

    try {
        await fetch('api/v1/production/ping', { signal: controller.signal});
        return true;
    } catch (error) {
        return false;
    } finally {
        clearTimeout(timeout)
    }
}

onMounted(async() => {
    const alive = await checkDatabase();
    if (!alive) {
        isWokeUp.value = true;

    }
})

</script>

<style scoped>

</style>