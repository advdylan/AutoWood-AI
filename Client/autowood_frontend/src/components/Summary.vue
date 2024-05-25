<template>
    <div class="columns">
        <div class="column is-two-thirds">
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                <thead>
                  <tr>
                    <th>Koszty elementów</th>
                    <th>Koszty akcesorii</th>
                    <th>Robocizna</th>
                    
                  </tr>
        
                </thead>
                
                <tfoot>
                  
                  <tr>
                    
                  </tr>
                               
                </tfoot>
                <tbody>
                  <tr v-for="data in summary" :key="summary.data">
                    
                    <th>{{ data.elements }}</th>
                            
                  </tr>
                </tbody>
                
              </table>
        </div>
        <div class="column">
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                <thead>
                  <tr>
                    <th>Name</th>
                    <th>Name</th>
                    
                  </tr>
        
                </thead>
                
                <tfoot>
                  
                  <tr>
                    
                  </tr>
                               
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
  import { storeToRefs } from 'pinia'
  
  const store = useNewProjectStoreBeta()
  
  const {elements, } = storeToRefs(store)




  
  </script>
  
  
  
  