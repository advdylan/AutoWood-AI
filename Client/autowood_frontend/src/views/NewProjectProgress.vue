<template>


<div class="card">

  <section class="section">
  
    <div class="columns is-centered has-text-centered is-vcentered">

      <!-- First Column -->
      <div class="column">
        <div class="button is-rounded is-medium" :class="
        {'is-warning': !firstStep},
        {'is-success': firstStep }
        ">{{ $t('client_data') }}</div>
      </div>
      <div class="column">
      <span class="icon is-medium">
      <i class="fa-solid fa-arrow-right-long"></i>
    </span></div>
      <!-- Line Between Buttons -->
      
      

      <!-- Second Column -->
      <div class="column">
        <div class="button is-rounded is-medium" :class=" 
        { 'is-warning': !secondStep},
        { 'is-success': secondStep}
        ">{{ $t('basic_info')}}</div>
      </div>
      <div class="column"><span class="icon is-medium">
      <i class="fa-solid fa-arrow-left-long "></i>
      </span>
      <span class="icon is-medium">
      <i class="fa-solid fa-arrow-right-long "></i>
    </span></div>
      <!-- Line Between Buttons -->
      

      <!-- Third Column -->
      <div class="column">
        <div class="button is-rounded is-medium" :class="
        { 'is-warning': !thirdStep},
        { 'is-success': thirdStep}
        ">{{$t('accessories')}}</div>
      </div>
      <!-- Line Between Buttons -->
      <div class="column"><span class="icon is-medium">
      <i class="fa-solid fa-arrow-left-long "></i>
      </span>
      <span class="icon is-medium">
      <i class="fa-solid fa-arrow-right-long "></i>
    </span></div>
      

      <!-- Fourth Column -->
      <div class="column">
        <div class="button is-rounded is-medium" :class="
        { 'is-warning': !fourthStep},
        { 'is-success': fourthStep}
        
        ">{{ $t('margins')  }}</div>
      </div>
      <!-- Line Between Buttons -->
      <div class="column">
      <span class="icon is-medium">
      <i class="fa-solid fa-arrow-right-long "></i>
    </span></div>


      <!-- Fifth Column -->
      <div class="column">
        <div class="button is-rounded is-medium" :class="
        { 'is-warning': !fifthStep},
        { 'is-success': fifthStep}
        ">{{ $t('summary')  }}</div>
      <!-- Line Between Buttons -->
      </div>
    </div>

    
  
</section>

  
    
  

  <div class="card-content">
    <div class="content">
     
        <ClientData :show-card-title="false"></ClientData>
     
      
        <NewProjectData></NewProjectData>      
     
      
        <AccessoryTable></AccessoryTable>
    
      

    </div>
  </div>
  <footer class="card-footer">

    <button @click="handleBackButton" class="card-footer-item button is-medium">
    <span class="icon is-medium">
      <i class="fa-solid fa-arrow-left "></i>
    </span>
    <span>{{ $t('back') }}</span>
  </button>

  <button class="card-footer-item button is-medium">Current Step</button>
  
  <button class="card-footer-item button is-medium">

    <span class="text">{{ $t('next') }}</span>
    <span class="icon is-medium">
      <i class="fa-solid fa-arrow-right "></i>
    </span>
  </button>
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
import NewProjectData from '@/components/NewProjectComponents/NewProjectData.vue'

import axios from 'axios'
import { toast } from 'bulma-toast'



const newProjectStore = useNewProjectStoreBeta()
const summaryStore = useSummaryStore()

const { addElement, loadData, $resetBoxes } = newProjectStore
const {summaryCosts, elementsMargin, accesoriesMargin, additionalMargin,summaryCostsWithMargin, elementsCost, accesoriesCost, worktimeCost} = storeToRefs(summaryStore)

loadData()

const {elements, wood, collection, paints, category, boxes, accesories, marginA, marginB, marginC, files, customer} = storeToRefs(newProjectStore)



const currentStep = ref(0)

const npSteps = ref([
{'position': 1, 'name': 'ClientData', component: ClientData, isValid: false, state: 'inProgress'},
{'position': 2, 'name': 'NewProjectData', component: NewProjectData, isValid: false, state: 'notYetDone'},
{'position': 3, 'name': 'AccessoryTable', component: AccessoryTable, isValid: false, state: 'notYetDone'},
{'position': 4, 'name': 'NewProjectData', component: NewProjectData, isValid: false, state: 'notYetDone'},
{'position': 5, 'name': 'WorktimeType', component: WorktimeType, isValid: false, state: 'notYetDone'},
{'position': 6, 'name': 'Summary', component: Summary, isValid: false, state: 'notYetDone'}

])



function handleBackButton() {
  console.log(npSteps.value[0])


  return 0
}

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
