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
import { onMounted, ref, onUnmounted } from 'vue';

const propsList =  defineProps({
    databaseModal: Boolean,
    default: false
})

const isWokeUp = ref(false);
let retryInterval;

async function checkDatabase() {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 30000);

    try {
        const response = await fetch('https://autowood.fly.dev/api/v1/production/ping', { signal: controller.signal });
        console.log(response)
        if (response.ok) {
            console.log(response.data)
            console.log("Got DJANGO response")
            clearInterval(retryInterval);

            return true;
        }
        return false;
    } catch (error) {
        return false;
    } finally {
        clearTimeout(timeout);
    }
}

onMounted(async() => {
    retryInterval = setInterval(async () => {
        const alive = await checkDatabase();
        if (alive) {
            clearInterval(retryInterval);
            isWokeUp.value = false; 
        } else {
            isWokeUp.value = true; 
        }
    }, 5000); 
});


onUnmounted(() => {
    clearInterval(retryInterval);
});

</script>

<style scoped>

</style>