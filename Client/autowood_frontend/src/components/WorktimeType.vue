<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-full" v-for="box in boxes" :key="box.text">
        <label class="checkbox">
          <input type="checkbox" v-model="box.checked" />
          {{ box.text }}
        </label>
        <input  class="input is-small" type="text" v-if="box.checked" v-model="box.hours" />
        <div class="box" v-if="box.checked"> Stawka godzinowa:{{ box.value }}</div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'WorktimeType'
}
</script>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'

const store = useNewProjectStoreBeta()
const {boxes} = storeToRefs(store)



</script>



