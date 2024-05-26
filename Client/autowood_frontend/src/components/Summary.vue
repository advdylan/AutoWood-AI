<template>
    <div class="columns">
        <div class="column is-one-quarter">
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                <thead>
                  <tr>
                    <th class="title is-size-5">Koszty elementów</th>        
                  </tr>    
                </thead>
                
                <tfoot>
   
                </tfoot>
                <tbody>
                  <th class="title is-size-5">Suma: {{ summElementCosts }} </th>
                  
                </tbody>
                
              </table>
        </div>
        <div class="column is-one-quarter">
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                <thead>
                  <tr>
                    <th class="title is-size-5">Koszty akcesorii</th>
                    </tr>
                </thead>
                
                <tfoot>

                               
                </tfoot>
                <tbody>
                  <th class="title is-size-5">Suma: {{ summAccesoriesCosts }} </th>
                            
                  
                </tbody>
                
              </table>
        </div>

        <div class="column is-one-quarter">
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                <thead>
                  <tr>
                    <th class="title is-size-5">Koszty pracy</th>
                    </tr>
                </thead>
                
                <tfoot>

                               
                </tfoot>
                <tbody>
                  <tr>
                    <tr v-for="worktime in worktimeCost">
                      <th> {{worktime.sum}}</th>
                    </tr>
                    
                  
                            
                  </tr>
                </tbody>
                
              </table>
        </div>

        <div class="column is-one-quarter">
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                <thead>
                  <tr>
                    <th class="title is-size-5">Marże</th>
                    </tr>
                </thead>
                
                <tfoot>

                               
                </tfoot>
                <tbody>
                  <tr v-for="data in summary" :key="summary.data">
                    
                    <th>{{ data.elements }}</th>
                            
                  </tr>
                </tbody>
                
              </table>
        </div>
    </div>

      
  </template>
  
  <script>
  export default {
    name: 'Summary'
  }
   
  </script>
  
  <script setup>
  import { useNewProjectStoreBeta } from '@/store/newproject'
  import { computed } from 'vue'
  import { storeToRefs } from 'pinia'
  
  const store = useNewProjectStoreBeta()
  

  const {elements, wood, pricedElements, accesoriesStore, worktimeCost} = storeToRefs(store)


  
 const summElementCosts = computed(() => {
  return pricedElements.value.reduce((n, {price}) => n + parseFloat(price), 0)
  
 })
 
 const summAccesoriesCosts = computed(() => {
  return accesoriesStore.value.reduce((n, {sum}) => n + parseFloat(sum), 0)
 })











  
  </script>
  
  
  
  