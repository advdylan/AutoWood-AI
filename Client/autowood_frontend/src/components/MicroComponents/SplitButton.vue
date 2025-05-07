<template>
    <button class="button fancy-split">
        <span class="button-content">
            {{ label }}
            <i class="fa-solid fa-trash"></i>
        </span>
    </button>

</template>

<script setup>



defineProps({
    label: String,
    iconClass: String,
    colorA: {type: String, default: "#608a8a"},
    colorB: {type:String, default: "#757575"}
})

</script>

<style  scoped>

.button.fancy-split {
  position: relative;
  border: none;
  border-radius: 8px;
  padding: 0 1rem;
  color: white;
  font-weight: bold;
  font-size: 1rem;
  cursor: pointer;
  background: linear-gradient(
    to top left,
    v-bind(colorA) 0%,       /* green (Bulma 'success') */
    v-bind(colorB) 65.5%,
    v-bind(colorB) 25.5%,    /* blue (Bulma 'info') */
    v-bind(colorB)
  );
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
} 

.button-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

</style>