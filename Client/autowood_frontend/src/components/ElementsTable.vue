<template>
      <table class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>Name</th>
            <th>Długość</th>
            <th>Wysokość</th>
            <th>Grubość</th>
            <th>Materiał</th>
            <th>Ilość</th>
          </tr>

        </thead>
        
        <tfoot>
          
          <tr>
            
          </tr>
        
        
        </tfoot>
        <tbody>
          <tr v-for="element in elements" :key="element.name">
            
            <th>{{ element.name }}</th>
            <td>{{ element.dimX }}</td>
            <td>{{ element.dimY }}</td>
            <td>{{ element.dimZ }}</td>
            <td>{{ element.wood_type }}</td>
            <td>{{ element.quantity }}</td>         
          </tr>
        </tbody>
        
      </table>
    
</template>

<script>
export default {
  name: 'ElementsTable'
}

</script>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'

const store = useNewProjectStoreBeta()

const {elements} = storeToRefs(store)

</script>



