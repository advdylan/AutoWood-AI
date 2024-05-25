<template>
    <div class="columns">
        <div class="column is-one-quarter">
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                <thead>
                  <tr>
                    <th class="title is-size-5">Koszty elementów</th> 
                    <button @click="elementsPrice" class="button">Button</button>
                        
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
                  <tr v-for="data in summary" :key="summary.data">
                    
                    <th>{{ data.elements }}</th>
                            
                  </tr>
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
                  <tr v-for="data in summary" :key="summary.data">
                    
                    <th>{{ data.elements }}</th>
                            
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
  import { storeToRefs } from 'pinia'
  
  const store = useNewProjectStoreBeta()
  
  const {elements, wood} = storeToRefs(store)

  function elementsPrice() {
    if(elements) {
        console.log(elements.value[0].dimX)
    }
  }
 
elementsPrice()



  
  </script>
  
  
  
  