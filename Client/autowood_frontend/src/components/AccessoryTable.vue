<template>
    <div class="acc-table-container">
    <table class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>Name</th>
            <th>Cena</th>
            <th>Typ</th>
            <th>Ilość</th>
          </tr>

        </thead>
        
        <tfoot>
          
          <tr>
            
          </tr>
        
        
        </tfoot>
        <tbody>
          <tr v-for="accesory in accesorytype" :key="accesory.name">
            
            <th>{{ accesory.name }}</th>
            <td>{{ accesory.price }}</td>
            <td>{{ accesory.type }}</td>
            <td><input class="input is-small" type="text" placeholder="Ilość"/></td>
                   
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
import { storeToRefs } from 'pinia'

const store = useNewProjectStoreBeta()
const {accesorytype} = storeToRefs(store)



</script>