<template>


<div class="card">

  <section class="section">
  
    <div class="columns is-centered has-text-centered is-vcentered">

      <!-- First Column -->
      <div class="column">
        <div class="button is-rounded is-medium" :class="returnButtonState(npSteps[0].state)">{{ $t('client_data') }}</div>
      </div>
      <div class="column">
      <span class="icon is-medium">
      <i class="fa-solid fa-arrow-right-long"></i>
    </span></div>
      <!-- Line Between Buttons -->

      <!-- Second Column -->
      <div class="column">
        <div class="button is-rounded is-medium" :class="returnButtonState(npSteps[1].state)"
        >{{ $t('elements_list')}}</div>
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
        <div class="button is-rounded is-medium" :class="returnButtonState(npSteps[2].state)">{{$t('accessories')}}</div>
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
        <div class="button is-rounded is-medium" :class="returnButtonState(npSteps[3].state)">{{ $t('margins')  }}</div>
      </div>
      <!-- Line Between Buttons -->
      <div class="column">
      <span class="icon is-medium">
      <i class="fa-solid fa-arrow-right-long "></i>
    </span></div>


      <!-- Fifth Column -->
      <div class="column">
        <div class="button is-rounded is-medium" :class="returnButtonState(npSteps[4].state)">{{ $t('summary')  }}</div>
      <!-- Line Between Buttons -->
      </div>
    </div>

    
  
</section>

  
    
  

  <div class="card-content">
    <div class="content">
      <transition
        enter-active-class="animate__animated animate__slideInRight"
        leave-active-class="animate__animated animate__slideOutLeft">
   
    <component
      v-if="activeStep"
      :is="activeStep.component"
      :key="activeStep.name"
    ></component>
    </transition>
  </div>
  


  <footer class="card-footer">

    <button @click="handleBackButton(findActiveStep)" class="card-footer-item button is-medium" :disabled="findActiveStep === 0">
    <span class="icon is-medium">
      <i class="fa-solid fa-arrow-left "></i>
    </span>
    <span>{{ $t('back') }}</span>
  </button>

  <button class="card-footer-item button is-medium">Current Step</button>
  
  <button @click="handleNextButton(findActiveStep)" class="card-footer-item button is-medium" :disabled="findActiveStep === -1">

    <span class="text">{{ $t('next') }}</span>
    <span class="icon is-medium">
      <i class="fa-solid fa-arrow-right "></i>
    </span>
  </button>
  </footer>
</div>
</div>


</template>
  
<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { useSummaryStore } from '@/store/summary'
import {ref, computed, onUnmounted, watch, watchEffect, shallowRef, markRaw} from 'vue'
import { storeToRefs } from 'pinia'
import {validateFormData} from '@/validators/Validators.js'
import { useI18n } from 'vue-i18n';

import ElementsProgressTable from '@/components/NewProjectComponents/ElementsProgressTable.vue'
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



const npSteps = ref([
  { position: 0, name: 'ClientData', component: markRaw(ClientData), isValid: false, state: 'inProgress' },
  { position: 1, name: 'NewProjectData', component: markRaw(ElementsProgressTable), isValid: false, state: 'notYetDone' },
  { position: 2, name: 'AccessoryTable', component: markRaw(AccessoryTable), isValid: false, state: 'notYetDone' },
  { position: 3, name: 'WorktimeType', component: markRaw(WorktimeType), isValid: false, state: 'notYetDone' },
  { position: 4, name: 'Summary', component: markRaw(Summary), isValid: false, state: 'notYetDone' }
])

const findActiveStep = computed (() => {
  return npSteps.value.findIndex((component) => component.state === 'inProgress')
})

const activeStep = computed (() => {
  return npSteps.value.find(step => step.state === "inProgress")
})

function returnButtonState(state) {

  if (state === 'inProgress') {
    return 'is-primary'
  }
  else if (state === 'notYetDone') {
    return 'is-warning'
  }
  else if (state === 'done'){
    return 'is-success'
  }
  
}


function handleNextButton(index) {
 

  let currentStep = npSteps.value[index]
  let nextStep = npSteps.value[index+1]
  console.log(currentStep, nextStep)

  if (currentStep && nextStep) {
  //validation here
  currentStep.state = 'done'
  nextStep.state = 'inProgress'
  }
}

function handleBackButton(index) {

  let currentStep = npSteps.value[index]
  let previousStep = npSteps.value[index-1]

  if (currentStep && previousStep) {
    currentStep.state = 'notYetDone'
    previousStep.state = 'inProgress'
  }

}

const newElement = ref({
  element: {
    name: 'Przód',
    dimX: 2500,
    dimY: 250,
    dimZ: 25,
    wood_type: ''
  },
  quantity: 1
})
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

</style>
