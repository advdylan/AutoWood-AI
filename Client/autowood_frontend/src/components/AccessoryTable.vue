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
          


            <td><button @click="addAccesory(accesory)" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i></button></td>
                   
          </tr>
        </tbody>
        
      </table>

      <table class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>Name</th>
            <th>Cena</th>
            <th>Typ</th>
            <th>Ilość</th>
            
            <th>Suma</th>
          </tr>

        </thead>
        
        <tfoot>
          
          <tr>   
          </tr>

        </tfoot>
        <tbody>
          <tr v-for="accesory in accesories" :key="accesory.name">
            
            <th>{{ accesory.name }}</th>
            <td>{{ accesory.price }}</td>
            <td>{{ accesory.type }}</td>
            <td> {{ accesory.quantity  }} 
                  <button @click="deleteAccesory(accesory)" class="button is-dark">Usuń</button>

             </td>
            
            <td> {{ accesory.sum }}</td>
            
            
                   
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
import {ref, computed} from 'vue'
import { storeToRefs } from 'pinia'


const store = useNewProjectStoreBeta()
const {addAccesory, deleteAccesory} = store
const {accesorytype, accesories} = storeToRefs(store)

const searchQuery = ref('')
const filterType = ref('')

const setFilterType = (type) => {
    filterType.value = type
}

accesorytype.forEach(accesory => {
  accesory.quantity = 0
})

const filteredAccesories = computed(() => {
  
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






</script>

<style>
.is-height-matched {
    height: 2.25em; /* Default height for Bulma's .input.is-small */
}
</style>