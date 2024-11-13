<template>
  <div class="elements-table-container">
      <table class="table is-bordered is-striped is-hoverable is-fullwidth">
        <thead>
          <tr>
            <th>{{ $t("name")}}</th>
            <th>{{ $t("length")}}</th>
            <th>{{ $t("width")}}</th>
            <th>{{ $t("thickness")}}</th>
            <th>{{ $t("wood_type")}}</th>
            <th>{{$t("quantity")}}</th>
            <th class="delete-column">{{$t("delete")}}</th>
            
          </tr>

        </thead>
        
        <tfoot>
          
          <tr>
            
          </tr>
        
        
        </tfoot>
        <tbody>
          <tr v-for="element in elements" :key="element.name">
            
            <th>{{ element.element.name }}</th>
            <td>{{ element.element.dimX }}</td>
            <td>{{ element.element.dimY }}</td>
            <td>{{ element.element.dimZ }}</td>
            <td>{{ element.element.wood_type.name }}</td>
            <td>{{ element.quantity }}</td>
            <td><b-button @click="deleteElement(element)" type="is-danger"><i class="fa-solid fa-xmark"></i></b-button></td>
          </tr>
        </tbody>
        
      </table>
    </div>
    
</template>

<script>
export default {
  name: 'ElementsTable', 
}
</script>


<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'

const store = useNewProjectStoreBeta()
const {deleteElement} = store

const props = defineProps({
  elements: Array,
  required: true
})




</script>
<style>
.delete-column {
  width: 10px; /* Adjust this width to fit your icon */
  text-align: center;
}

.delete-column b-button {
  padding: 0;
}</style>


