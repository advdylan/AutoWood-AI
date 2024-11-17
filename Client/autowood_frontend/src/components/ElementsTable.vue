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


    <b-table :data="elements" :columns="columns">
      <template v-for="(column, index) in columns" :key="column.id">
        <b-table-column v-bind="column">
          <template v-slot="props">
            <template v-if="column.label === 'nav'">
              <b-button @click="deleteElement(props.row)" type="is-danger" icon-left="x">X</b-button>
          </template>
          
          </template>

        </b-table-column>

        
              
          
        
      </template>
      
    </b-table>
  
    
</template>

<script>
export default {
  name: 'ElementsTable', 
}
</script>


<script setup>
import { computed } from 'vue'
import { useNewProjectStoreBeta } from '@/store/newproject'
import { useI18n } from 'vue-i18n';

const store = useNewProjectStoreBeta()
const {deleteElement} = store

const props = defineProps({
  elements: Array,
  required: true
})

const { t } = useI18n();
 
const columns = computed(() => [
  {
    field: 'element.name',
    label: t('name'), 
    
    sortable: true,
  },
  {
    field: 'element.dimX',
    label: t("length"), 
    
    sortable: true,
  },
  {
    field: 'element.dimY',
    label: t("width"), 
   
    sortable: true,
  },
  {
    field: 'element.dimZ',
    label: t('thickness'), 
    
    sortable: true,
  },
  {
    field: 'element.wood_type.name',
    label: t('wood_type'),
    
    sortable: true,
  },
  {
    field: 'quantity',
    label: t('quantity'), 
    sortable: true,
  },
  {
    field: 'nav',
    label: t('Nav'), 
    sortable: true,
  },
  
])



</script>
<style>
.delete-column {
  width: 10px; 
  text-align: center;
}

.delete-column b-button {
  padding: 0;
}</style>


