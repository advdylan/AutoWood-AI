<template>
    <div class=columns >
        <div class="column is-full">
       
        <div class="container">
          <div class="notification is-text">
            <div class="title is-centered is-size-4">
              Dział zarządzania akcesoriami     
            </div>
            <div class="text">
              Każdorazowa zmiana poniższych kosztów akcesorii nie działa wstecz. Tylko nowe projekty otrzymają nowe, poniższe wartości.
            </div>
          </div>
        </div>
        </div>
      </div>

      <div class="column">

        <div class="card">
            <header class="card-header">
              <p class="card-header-title is-centered is-size-4">Dodaj nowe akcesoria
                <span>&nbsp;<i class="fa-solid fa-plus"></i></span>
              </p>
              
            </header>
            <div class="card-content">
              <div class="content">
                
                
                            
                </div>
              </div>
            </div>               
        </div>

        <div class="column">

            <div class="card">
                <header class="card-header">
                  <p class="card-header-title is-centered is-size-4">Akcesoria
                    <span>&nbsp;<i class="fa-solid fa-screwdriver-wrench fa-lg"></i></span>
                  </p>
                  
                </header>
                <div class="card-content">
                  <div class="content">
                    <div class="projects-list-container">
                        <b-table :data="accesorytype"
                        :paginated="isPaginated"
                        :per-page="perPage"
                        :current-page.sync="currentPage"
                        :pagination-simple="isPaginationSimple"
                        :pagination-position="paginationPosition"
                        :default-sort-direction="defaultSortDirection"
                        :pagination-rounded="isPaginationRounded"
                        :sort-icon="sortIcon"
                        :sort-icon-size="sortIconSize"
                        default-sort="user.first_name"
                        aria-next-label="Next page"
                        aria-previous-label="Previous page"
                        aria-page-label="Page"
                        aria-current-label="Current page"
                        :page-input="hasInput"
                        :pagination-order="paginationOrder"
                        :page-input-position="inputPosition"
                        :debounce-page-input="inputDebounce">
                            <template v-for="column in columns" :key="column.id">
                                <b-table-column v-bind="column">
                                    <template v-if="column.searchable && !column.numeric" #searchable="props">
                                        <b-input
                                            v-model="props.filters[props.column.field]"
                                            placeholder="Wyszukaj"
                                            icon="magnify"/>
                                    </template>
                                    <template v-slot="props">
                                        
                                        <template v-if="column.field === 'nawigacja'">
                                            <router-link :to="{ name: 'NewProjectDetail', params: { id: props.row.id } }">
                                                <b-button icon-right="circle-info">Szczegóły</b-button>                               
                                            </router-link>
                                            
                                        </template>
                                        <template v-else>
                                        {{ props.row[column.field] }}
                                    </template>
                                </template>
                                </b-table-column>
                            </template>
                        </b-table>
                    </div>
                    
                    
                                
                    </div>
                  </div>
                </div>               
            </div>

        

</template>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'
import { onMounted, ref, watch, computed } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'

import AccessoryTable from '@/components/AccessoryTable.vue'


const newProjectStore = useNewProjectStoreBeta()
const data = ref([])
let isPaginated = true
let isPaginationSimple = true
let isPaginationRounded = false
let paginationPosition = 'bottom'
let defaultSortDirection = 'asc'
let sortIcon= 'arrow-up'
let sortIconSize= 'is-small'
let currentPage= 1
let perPage= 5
let hasInput= false
let paginationOrder= ''
let inputPosition= ''
let inputDebounce= ''
const {loadData} = newProjectStore
const {accesories, accesorytype} = storeToRefs(newProjectStore)



let columns = [
    { 
    field: 'name', 
    label: 'Nazwa',
    searchable: true
    },
    { 
    field: 'type', 
    label: 'Typ',
    searchable: true 
    },
    { 
    field: 'weight', 
    label: 'Waga',
    searchable: true
    },
    { 
    field: 'price', 
    label: 'Cena',
    searchable: true 
    },
    {
    field: 'nawigacja',
    label: 'Nawigacja'
    }
]

onMounted(() => {
    loadData()
    
})

</script>


<style>

</style>