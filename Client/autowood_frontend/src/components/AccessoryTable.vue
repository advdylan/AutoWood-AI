<template>
    <div class="acc-table-container">
    <div class="buttons">
    <button class="button is-dark" @click="setFilterType('Prowadnice')">Prowadnice</button>
    <button class="button is-dark" @click="setFilterType('Złącza')">Złącza</button>
    <button class="button is-dark" @click="setFilterType('Zawiasy')">Zawiasy</button>
    </div>
    <input v-model="searchQuery" class="input" type="text" placeholder="Search...">
    <table class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>Name</th>
            <th>Cena</th>
            <th>Typ</th>
            <th>Ilość</th>
            <th>Dodaj</th>
            
          </tr>

        </thead>
        
        <tfoot>
          
          <tr>   
          </tr>

        </tfoot>
        <tbody>
          <tr v-for="accesory in filteredAccesories.slice(0, 3)" :key="accesory.name">
            
            <th>{{ accesory.name }}</th>
            <td>{{ accesory.price }}</td>
            <td>{{ accesory.type }}</td>

            <td>
            <div class="field has-addons">
            <div class="control">
              <button @click="increaseQuantity(accesory)" class="button is-dark is-small is-height-matched"><i class="fa-solid fa-plus"></i></button> 
            </div>
            &nbsp;
            <div class="control">     
            <input v-model="accesory.quantity" class="input is-small is-height-matched" type="text" placeholder="Ilość"/>
            </div>
            &nbsp;
            <div class="control"> 
            <button @click="decreaseQuantity(accesory)" class="button is-dark is-small is-height-matched"><i class="fa-solid fa-minus"></i></button> 
            </div>
            </div>
            </td>
 
            <td><button @click="handleClick(accesory)" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i></button></td>
                   
          </tr>
        </tbody>
        
      </table>

      <p class="title is-centered is-size-3">Dodane akcesoria</p>

      <table v-if="propsAccesories" class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>Name</th>
            <th>Cena</th>
            <th>Typ</th>
            <th>Ilość</th>
            <th>Suma</th>
            <th>Usuń</th>
          </tr>
  
        </thead>
        
        <tfoot>
          
          <tr>   
          </tr>
  
        </tfoot>
        <tbody>
          <tr v-for="accesory in propsAccesories" :key="accesory.name">
            
            <th>{{ accesory.type.name }}</th>
            <td>{{ accesory.type.price }}</td>
            <td>{{ accesory.type.type }}</td>
            <td> {{ accesory.quantity  }}</td>
            <td>  {{ accesory.type.price * accesory.quantity  }} zł </td>
            <td><b-button @click="deleteAccesory(accesory)" type="is-danger"><i class="fa-solid fa-xmark"></i></b-button></td>
            
            
                   
          </tr>
        </tbody>
        
      </table>

      <table v-else class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>Name</th>
            <th>Cena</th>
            <th>Typ</th>
            <th>Ilość</th>  
            <th>Suma</th>
            <th>Usuń</th>
          </tr>

        </thead>
        
        <tfoot>
          
          <tr>   
          </tr>

        </tfoot>
        <tbody>
          <tr v-for="accesory in accesoriesStore" :key="accesory.name">
            
            <th>{{ accesory.type.name }}</th>
            <td>{{ accesory.type.price }}</td>
            <td>{{ accesory.type.type }}</td>
            <td> {{ accesory.quantity  }}</td>          
            <td>  {{ accesory.type.price * accesory.quantity  }}zł </td>
            <td><b-button @click="deleteAccesory(accesory)" type="is-danger"><i class="fa-solid fa-xmark"></i></b-button></td>
   
          </tr>
        </tbody>
        
      </table>
    </div>


    
  

</template>

<script>
export default {
    name: "AccessoryTable",

}
</script>
<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import {useProjectsListStore} from '@/store/projectslist'
import {ref, computed } from 'vue'
import { storeToRefs } from 'pinia'
import { toast } from 'bulma-toast'



const store = useNewProjectStoreBeta()
const detail_store = useProjectsListStore()

const {addAccesory, deleteAccesory, } = store
const { addAccesoryDetailProject} = detail_store
const {accesorytype, accesories, accesoriesStore} = storeToRefs(store)
const {detail_project} = storeToRefs(detail_store)


const props = defineProps({
  propsAccesories: Object,
  addAccDetail: String
})

const searchQuery = ref('')
const filterType = ref('')
const errors = ref([])

const setFilterType = (type) => {
    filterType.value = type
}


const filteredAccesories = computed(() => {

    accesorytype.value.forEach(accesory => {
    accesory.quantity = 0
    })

    let result = accesorytype.value

    if (searchQuery.value) {
        result = result.filter(accesory => 
            accesory.name.toLowerCase().
            includes(searchQuery.value.toLocaleLowerCase())         
        ) 
    }
    if (filterType.value) {
        result = result.filter(accesory => 
            accesory.type === filterType.value
        )       
    }
    
    return result
})

function increaseQuantity(accesory) {
  accesory.quantity++
}
function decreaseQuantity(accesory) {
  accesory.quantity--
}
function calculateSum(accesory) {
  return accesory.price * accesory.quantity;
}



function handleClick(accesory) {

  if (accesory.quantity <= 0) {
    errors.value.push('Niepoprawna ilość akcesorii')
  }

  if (!errors.value.length) {
    if (props.addAccDetail === 'one'){
          
          addAccesoryDetailProject(accesory)
        }
        else {

          addAccesory(accesory)         
        }
        return 0
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

</script>

<style>
.is-height-matched {
    height: 2.25em; /* Default height for Bulma's .input.is-small */
}
</style>