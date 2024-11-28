<template>


<div class="card">

  <section class="section">
  
    <div class="columns is-centered has-text-centered is-vcentered">
      <!-- First Column -->
      <div class="column">
        <div class="button is-rounded" :class=" {'is-success': firstStep }">1</div>
      </div>
      <!-- Line Between Buttons -->
      ------

      <!-- Second Column -->
      <div class="column">
        <div class="button is-rounded" :class=" { 'is-success': secondStep}">2</div>
      </div>
      <!-- Line Between Buttons -->
      ------

      <!-- Third Column -->
      <div class="column">
        <div class="button is-rounded" :class=" { 'is-success': thirdStep}">3</div>
      </div>
      <!-- Line Between Buttons -->
      ------

      <!-- Fourth Column -->
      <div class="column">
        <div class="button is-rounded" :class=" { 'is-success': fourthStep}">4</div>
      </div>
    </div>
  
</section>

  
    
  

  <div class="card-content">
    <div class="content">
      <ClientData :show-card-title="false"></ClientData>

    </div>
  </div>
  <footer class="card-footer">
    <div class="sphere"></div>
    <a href="#" class="card-footer-item">Wstecz</a>
    <a href="#" class="card-footer-item">Dalej</a>
  </footer>
</div>





 
</template>
  
<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { useSummaryStore } from '@/store/summary'
import {ref, computed, onUnmounted, watch, watchEffect} from 'vue'
import { storeToRefs } from 'pinia'
import {validateFormData} from '@/validators/Validators.js'
import { useI18n } from 'vue-i18n';

import ElementsTable from '@/components/ElementsTable'
import WorktimeType from '@/components/WorktimeType'
import AccessoryTable from '@/components/AccessoryTable.vue'
import Summary from '@/components/Summary.vue'
import ClientData from '@/components/NewProjectComponents/ClientData.vue'


import axios from 'axios'
import { toast } from 'bulma-toast'

const firstStep = ref(false)
const secondStep = ref(false)
const thirdStep = ref(false)
const fourthStep = ref(false)







</script>

<style>

.modal{
  --bulma-modal-content-width: 70%;
}

.line {
  width: 100px; /* Adjust the length of the line */
  height: 2px; /* Thickness of the line */
  background-color: #ccc; /* Line color */
  margin: auto; /* Center it */
}



</style>
