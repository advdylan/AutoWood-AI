<template>
  <div class="columns">
    <div class="column is-halfs is-offset-one-quarter">

        <div class="field is-grouped">

          <div class="field">      
                      <label class="label is-size-5">{{$t("project_name")}}</label>
                      <div class="control">
                        <input v-model="projectName" :class="inputClass" type="text" :placeholder="$t('project_name')">
                      </div>
                    </div>
  
                    <div class="field">
                      <label class="label is-size-5">{{$t("wood_type")}}</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="selectedWood">
                            <option v-for="woodItem in wood"> {{ woodItem.name }}</option>
                          </select>
                        </div>
                      </div>
                    </div>
  
                    <div class="field">
                      <label class="label is-size-5">{{$t("category")}}</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="selectedCategory">
                            <option v-for="categoryItem in category"> {{ categoryItem.name }}</option>
                          </select>
                        </div>
                      </div>
                    </div>
  
                    <div class="field">
                      <label class="label is-size-5">{{$t("collection")}}</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="selectedCollection">
                          <option v-for="collection in collection"> {{ collection.name }}</option>
                          </select>
                        </div>
                      </div>
                      </div>
  
                      <div class="field">
                        <label class="label is-size-5">{{$t("painting")}}</label>
                        <div class="control">
                          <div class="select">
                            <select v-model="selectedPaint">
                              <option v-for="paints in paints">{{ paints.name}}</option>
                            </select>
                          </div>
                        </div>
                      </div> 

        </div>

                        
                                   
                    



    </div>

    
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
  