<template>
  
  <section class="hero is-primary is-small">
  <div class="hero-body">
    <p class="title">Elementy</p>

  </div>
</section>


  <div v-if="elements.length">
  <b-table :key="tableKey" :data="elements" :paginated="isPaginated" :per-page="perPage" :current-page.sync="currentPage" :pagination-simple="isPaginationSimple" :pagination-position="paginationPosition" :default-sort-direction="defaultSortDirection" :pagination-rounded="isPaginationRounded" :sort-icon="sortIcon" :sort-icon-size="sortIconSize" default-sort="user.first_name" aria-next-label="Next page" aria-previous-label="Previous page" aria-page-label="Page" aria-current-label="Current page" :page-input="hasInput" :pagination-order="paginationOrder" :page-input-position="inputPosition" :debounce-page-input="inputDebounce">

  <b-table-column :label="$t('name')"> 
    <template v-if="editMode" #default="props">
      <b-input  v-model="props.row.element.name"/>
    </template> 
    <template v-else #default="props">
      {{ props.row.element.name }}
    </template>
  </b-table-column>

  <b-table-column :label="$t('length')">
    <template v-if="editMode" #default="props">
      <b-input  v-model="props.row.element.dimX"/>
    </template> 
    <template #default="props">
      {{ props.row.element.dimX }}
    </template>
  </b-table-column>

  <b-table-column :label="$t('width')">
    <template v-if="editMode" #default="props">
      <b-input  v-model="props.row.element.dimY"/>
    </template> 
    <template #default="props">
      {{ props.row.element.dimY }}
    </template>
  </b-table-column>
  
  <b-table-column :label="$t('thickness')">
    <template v-if="editMode" #default="props">
      <b-input  v-model="props.row.element.dimZ"/>
    </template> 
    <template #default="props">
      {{ props.row.element.dimZ }}
    </template>
  </b-table-column>

  <b-table-column :label="$t('wood_type')">
    <template v-if="editMode" #default="props">
      <b-select v-model="props.row.element.wood_type" :placeholder="$t('wood_type')">
        <option
          v-for="woodItem in wood"
          :value="woodItem"
          :key="woodItem.id">
        {{ woodItem.name }}</option>
      </b-select>
    </template>

    <template #default="props">
      {{ props.row.element.wood_type.name }}
    </template>
  </b-table-column>

  <b-table-column :label="$t('quantity')">
    <template v-if="editMode" #default="props">
      <b-input  v-model="props.row.quantity"/>
    </template> 
    <template #default="props">
      {{ props.row.quantity }}
    </template>
  </b-table-column>

  <b-table-column :label="$t('Nav')">
    <template #header>
      <b-switch v-model="editMode">
        Edit
      </b-switch>
    </template>
  <b-button @click="handleDeleteButton(props.row)" type="is-danger" icon-left="x">    
  </b-button>


  </b-table-column>
</b-table>                            
</div>

</template>



<script>
export default {
  name: 'ElementsTable', 
}
</script>


<script setup>
import { computed, ref } from 'vue'
import { useNewProjectStoreBeta } from '@/store/newproject'
import { useI18n } from 'vue-i18n';
import { storeToRefs } from 'pinia';

const store = useNewProjectStoreBeta()
const { elements,wood} = storeToRefs(store)
const {deleteElement} = store

//table variables
const editMode = ref(false)
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
const tableKey = ref(0)

const props = defineProps({
  elements: Array,
  default: () => [],
  required: true
})

const { t } = useI18n();

console.log("Elements Data:", elements);

function getNestedValue(obj, path) {
  return path.split('.').reduce((acc, part) => acc && acc[part], obj);
}

const columns = computed(() => [
  { field: 'element.name', label: t('name'), sortable: true, searchable: true, },
  { field: 'element.dimX', label: t("length"), sortable: true, searchable: true, },
  { field: 'element.dimY', label: t("width"), sortable: true, searchable: true, },
  { field: 'element.dimZ', label: t('thickness'), sortable: true, searchable: true, },
  { field: 'element.wood_type.name', label: t('wood_type'), sortable: true, searchable: true, },
  { field: 'quantity', label: t('quantity'), sortable: true },
  { field: 'nav', label: 'nav', sortable: false, centered: true },
]);



</script>
<style>
.delete-column {
  width: 10px; 
  text-align: center;
}

.delete-column b-button {
  padding: 0;
}</style>


