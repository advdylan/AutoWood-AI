<template>
    <div class="columns">
        <div class="column is-half">





          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Suma kosztów</p>
    
            </header>
            <div class="card-content">
              <div class="content">
                

                <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                  <thead>
                    <tr>
                      <th class="title is-size-6">Koszty elementów</th>        
                    </tr>    
                  </thead>
                  
                  <tfoot>
     
                  </tfoot>
                  <tbody>
                    <th class="title is-size-6">Suma: {{ summElementCosts }} zł </th>
                    
                  </tbody>
                  
                </table>
  
                <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                  <thead>
                    <tr>
                      <th class="title is-size-6">Koszty akcesorii</th>
                      </tr>
                  </thead>
                  
                  <tfoot>
  
                                 
                  </tfoot>
                  <tbody>
                    <th class="title is-size-6">Suma: {{ summAccesoriesCosts }} zł </th>
                              
                    
                  </tbody>
                  
                </table>
  
                <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                  <thead>
                    <th class="title is-size-6">Dział</th>
                    <th class="title is-size-6">Czas</th>
                    <th class="title is-size-6">Stawka</th>
                    <th class="title is-size-6">Suma</th>

                  </thead>
                 
   
                  <tbody>
  
                      <tr v-for="worktime in worktimeCost">
                        <th> {{worktime.text}}</th>
                        <th> {{worktime.hours}} h</th>
                        <th> {{worktime.value}} zł/h</th>
                        <th> {{worktime.sum}} zł</th>
                        
                      </tr>
                      <tr>
                        <th>Suma </th>
                      </tr>

                  </tbody>

                  
                  
                </table>
          </div>
          
              </div>
            </div>
          
          </div>



        <div class="column">
          <div class="card">
            <header class="card-header">
              <p class="card-header-title">Component</p>           
            </header>
            <div class="card-content">
              <div class="content">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec
                iaculis mauris.
                <a href="#">@bulmaio</a>. <a href="#">#css</a> <a href="#">#responsive</a>
                <br />
                <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
              </div>
            </div>
            <footer class="card-footer">
              <a href="#" class="card-footer-item">Save</a>
              <a href="#" class="card-footer-item">Edit</a>
              <a href="#" class="card-footer-item">Delete</a>
            </footer>
          </div>
            
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

 console.log(worktimeCost.value)










  
  </script>
  
  
  
  