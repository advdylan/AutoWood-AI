<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-full" v-for="box in boxes" :key="box.text">
        <label class="checkbox">
          <input type="checkbox" v-model="box.checked" />
          {{ box.text }}
        </label>
        <input class="input" type="tel" v-if="box.checked" v-model="box.input" />
        <div class="box" v-if="box.checked">{{ box.value }}</div>
      </div>
    </div>
  </div>

  <div class="column" v-for="worktimetyp in worktimetype"> {{ worktimetyp.cost }}  </div>
</template>

<script>

</script>


<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import {ref} from 'vue'
import { storeToRefs } from 'pinia'

const store = useNewProjectStoreBeta()

const {worktimetype} = storeToRefs(store)

const boxes = ref([
      { text: 'Produkcja', checked: false, input: '', value: worktimetype.cost },
      { text: 'Czyszczenie', checked: false, input: '', value: worktimetype.cost },
      { text: 'Lakiernia', checked: false, input: '', value: worktimetype.cost },
      { text: 'Pakowanie', checked: false, input: '', value: worktimetype.cost }
    ])



</script>



