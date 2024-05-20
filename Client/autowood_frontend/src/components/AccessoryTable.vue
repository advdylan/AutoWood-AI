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
            <td><input v-model="accesory.quantity" class="input is-small" type="text" placeholder="Ilość"/></td>
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
            <td> {{ accesory.quantity }} <div class="buttons">
              <td><button @click="addAccesory(accesory)" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i></button>
                  <button @click="deleteAccesory(accesory)" class="button is-dark"><i class="fa-solid fa-minus">&nbsp;</i></button>
              </td>
            </div> </td>
            
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
import { types } from 'sass';

const store = useNewProjectStoreBeta()
const {addAccesory, deleteAccesory} = store
const {accesorytype, accesories} = storeToRefs(store)

const searchQuery = ref('')
const filterType = ref('')

const setFilterType = (type) => {
    filterType.value = type
}

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




</script>