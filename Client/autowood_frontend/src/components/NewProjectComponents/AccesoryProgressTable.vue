<template>
    <section class="section">

    <div class="column">
        <div class="card">
            <div class="card-content">
                <div class="content">
                    <div class="projects-list-container">
                        <b-table :key="tableKey" :data="filteredAccessories" :paginated="isPaginated" :per-page="perPage" :current-page.sync="currentPage" :pagination-simple="isPaginationSimple" :pagination-position="paginationPosition" :default-sort-direction="defaultSortDirection" :pagination-rounded="isPaginationRounded" :sort-icon="sortIcon" :sort-icon-size="sortIconSize" default-sort="user.first_name" aria-next-label="Next page" aria-previous-label="Previous page" aria-page-label="Page" aria-current-label="Current page" :page-input="hasInput" :pagination-order="paginationOrder" :page-input-position="inputPosition" :debounce-page-input="inputDebounce">
                            <template v-for="(column, index) in columns" :key="column.id">
                                <b-table-column v-bind="column">
                                    <template v-if="column.searchable && !column.numeric" #searchable="props">
                                        <b-input v-model="props.filters[props.column.field]" :placeholder="$t('search')" icon="magnify"/>
                                    </template>

                                    <template v-if="column.field === 'nawigacja'" #header>
                                    </template>
                                    <template v-slot="props">
                                        <template v-if="column.field == 'quantity'">
                                            <input type="number" placeholder="Quantity" class="input is-small" v-model="quantities[props.row.id]">
                                        </template>
                                        <template v-else-if="column.field === 'nawigacja'">
                                            <button @click="handleAddAccButton(props.row)" class="button is-success"> <i class="fa-solid fa-plus"></i></button>
                                        </template>
                                        <template v-else>
                                          {{ getNestedValue(props.row, column.field) }}
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
    
    
    <div class="box">
      <table class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>{{ $t("name")}}</th>
            <th>{{ $t("price")}}</th>
            <th>{{ $t("typ")}}</th>
            <th>{{ $t("quantity")}}</th>  
            <th>{{ $t("quantity")}}</th>
            <th class="delete-column">{{ $t("delete")}}</th>
          </tr>

        </thead>
        
        <tfoot>
          
          <tr>   
          </tr>

        </tfoot>
        <tbody>
          <tr v-for="accesory in accesories" :key="accesory.name">
            
            <th>{{ accesory.type.name }}</th>
            <td>{{ accesory.type.price }}</td>
            <td>{{ accesory.type.type }}</td>
            <td> {{ accesory.quantity  }}</td>          
            <td>  {{ (accesory.type.price * accesory.quantity).toFixed(2)   }}zł </td>
            <td><b-button @click="deleteAccesory(accesory)" type="is-danger"><i class="fa-solid fa-xmark"></i></b-button></td>
   
          </tr>
        </tbody>
        
      </table>
      
    </div>
  </section>
</template>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'
import { onMounted, ref, watch, onBeforeUnmount, reactive, computed, nextTick } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'
import {validateFormData, validateNewAccesory} from '@/validators/Validators.js'
import AccessoryTable from '../AccessoryTable.vue'

