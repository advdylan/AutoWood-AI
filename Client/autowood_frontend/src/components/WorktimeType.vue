<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-full" v-for="box in boxes" :key="box.text">
        <label class="checkbox">
          <input type="checkbox" v-model="box.checked" />
          {{ box.text }}
        </label>
        <input class="input" type="tel" v-if="box.checked" v-model="box.input" />
        <div class="box" v-if="box.checked"> Stawka godzinowa:{{ box.value }}</div>
      </div>
    </div>
  </div>

</template>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import {ref, reactive, computed} from 'vue'
import { storeToRefs } from 'pinia'

const store = useNewProjectStoreBeta()
const {worktimetype} = storeToRefs(store)

const boxes = computed(() => {
  return worktimetype.value.map(item => ({
    text: item.name,
    value: item.cost,
    checked: false,
    input: ''
  }))
})
</script>



