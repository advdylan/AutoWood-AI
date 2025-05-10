<template>
    <button 
    @click="emit('click')"
    class="button fancy-split">
        <span class="button-content">
            {{ label }}
            <i :class="iconClass"></i>
        </span>
    </button>

</template>

<script setup>

const emit = defineEmits(['click']);

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
  -60deg,
    v-bind(colorB) 0%,
    v-bind(colorB) 20%,
    v-bind(colorA) 21%,
    v-bind(colorA) 100%
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