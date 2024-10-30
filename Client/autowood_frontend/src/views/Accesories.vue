<template>
  
    <div class=columns >
        <div class="column is-full">
       
  
          <div class="notification is-text">
            <div class="title is-centered is-size-4">
              Dział zarządzania akcesoriami     
            </div>
            <div class="text">
              Każdorazowa zmiana poniższych kosztów akcesorii nie działa wstecz. Tylko nowe projekty otrzymają nowe wartości.
            </div>
          </div>
        
        </div>
      </div>
      <div class="column">

        <div class="card">
            <header class="card-header">
              <p class="card-header-title is-centered is-size-4">Akcesoria
                <span>&nbsp;<i class="fa-solid fa-screwdriver-wrench fa-lg"></i></span>
              </p>
              
            </header>
            <div class="card-content">
              <div class="content">
                <div class="projects-list-container">
                    <b-table :key="tableKey" :data="accesorytype"
                    :paginated="isPaginated"
                    :per-page="perPage"
                    :current-page.sync="currentPage"
                    :pagination-simple="isPaginationSimple"
                    :pagination-position="paginationPosition"
                    :default-sort-direction="defaultSortDirection"
                    :pagination-rounded="isPaginationRounded"
                    :sort-icon="sortIcon"
                    :sort-icon-size="sortIconSize"
                    default-sort="user.first_name"
                    aria-next-label="Next page"
                    aria-previous-label="Previous page"
                    aria-page-label="Page"
                    aria-current-label="Current page"
                    :page-input="hasInput"
                    :pagination-order="paginationOrder"
                    :page-input-position="inputPosition"
                    :debounce-page-input="inputDebounce"
                    >                    
                        <template v-for="column in columns" :key="column.id">
                            <b-table-column v-bind="column">
                                <template v-if="column.searchable && !column.numeric" #searchable="props">
                                    <b-input
                                        v-model="props.filters[props.column.field]"
                                        placeholder="Wyszukaj"
                                        icon="magnify"/>
                                </template>
                                <template v-slot="props">
                                    
                                    <template v-if="column.field === 'nawigacja'">
                                      <b-button type="is-danger"
                                      icon-left="x">
                                      Usuń
                                  </b-button>                            

                                    </template>
                                    <template v-else>
                                    {{ props.row[column.field] }}
                                </template>
                            </template>
                            </b-table-column>
                        </template>
                    </b-table>
                </div>
                </div>
              </div>
            </div>               
        </div>

      <div class="column">

        <div class="card">
            <header class="card-header">
              <p class="card-header-title is-centered is-size-4">Dodaj nowe akcesoria
                <span>&nbsp;<i class="fa-solid fa-plus"></i></span>
              </p>
              
            </header>
            <div class="card-content">
              <div class="content">
                
                <nav class="level">
                    <div class="level-item has-text-centered">
                        <input v-model="accesory.name" class="input" type="text" placeholder="Nazwa"/>
                    </div>
                    <div class="level-item has-text-centered">
                      <div class="select">
                        <select v-model="accesory.type">
                          <option v-for="type in accesorytypes" :value="type">
                            {{ type }}                    
                          </option>
                        </select>
                      </div>
                    </div>
                    <div class="level-item has-text-centered">
                        <input v-model="accesory.weight" class="input" type="text" placeholder="Waga"/>
                    </div>
                    <div class="level-item has-text-centered">
                        <input v-model="accesory.price" class="input" type="text" placeholder="Cena"/>
                    </div>
                    <div class="level-item has-text-centered">
                        <button v-on:click="handleAddButton()" class="button is-success">Dodaj</button>
                    </div>
                </nav>

                </div>
              </div>
            </div>               
        </div>






<div class="modal" v-bind:class="{'is-active': showAccModal}" id="newelement-modal" style="--bulma-modal-content-width: 50%;" >
  <div class="modal-background"></div>
  <div class="modal-content">

    <div class="modal-card">
      <header class="modal-card-head">
            <p class="modal-card-title is-centered is-size-2">Dodaj nowe akcesorium</p>
            <button class="delete" aria-label="close" @click="showAccModal = false"></button>        
          </header>
          <section class="modal-card-body has-text-centered">
            <div class="notification is-success">
              <button class="delete"></button>
              Sprawdź poprawność i dodaj opis nowego akcesorium
            </div>
            <nav class="level">
              <div class="level-item has-text-centered">
                  <input v-model="accesory.name" class="input" type="text" placeholder="Nazwa"/>
              </div>
              <div class="level-item has-text-centered">
                <div class="select">
                  <select v-model="accesory.type">
                    <option v-for="type in accesorytypes" :value="type">
                      {{ type }}                    
                    </option>
                  </select>
                </div>
              </div>
              <div class="level-item has-text-centered">
                  <input v-model="accesory.weight" class="input" type="text" placeholder="Waga"/>
              </div>
              <div class="level-item has-text-centered">
                  <input v-model="accesory.price" class="input" type="text" placeholder="Cena zł"/>
              </div>
              
          </nav>  

          
          <div class="label">Opis</div>
          <textarea v-model="accesory.description" placeholder="Opis" class="textarea"></textarea>

        </section>

            <footer class="modal-card-foot">
              
              <div class="buttons">
              <button
              @click="handleUpdateAccesories(accesorytype);
              "
              class="button is-success"><i class="fa-solid fa-plus">&nbsp;</i>Dodaj
              </button>
              <button @click="showAccModal = !showAccModal;
                " class="button"><i class="fa-solid fa-ban">&nbsp;</i>Anuluj</button>
            </div>

            </footer>
            
           
              
         
            
          

  </div>
  </div>
