<template>
   <b-steps
            v-model="activeStep"
            :animated="isAnimated"
            :rounded="isRounded"
            :has-navigation="hasNavigation"
            :icon-prev="prevIcon"
            :icon-next="nextIcon"
            :label-position="labelPosition"
            :mobile-mode="mobileMode">
            <b-step-item step="1" label="Account" :clickable="isStepsClickable">
                <h1 class="title has-text-centered">Account</h1>
                Lorem ipsum dolor sit amet.
            </b-step-item>

            <b-step-item step="2" label="Profile" :clickable="isStepsClickable" :type="{'is-success': isProfileSuccess}">
                <h1 class="title has-text-centered">Profile</h1>
                Lorem ipsum dolor sit amet.
            </b-step-item>

            <b-step-item step="3" :visible="showSocial" label="Social" :clickable="isStepsClickable">
                <h1 class="title has-text-centered">Social</h1>
                Lorem ipsum dolor sit amet.
            </b-step-item>

            <b-step-item :step="showSocial ? '4' : '3'" label="Finish" :clickable="isStepsClickable" disabled>
                <h1 class="title has-text-centered">Finish</h1>
                Lorem ipsum dolor sit amet.
            </b-step-item>

            <template
                v-if="customNavigation"
                #navigation="{previous, next}">
                <b-button
                    outlined
                    type="is-danger"
                    icon-pack="fas"
                    icon-left="backward"
                    :disabled="previous.disabled"
                    @click.prevent="previous.action">
                    Previous
                </b-button>
                <b-button
                    outlined
                    type="is-success"
                    icon-pack="fas"
                    icon-right="forward"
                    :disabled="next.disabled"
                    @click.prevent="next.action">
                    Next
                </b-button>
            </template>
        </b-steps>



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


// b-steps variables
let activeStep = ref(0);
let showSocial = ref(false);
let isAnimated = ref(true);
let isRounded = ref(true);
let isStepsClickable = ref(true);
let hasNavigation = ref(true);
let customNavigation = ref(false);
let isProfileSuccess = ref(true);
let prevIcon = ref('chevron-left');
let nextIcon = ref('chevron-right');
let labelPosition = ref('bottom');
let mobileMode = ref('minimalist');


