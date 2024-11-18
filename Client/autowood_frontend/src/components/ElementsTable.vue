<template>
<div v-if="elements.length">
<b-table :key="tableKey" :data="elements" :paginated="isPaginated" :per-page="perPage" :current-page.sync="currentPage" :pagination-simple="isPaginationSimple" :pagination-position="paginationPosition" :default-sort-direction="defaultSortDirection" :pagination-rounded="isPaginationRounded" :sort-icon="sortIcon" :sort-icon-size="sortIconSize" default-sort="user.first_name" aria-next-label="Next page" aria-previous-label="Previous page" aria-page-label="Page" aria-current-label="Current page" :page-input="hasInput" :pagination-order="paginationOrder" :page-input-position="inputPosition" :debounce-page-input="inputDebounce">
                            <template v-for="(column, index) in columns" :key="column.id">
                                <b-table-column v-bind="column">
                                    <template v-if="column.searchable && !column.numeric" #searchable="props">
                                        <b-input v-model="props.filters[props.column.field]" :placeholder="$t('search')" icon="magnify"/>
                                    </template>
                                    <template v-if="column.field === 'nav'" #header>
                                    <b-switch v-model="editMode">
                                        {{  $t('edit_mode') }}
                                    </b-switch>
                                    </template>
                                    <template v-slot="props">
                                        <template v-if="column.field === 'nav'">
                                            <b-button @click="handleDeleteButton(props.row)" type="is-danger" icon-left="x">
                                                
                                            </b-button>
                                        </template>
                                        
                                        <template v-if="editMode && column.searchable">
                                            <b-input @input="markAsEdited(props.row)"  v-model="props.row[column.field]"></b-input>
                                        </template>
                                        <template v-else>
                                          {{ getNestedValue(props.row, column.field) || 'N/A' }}
                                        </template>

                                    </template>
                                </b-table-column>

                            </template>
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
const { elements} = storeToRefs(store)
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
  { field: 'nav', label: 'nav', sortable: false },
]);

console.log('Columns:', columns.value); // Debugging

console.log("Columns:", columns);

</script>
<style>
.delete-column {
  width: 10px; 
  text-align: center;
}

.delete-column b-button {
  padding: 0;
}</style>


