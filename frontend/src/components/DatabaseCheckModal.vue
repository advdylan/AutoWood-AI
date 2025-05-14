<template>
  <div class="modal" :class="{ 'is-active': !isWokeUp }">
    <div class="modal-background"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Checking server...</p>
      </header>
      <section class="modal-card-body">
        Waiting for backend response...
      </section>
      <footer class="modal-card-foot">
        <p v-if="!isWokeUp" class="has-text-danger">Still trying to connect...</p>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const isWokeUp = ref(false);
let retryInterval = null;

async function checkDatabase() {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 2000);

  try {
    const response = await fetch('https://autowood.fly.dev/api/v1/production/ping', {
      signal: controller.signal
    });

    if (response.ok) {
      return true;
    } else {
      return false;
    }
  } catch (error) {
    return false;
  } finally {
    clearTimeout(timeout);
  }
}

async function tryToWakeUp() {
  const alive = await checkDatabase();
  if (alive) {
    isWokeUp.value = true;
    clearInterval(retryInterval);
  } else {
    isWokeUp.value = false;
  }
}

onMounted(async () => {
  await tryToWakeUp(); // 

  retryInterval = setInterval(async () => {
    if (!isWokeUp.value) {
      await tryToWakeUp();
    }
  }, 5000); // retry every 5s
});

onUnmounted(() => {
  clearInterval(retryInterval);
});
</script>

<style scoped>

</style>