function onStepUpdate(newStep) {
  // Add logic to handle step updates
  activeStep.value = newStep; // This avoids direct recursion
}
// end of  b-steps variables 

  
  const showElementModal = ref(false)
  const showElementModalTable = ref(false)
  const showAccModal = ref(false)
  const isCollapsedacc = ref(false)
  const isCollapsedpaints = ref(false)
  const isCollapsed = ref(false)
  const isCollapsedelements = ref(false)
  
  const project = ref({})
  const errors = ref([])
  const { t } = useI18n();
  
  
  const projectName = ref()
  const selectedWood = ref()
  const selectedCategory = ref()
  const selectedCollection = ref()
  const selectedPaint = ref()
  const projectpostData = ref()
  const inputClass = ref('input')
  
  
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
  const newProjectStore = useNewProjectStoreBeta()
  const summaryStore = useSummaryStore()
  
  const { addElement, loadData, $resetBoxes } = newProjectStore
  const {summaryCosts, elementsMargin, accesoriesMargin, additionalMargin,summaryCostsWithMargin, elementsCost, accesoriesCost, worktimeCost} = storeToRefs(summaryStore)
  
  loadData()
  
  const {elements, wood, collection, paints, category, boxes, accesories, marginA, marginB, marginC, files, customer} = storeToRefs(newProjectStore)
  
  
  const submitForm = () => {
  
   
  
    if( elements.value.length > 0) {
      for ( let accName of elements.value){
        if(newElement.value.element.name === accName.element.name) {
          errors.value.push('Projekt zawiera element o takiej nazwie. Zmień nazwę')
        }
      }
    } 
  
  
    if (newElement.value.element.dimX <= 0) {
      errors.value.push('Podaj długość większą niż 0')
    }
    if (typeof newElement?.value?.element?.name !== 'string' || newElement.value.element.name.trim() === '') {
      errors.value.push('Podaj właściwą nazwę')
    }
    if (newElement.value.element.dimY <= 0) {
      errors.value.push('Podaj wysokość większą niż 0')
    }
    if (newElement.value.element.dimZ <= 0) {
      errors.value.push('Podaj grubość większą niż 0')
    }
    console.log(newElement.value.element.wood_type)
    if (newElement.value.element.wood_type == '') {
      errors.value.push('Wybierz materiał')
    }
  
    if (!errors.value.length) {
      addElement(newElement.value);
    newElement.value = {
      element: {
        name: 'Przód',
        dimX: 2500,
        dimY: 250,
        dimZ: 25,
        wood_type: ''
              },
      quantity: 1
      }
      }
  
    else {
  
      let msg = ''
  
      for (let i=0; i <errors.value.length; i++){
        msg += errors.value[i] += "\n"
      }
  
      toast({
          message: msg,
          duration: 5000,
          position: "top-center",
          type: 'is-danger',
          animate: { in: 'backInDown', out: 'backOutUp' },
        })
  
        errors.value = []
    }
    }
  
  
  
    async function saveData() {
  
    const formData = new FormData();
  
    //console.log(formData.get('name').trim())
  
  
  
    // Add regular project data
    formData.append('name', projectName.value)
    formData.append('category', selectedCategory.value)
    formData.append('wood', selectedWood.value)
    formData.append('collection', selectedCollection.value)
    formData.append('paint', selectedPaint.value)
    formData.append('elements_margin', parseFloat(elementsMargin.value.toFixed(2)))
    formData.append('accesories_margin', parseFloat(accesoriesMargin.value.toFixed(2)))
    formData.append('additional_margin', parseFloat(additionalMargin.value.toFixed(2)))
    formData.append('summary_with_margin', parseFloat(summaryCostsWithMargin.value.toFixed(2)))
    formData.append('summary_without_margin', parseFloat(Number(summaryCosts.value).toFixed(2)))
    formData.append('elements', JSON.stringify(elements.value))
    formData.append('worktime', JSON.stringify(boxes.value))
    formData.append('accesories', JSON.stringify(accesories.value))
    formData.append('percent_elements_margin', marginA.value)
    formData.append('percent_accesories_margin', marginB.value)
    formData.append('percent_additional_margin', marginC.value)
    formData.append('elements_cost', elementsCost.value)
    formData.append('accesories_cost', accesoriesCost.value)
    formData.append('worktime_cost', worktimeCost.value)
    formData.append('customer', JSON.stringify(customer.value))
    files.value.forEach((file, index) => {
    formData.append(`files[${index}]`, file)
  })
   
  
    
  
   //ERROR CHECKING FUNCTIONS
   validateFormData(formData, errors)
  
    if (!errors.value.length) {
  
      try {
        const response = await axios.post('api/v1/product/save', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log('Server response:', response)
        console.log('Project updated successfully:', response.data)
      } catch (error) {
        console.error('Error saving the project:', error)
      }
      toast({
              message: t('save_msg'),
              duration: 5000,
              position: "top-center",
              type: 'is-success',
              animate: { in: 'backInDown', out: 'backOutUp' },
            })
      resetInput()
    } 
  
    else {
          let msg = ''
  
          for (let i=0; i <errors.value.length; i++){
            msg += errors.value[i] += "\n"
          }
          toast({
              message: msg,
              duration: 5000,
              position: "top-center",
              type: 'is-danger',
              animate: { in: 'backInDown', out: 'backOutUp' },
            })
  
            errors.value = []
          }
  
    }
  
      
  
  
    function resetInput() {
      
  
      projectName.value  = ''
      selectedWood.value = ''
      selectedCategory.value = ''
      selectedCollection.value = ''
      selectedPaint.value = ''
      elements.value = []
      accesories.value = []
      $resetBoxes()
      marginA.value = 0
      marginB.value = 0
      marginC.value = 0
  
      
  
    }
  
  
  
  </script>
  
  <style>
  
  .modal{
    --bulma-modal-content-width: 70%;
  }
  
  
  
  </style>
  