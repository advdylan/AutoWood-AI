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
                  <tr v-for="element in pricedElements" :key="pricedElements.name">
                    
                    <th>{{ element.price }}</th>
                            
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
  const { elementsPrice } = store

  const pricedElements = elementsPrice()



  

  const {elements, wood} = storeToRefs(store)

 
 



  
  </script>
  
  
  
  