import { useRouter, useRoute, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const router = useRouter()
const route = useRoute()


const showActiveAcc = ref(false)
const editMode = ref(false)
const editedAcc = ref(false)
const showAccModal = ref(false)
const saveReminder = ref(false)
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
const quantities = ref({})



//table variables
let isPaginated = true
let isPaginationSimple = true
let isPaginationRounded = false
let paginationPosition = 'bottom'
let defaultSortDirection = 'asc'
let sortIcon= 'arrow-up'
let sortIconSize= 'is-small'
let currentPage= 1
let perPage= 5
let hasInput= false
let paginationOrder= ''
let inputPosition= ''
let inputDebounce= ''

const filteredAccessories = computed(() => {
    const newAcc = accesorytype.value
    .filter(acc => acc.is_active !== showActiveAcc.value)
    .map(acc => ({
      id: acc.id,
      project: 0,
      quantity: quantities.value[acc.id],
      type: {
        id: acc.id,
        name: acc.name,
        type: acc.type,
        weight: acc.weight,
        price: acc.price,
        description: acc.description,
      }
    }))
    return newAcc
})


const {loadData, addAccesorytype, updateAccesories, addAccesory, deleteAccesory} = newProjectStore
const {accesories, accesorytype} = storeToRefs(newProjectStore)


function getAccessoryTypes(accesoryList) {
  return [...new Set(accesoryList.flatMap(item => item.type_choices.map(choice => choice[0])))];
}

const accesorytypes = getAccessoryTypes(accesorytype.value)

function handleUpdateAccesories(accesorytype) {

const accesorytypes = getAccessoryTypes(accesorytype)
validateNewAccesory(accesorytype,errors,accesorytypes)

/* for ( let accesory of accesorytype) {
  console.log(accesory.name)
}
 */




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
        saveReminder.value = false
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

function handleAddAccButton(accesory) {
  
  const newAccesory = {
        id: accesory.id,
        project: 0,
        quantity: accesory.quantity,
        type: {
            description: accesory.type.description,
            id: accesory.type.id,
            name: accesory.type.name,
            price: accesory.type.price,
            type: accesory.type.type,
            weight: accesory.type.weight
        }
    }
    accesories.value.push(newAccesory)

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
    console.log(accesorytypes)
    validateNewAccesory(newAccesory,errors,accesorytypes)

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
      showAccModal = false
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

    function handleDeleteButton(row){
      const index = accesorytype.value.findIndex(item => item.id === row.id)
      accesorytype.value[index].is_active = false
      //accesorytype.value.splice(index, 1)
      tableKey.value += 1 //refreshing the table
    }






let originalArray = [...accesorytype.value]

const editedRows = ref(new Set())
const pendingRoute = ref(null)

const editedRowsArray = computed(()=> [...editedRows.value])
const markAsEdited = (row) => {
    editedRows.value.add(row)
}





onBeforeRouteLeave(async (to, from) => {

//console.log("editedRows value:", editedRows.value);
//console.log("Before if",editedRows.value.size)

if (editedRows.value.size > 0) 
{
console.log("After if ", editedRows.value.size)
saveReminder.value = true // open modal
pendingRoute.value = to;
return new Promise((resolve, reject) => {
    const unwatch = watch(saveReminder, (val)=> {
        if (!val) {
            unwatch()
            reject()
            editedRows.value = new Set()
            router.push(pendingRoute.value.fullPath)
            pendingRoute.value = null

            console.log("CLEARING if!val")
        } else {
            unwatch()
            resolve()
            editedRows.value = new Set()
            router.push(pendingRoute.value.fullPath)
            console.log("CLEARING else")
        }
    })
}) 
}  

/* else if(editedRows.value.size === 0) {
editedRows.value = new Set()
console.log("CLEARING elif")

} */

})

function discardChanges() {

console.log('Discarding changes')
saveReminder.value = false
router.push(pendingRoute.value.fullPath)

}

const preventNavigation = (event) => {
    if (editedRows.value) {
        event.preventDefault();
        event.returnValue = ''; // Trigger browser confirmation dialog
    }
};

onMounted(() => {
    loadData()
    /* window.addEventListener('beforeunload', preventNavigation); */
})

onBeforeUnmount (() => {
   /*  window.removeEventListener('beforeunload', preventNavigation); */
    console.log("Before unmount")
})

function getNestedValue(obj, path) {
    return path.split('.').reduce((acc, part) => acc && acc[part], obj)
}
let columns = [
    { 
    field: 'type.name', 
    label: 'Nazwa',
    searchable: true,
    sortable: true
    },
    { 
    field: 'type.type', 
    label: 'Type',
    searchable: true,
    sortable: true
    },
    { 
    field: 'type.weight', 
    label: 'Waga',
    searchable: true,
    sortable: true
    },
    {  
    field: 'type.price', 
    label: 'Cena',
    searchable: true,
    sortable: true
    },
    {
    field: 'quantity',
    label: 'Quantity',
    },
    {
    field: 'nawigacja',
    label: 'Nawigacja',
    centered: true
    }
]


</script>

<style>
.is-height-matched {
    height: 2.25em; /* Default height for Bulma's .input.is-small */
}
.delete-column {
  width: 50px; /* Adjust this width to fit your icon */
  text-align: center;
}
.input-column {
  width: 200px;
  text-align: center;
}
.delete-column b-button {
  padding: 0;
}
</style>