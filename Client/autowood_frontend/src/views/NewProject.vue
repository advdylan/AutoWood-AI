<template>
  <div class="columns">
      <div class="column is-full">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title is-centered is-size-3">Szkic projektu</p>        
            </header>

            <div class="columns">
            <div class="column is-two-fifths">
              <div class="card-content">               
                <div class="content">
                  <div class="field">
                    <label class="label is-size-5">Nazwa projektu</label>
                    <div class="control">
                      <input v-model="projectName" :class="inputClass" type="text" placeholder="Nazwa projektu">
                    </div>
                  </div>

                  <div class="field">
                    <label class="label is-size-5">Materiał</label>
                    <div class="control">
                      <div class="select">
                        <select v-model="selectedWood">
                          <option v-for="woodItem in wood"> {{ woodItem.name }}</option>
                        </select>
                      </div>
                    </div>
                  </div>

                  <div class="field">
                    <label class="label is-size-5">Kategoria</label>
                    <div class="control">
                      <div class="select">
                        <select v-model="selectedCategory">
                          <option v-for="categoryItem in category"> {{ categoryItem.name }}</option>
                        </select>
                      </div>
                    </div>
                  </div>

                  <div class="field">
                    <label class="label is-size-5">Kolekcja</label>
                    <div class="control">
                      <div class="select">
                        <select v-model="selectedCollection">
                        <option v-for="collection in collection"> {{ collection.name }}</option>
                        </select>
                      </div>
                    </div>
                    </div>

                    <div class="field">
                      <label class="label is-size-5">Malowanie</label>
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
                  
                  
                  <div class="column">

                    <div class="card-content">               
                      <div class="content">
                    <div class="card">
                      <header class="card-header" @click="isCollapsedelements = !isCollapsedelements">
                        <p class="card-header-title is-size-5">
                          Lista elementów
                        </p>
                        <a href="#collapsible-card" data-action="collapse" class="card-header-icon is-hidden-fullscreen" aria-label="more options">
                          <span class="icon">
                            <i class="fas fa-angle-down" aria-hidden="true"></i>
                          </span>
                        </a>
                      </header>

                      <div id="collapsible-card" class="is-collapsible" v-show="isCollapsedelements">
                      <div class="card-content">

                        <ElementsTable :elements="elements" />
                    </div>

                      

                      <div class="buttons">

                        <button @click="showElementModal = true" data-target="newelement-modal" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>Dodaj element</button>

                       
                        <button class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj tabelę</button>
                        <button class="button is-dark"><i class="fa-regular fa-file">&nbsp;</i>Wygeneruj rozpiskę</button>
                      </div>
                      </div>
                    

                  

         </div> 
         
         
         <div class="card">
          <header class="card-header" @click="isCollapsedpaints = !isCollapsedpaints">
            <p class="card-header-title is-size-5">
              Koszty pracy
            </p>
            <a href="#collapsible-card" data-action="collapse" class="card-header-icon is-hidden-fullscreen" aria-label="more options">
              <span class="icon">
                <i class="fas fa-angle-down" aria-hidden="true"></i>
              </span>
            </a>
          </header>

          <div id="collapsible-card" class="is-collapsible" v-show="isCollapsedpaints">
            <div class="card-content">
              <WorktimeType/>        
              </div>
              </div>
              </div>     


              <div class="card">
                <header class="card-header" @click="isCollapsedacc = !isCollapsedacc">
                  <p class="card-header-title is-size-5">
                    Akcesoria
                  </p>
                  <a href="#collapsible-card" data-action="collapse" class="card-header-icon is-hidden-fullscreen" aria-label="more options">
                    <span class="icon">
                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                    </span>
                  </a>
                </header>
      
                <div id="collapsible-card" class="is-collapsible" v-show="isCollapsedacc">
                  <div class="card-content">
                    <button @click="showAccModal = true" data-target="newelement-modal" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>Przeszukaj akcesoria</button>

                    
                    </div>
                    </div>
                    </div> 


                    
         </div> 
        </div>
      </div>
     </div>    
    </div>                          
   </div>           
  </div>

  <div v-bind:class="{'is-active': showElementModal}" id="newelement-modal" class="modal">
    <div class="modal-background"></div>
    <div class="modal-content">


      <div class="modal-card">
        <header class="modal-card-head">
              <p class="modal-card-title is-centered is-size-3">Dodaj element</p>
              <button class="delete" aria-label="close" @click="showElementModal = false"></button>        
            </header>
            
        
        <section class="modal-card-body">
          <div class="columns">
            <div class="column is-two-fifths">

          <form @submit.prevent="submitForm">

          <div class="field">
            <label class="label">Nazwa</label>
            <div class="control">
              <input class="input" type="text" placeholder="Nazwa" v-model="newElement.element.name">             
            </div>
          </div>

          <div class="field">
            <label class="label">Długość</label>
            <div class="control">
              <input class="input" type="number" placeholder="Długość" v-model="newElement.element.dimX">           
            </div>
          </div>

          <div class="field">
            <label class="label">Szerokość</label>
            <div class="control">
              <input class="input" type="number" placeholder="Szerokosć" v-model="newElement.element.dimY" >             
            </div>
          </div>

          <div class="field">
            <label class="label">Grubość</label>
            <div class="control">
              <input class="input" type="number" placeholder="Grubość" v-model="newElement.element.dimZ">             
            </div>
          </div>

          <div class="field">
            <label class="label">Ilość</label>
            <div class="control">
              <input class="input" type="number" placeholder="Ilość" v-model="newElement.quantity" >             
            </div>
          </div>

          <div class="field">
            <label class="label">Materiał</label>
            <div class="control">
              <div class="select">
                <select v-model="newElement.element.wood_type">
                  <option v-for="woodItem in wood" :key="woodItem.id" :value="woodItem">
                    {{ woodItem.name }}
                  </option>
                </select>
              </div>
            </div>
          </div>
 
        <footer class="modal-card-foot">
          <div class="buttons">
            <button type="submit" class="button is-success">Dodaj element</button>
           
          </div>
        </footer>
        

      </form>
    </div>
    <div class="column">
      <ElementsTable :elements="elements" />
    </div>
    </div>

    </section>

    </div>
    </div>


  </div>

  <div v-bind:class="{'is-active': showAccModal}" id="newelement-modal" class="modal">
    <div class="modal-background"></div>
    <div class="modal-content">

      <div class="modal-card">
        <header class="modal-card-head">
              <p class="modal-card-title is-centered is-size-3">Akcesoria</p>
              <button class="delete" aria-label="close" @click="showAccModal = false"></button>        
            </header>
            <section class="modal-card-body">
              <AccessoryTable />
            </section>

    </div>
    </div>
  </div>
  

  <div class="card">
    <div class="card-content">
      <p class="title">
        Podsumowanie
      </p>
     
    </div>
    <Summary
    :prop-margin-a="Number(marginA)"
    :prop-margin-b="Number(marginB)"
    :prop-margin-c="Number(marginC)"
    >
      <div class="buttons">
        <b-button @click="saveData" type="is-success" >
          <i class="fa-solid fa-floppy-disk"></i>
          Zapisz projekt
        </b-button>
        <b-button @click="resetInput" type="is-danger" >
          <i class="fa-solid fa-xmark"></i>
          Wyczyść projekt
        </b-button>
      </div>
    </Summary>
    

    <footer class="card-footer">
      <p class="card-footer-item">
        <span>
        
        </span>
      </p>
      <p class="card-footer-item">
        <span>
          Wydrukuj podsumowanie dla klienta
        </span>
      </p>
      
    </footer>
  </div>

  

  

