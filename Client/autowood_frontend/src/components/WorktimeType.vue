<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-full" v-for="box in boxes" :key="box.text">
        <label class="checkbox">
          <input type="checkbox" v-model="box.checked" />
          {{ box.text }}
        </label>
        <div class="columns">
        <div class="column is-one-third">
        <div class="block">

          <div class="control">
          <label v-if="box.checked">{{ $t("worktime")}}</label>
        <input  class="input" type="number" v-if="box.checked" v-model="box.hours" :placeholder="$t('hours')" />
          </div>
        <label v-if="box.checked">{{ $t("workers")}}</label>
        <input class="input" type="number" v-if="box.checked" v-model="box.workers" :placeholder="$t('workers')">
        </div>
      </div>
      <div class="column is-one-third">
        <label>{{ $t("section_cost")}} {{ box.text}}</label>
        <input  class="input" type="text" :placeholder="$t('section_cost')" v-model="box.value" disabled />
      </div>
      </div>
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



