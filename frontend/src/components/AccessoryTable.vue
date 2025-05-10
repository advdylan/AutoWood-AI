<template>

    <section class="section">
    <div class="buttons">
    <button class="button is-dark" @click="setFilterType('Prowadnice')">{{ $t("runner_systems")}}</button>
    <button class="button is-dark" @click="setFilterType('Złącza')">{{ $t("fittings")}}</button>
    <button class="button is-dark" @click="setFilterType('Zawiasy')">{{ $t("hinges")}}</button>
    </div>
    <input v-model="searchQuery" class="input" type="text" placeholder="Search...">
    <table class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>{{ $t("name")}}</th>
            <th>{{ $t("price")}}</th>
            <th>{{ $t("typ")}}</th>
            <th class="input-column">{{ $t("quantity")}}</th>
            <th class="delete-column">{{ $t("add")}}</th>
            
          </tr>

        </thead>
        
        <tfoot>
          
          <tr>   
          </tr>

        </tfoot>
        <tbody>
          <tr v-for="accesory in filteredAccesories.slice(0, 10)" :key="accesory.name">
            
            <th>{{ accesory.name }}</th>
            <td>{{ accesory.price }}</td>
            <td>{{ accesory.type }}</td>

            <td>
            <div class="field has-addons">
            <div class="control">
              <button @click="increaseQuantity(accesory)" class="button is-success is-height-matched"><i class="fa-solid fa-plus"></i></button> 
            </div>
            &nbsp;
            <div class="control">     
            <input v-model="accesory.quantity" class="input is-height-matched" type="text" :placeholder="$t('quantity')"/>
            </div>
            &nbsp;
            <div class="control"> 
            <button @click="decreaseQuantity(accesory)" class="button is-danger is-height-matched"><i class="fa-solid fa-minus"></i></button> 
            </div>
            </div>
            </td>
 
            <td><button @click="handleClick(accesory)" class="button is-success"><i class="fa-solid fa-plus">&nbsp;</i></button></td>
                   
          </tr>
        </tbody>
        
      </table>

      <p class="title is-centered is-size-3">{{ $t("accessories_list")}}</p>

      <table v-if="propsAccesories" class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>{{ $t("name")}}</th>
            <th>{{ $t("price")}}</th>
            <th>{{ $t("typ")}}</th>
            <th >{{ $t("quantity")}}</th>
            <th>{{ $t("sumary")}}</th>
            <th class="delete-column">{{ $t("delete")}}</th>
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
            <td>  {{ (accesory.type.price * accesory.quantity).toFixed(2)  }} zł </td>
            <td><b-button @click="deleteAccesory(accesory)" type="is-danger"><i class="fa-solid fa-xmark"></i></b-button></td>
            
            
                   
          </tr>
        </tbody>
        
      </table>

      <table v-else class="table is-bordered is-striped is-hoverable is-fullwidth">
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
          <tr v-for="accesory in accesoriesStore" :key="accesory.name">
            
            <th>{{ accesory.type.name }}</th>
            <td>{{ accesory.type.price }}</td>
            <td>{{ accesory.type.type }}</td>
            <td> {{ accesory.quantity  }}</td>          
            <td>  {{ (accesory.type.price * accesory.quantity).toFixed(2)   }}zł </td>
            <td><b-button @click="deleteAccesory(accesory)" type="is-danger"><i class="fa-solid fa-xmark"></i></b-button></td>
   
          </tr>
        </tbody>
        
      </table>



    
    </section>
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

  if (accesory.quantity <= 0 || typeof accesory.quantity != 'number')   {
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