</template>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { useSummaryStore } from '@/store/summary'
import {ref, computed, onUnmounted, watch, watchEffect} from 'vue'
import { storeToRefs } from 'pinia'

import ElementsTable from '@/components/ElementsTable'
import WorktimeType from '@/components/WorktimeType'
import AccessoryTable from '@/components/AccessoryTable.vue'
import Summary from '@/components/Summary.vue'

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
const elementStore = useNewProjectStoreBeta()
const summaryStore = useSummaryStore()

const { addElement, loadData, $resetBoxes } = elementStore
const {summaryCosts, elementsMargin, accesoriesMargin, additionalMargin,summaryCostsWithMargin, elementsCost, accesoriesCost} = storeToRefs(summaryStore)

loadData()

const {elements, wood, collection, paints, category, boxes, accesories, marginA, marginB, marginC} = storeToRefs(elementStore)


const submitForm = () => {

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
      wood_type: 'Sosna'
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
  const projectpostData = {
    name: projectName.value,
    category: selectedCategory.value,
    wood: selectedWood.value,
    collection: selectedCollection.value,
    paint: selectedPaint.value,
    elements_margin: parseFloat(elementsMargin.value.toFixed(2)),
    accesories_margin: parseFloat(accesoriesMargin.value.toFixed(2)),
    additional_margin: parseFloat(additionalMargin.value.toFixed(2)),
    summary_with_margin: parseFloat(summaryCostsWithMargin.value.toFixed(2)),
    summary_without_margin: parseFloat(summaryCosts.value.toFixed(2)),
    elements: elements.value,
    worktime: boxes.value,
    accesories: accesories.value,
    percent_elements_margin: marginA.value,
    percent_accesories_margin: marginB.value,
    percent_additional_margin: marginC.value,
    elements_cost: elementsCost.value,
    accesories_cost: accesoriesCost.value,


    
  }
  let jsonProjectData = JSON.stringify(projectpostData)
  let parsedProjectData = JSON.parse(jsonProjectData)
  console.log(parsedProjectData.name)
  

  if (typeof parsedProjectData.name !== 'string' || parsedProjectData.name.trim() === '') {
    errors.value.push('Podaj właściwą nazwę wyceny w oknie "Nazwa projektu"')
    //inputClass.value = 'input is-danger'
  }
  if (typeof parsedProjectData.category !== 'string' || parsedProjectData.name.trim() === '') {
    errors.value.push('Podaj właściwą nazwę w oknie "Kategoria"')
  }
  if (typeof parsedProjectData.wood !== 'string' || parsedProjectData.name.trim() === '') {
    errors.value.push('Podaj właściwą nazwę w oknie "Materiał"')
  }
  if (typeof parsedProjectData.collection !== 'string' || parsedProjectData.name.trim() === '') {
    errors.value.push('Podaj właściwą nazwę w oknie "Kolekcja"')
  }
  if (typeof parsedProjectData.paint !== 'string' || parsedProjectData.name.trim() === '') {
    errors.value.push('Podaj właściwą nazwę w oknie "Malowanie"')
  }


  if (!errors.value.length) {
      await axios
          .post(`api/v1/product/save`, jsonProjectData)
          .then(response => {  
            toast({
              message: `Wycena ${parsedProjectData.name} dodane poprawnie`,
              duration: 5000,
              position: "top-center",
              type: 'is-success',
              animate: { in: 'backInDown', out: 'backOutUp' },
            })        
          })
          .catch(error => {
            console.log(error)
          })
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
:root
.modal{
  --bulma-modal-content-width: 100rem;
}

</style>