</div>

</template>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'
import { onMounted, ref, watch, computed } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'

import {validateFormData} from '@/validators/Validators.js'

const showAccModal = ref(false)
const newProjectStore = useNewProjectStoreBeta()
const data = ref([])
const tableKey = ref(0)
const accesory = ref({
  description: '',
  name: '',
  price: '',
  type: '',
  weight: ''
})
const typeChoices = ref([])
const errors = ref([])
let isPaginated = true
let isPaginationSimple = true
let isPaginationRounded = false
let paginationPosition = 'bottom'
let defaultSortDirection = 'asc'
let sortIcon= 'arrow-up'
let sortIconSize= 'is-small'
let currentPage= 1
let perPage= 10
let hasInput= false
let paginationOrder= ''
let inputPosition= ''
let inputDebounce= ''
const {loadData, addAccesorytype, updateAccesories} = newProjectStore
const {accesories, accesorytype} = storeToRefs(newProjectStore)



function getAccessoryTypes(accesoryList) {
  return [...new Set(accesoryList.flatMap(item => item.type_choices.map(choice => choice[0])))];
}

const accesorytypes = getAccessoryTypes(accesorytype.value)

function handleUpdateAccesories(accesorytype) {

for ( let accesory of accesorytype) {
  console.log(accesory.name)


}

if(!errors.value.length) {      


  const result = updateAccesories(accesorytype)
  

  if (result) {
    toast({
          message: `Poprawnie dodane nowe akcesoria`,
          duration: 5000,
          position: "top-center",
          type: 'is-success',
          animate: { in: 'backInDown', out: 'backOutUp' },
        })
  }

  else {
    toast({
          message: `Czasy pracy nie zaktualizowane poprawnie`,
          duration: 5000,
          position: "top-center",
          type: 'is-danger',
          animate: { in: 'backInDown', out: 'backOutUp' },
        })
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

function handleAddButton() {      

    let tempId = -1 //temporary ID for frontend new accesories
    const allTypeChoices = accesorytype.value.flatMap(item => item.type_choices) 
    const uniqueTypeChoices = [...new Set(allTypeChoices.map(JSON.stringify))].map(JSON.parse)

      const newAccesory = {
        description: accesory.value.description,
        id: tempId--,
        name: accesory.value.name,
        price: accesory.value.price,
        type: accesory.value.type,
        weight: accesory.value.weight,
        type_choices: uniqueTypeChoices
    }
    /* console.log("Accesorytype: ", accesorytype.value)
    console.log("NewAcc:" , newAccesory) */

    //error CHECKING HERE

    if (newAccesory.name.trim() === '') {
      errors.value.push("Błędna nazwa")
    }
    if (newAccesory.type.trim() === '') {
      errors.value.push("Błędna typ")
    }
    if (newAccesory.weight.trim() === '' || newAccesory.weight.trim() <= 0) {
      errors.value.push("Błędna waga")
    }
    if (newAccesory.price.trim() === '' || newAccesory.price.trim() <= 0) {
      errors.value.push("Błędna cena")
    }

    if (!errors.value.length) {
      addAccesorytype(newAccesory)
      tableKey.value += 1 //Refreshing table data 
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

    function handleDeleteButton(accesory){
      return 0
    }

    



let columns = [
    { 
    field: 'name', 
    label: 'Nazwa',
    searchable: true
    },
    { 
    field: 'type', 
    label: 'Typ',
    searchable: true 
    },
    { 
    field: 'weight', 
    label: 'Waga',
    searchable: true
    },
    {  
    field: 'price', 
    label: 'Cena',
    searchable: true 
    },
    {
    field: 'nawigacja',
    label: 'Nawigacja'
    }
]

onMounted(() => {
    loadData()
    
   
    
})

</script>


<style>

</style>