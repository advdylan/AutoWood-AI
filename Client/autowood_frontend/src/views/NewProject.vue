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
                      <input v-model="projectName" class="input" type="text" placeholder="Nazwa projektu">
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

                      <ElementsTable />
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
              <input class="input" type="text" placeholder="Nazwa" v-model="newElement.name" >             
            </div>
          </div>

          <div class="field">
            <label class="label">Długość</label>
            <div class="control">
              <input class="input" type="text" placeholder="Długość" v-model="newElement.dimX" >             
            </div>
          </div>

          <div class="field">
            <label class="label">Szerokość</label>
            <div class="control">
              <input class="input" type="text" placeholder="Szerokosć" v-model="newElement.dimY" >             
            </div>
          </div>

          <div class="field">
            <label class="label">Grubość</label>
            <div class="control">
              <input class="input" type="text" placeholder="Grubość" v-model="newElement.dimZ">             
            </div>
          </div>

          <div class="field">
            <label class="label">Ilość</label>
            <div class="control">
              <input class="input" type="text" placeholder="Ilość" v-model="newElement.quantity" >             
            </div>
          </div>

          <div class="field">
            <label class="label">Materiał</label>
            <div class="control">
              <div class="select">
                <select v-model="newElement.wood_type">
                  <option v-for="wood in wood"> {{ wood.name}}</option >
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
      <ElementsTable/>
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
      <p class="subtitle">{{projectName}}</p>
    </div>
    <Summary/>
    <footer class="card-footer">
      <p class="card-footer-item">
        <span>
          Wydrukuj podsumowanie wewnętrzne
          <button @click="printData" class="button is-primary">PRINT</button>
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
import {ref, computed} from 'vue'
import { storeToRefs } from 'pinia'
import ElementsTable from '@/components/ElementsTable'
import WorktimeType from '@/components/WorktimeType'
import AccessoryTable from '@/components/AccessoryTable.vue'
import Summary from '@/components/Summary.vue'

const showElementModal = ref(false)
const showElementModalTable = ref(false)
const showAccModal = ref(false)
const isCollapsedacc = ref(false)
const isCollapsedpaints = ref(false)
const isCollapsed = ref(false)
const isCollapsedelements = ref(false)
const project = ref({})


const projectName = ref()
const selectedWood = ref()
const selectedCategory = ref()
const selectedCollection = ref()
const selectedPaint = ref()

const newElement = ref({
id: '',
name: '',
dimX: '',
dimY: '',
dimZ: '',
quantity: '',
wood_type: ''
})

const elementStore = useNewProjectStoreBeta()
const summaryStore = useSummaryStore()

const { addElement, loadData, } = elementStore
const {summaryCosts, elementsMargin, accesoriesMargin, additionalMargin,summaryCostsWithMargin} = storeToRefs(summaryStore)

console.log(elementsMargin.value, accesoriesMargin.value, additionalMargin.value, summaryCostsWithMargin.value)

loadData()
const {elements, wood, collection, paints, category, boxes} = storeToRefs(elementStore)

const submitForm = () => {
addElement(newElement.value)
newElement.value = {
  id: '',
  name: '',
  dimX: '',
  dimY: '',
  dimZ: '',
  quantity: '',
  wood_type: ''
}
}

  

function printData() {
  const projectpostData = {
    name: projectName.value,
    wood: selectedWood.value,
    elements_margin: parseFloat(elementsMargin.value.toFixed(2)),
    accesories_margin: parseFloat(accesoriesMargin.value.toFixed(2)),
    additional_margin: parseFloat(additionalMargin.value.toFixed(2)),
    summary_with_margin: parseFloat(summaryCostsWithMargin.value.toFixed(2)),
    summary_without_margin: parseFloat(summaryCosts.value.toFixed(2)),
    elements: elements.value,
    worktime: boxes.value,

    
  }
  let jsonProjectData = JSON.stringify(projectpostData)
  console.log(projectpostData)
  console.log(jsonProjectData)
}






















</script>

<style>
:root
.modal{
  --bulma-modal-content-width: 100rem;
}

</style>
