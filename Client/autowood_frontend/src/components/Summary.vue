<template>
    <div class="columns">
        <div class="column is-half">





          <div class="card">
            <header class="card-header">
              <p class="card-header-title is-size-5">Suma kosztów</p>
    
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
                        <th></th>
                        <th></th>
                        <th> {{ summWorktimeCosts }} zł</th>
                      </tr>
                  </tbody>
                </table>

                <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                  <thead>
                    <tr>
                      <th class="title is-size-6">Łącznie</th>        
                    </tr>    
                  </thead>
                  <tbody>
                    <tr>
                      <th> Suma: {{ summaryCosts}}</th>
                    </tr>
                    <tr>
                      <th v-if="marginA"> Suma z marżą materiałową : {{ parseFloat(summaryCostsWithMarginA).toFixed(2) }}</th>
                      <th v-if="marginB"> Suma z marżą na akcesoria: {{ parseFloat(summaryCostsWithMarginB).toFixed(2)}}</th>
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
              <p class="card-header-title is-size-5">Marże</p>           
            </header>
            <div class="card-content">
              <div class="content">
                <div class="field">
                  <label class="label">Marża materiałowa</label>
                  <div class="control">
                    <input v-model="marginA" class="input" type="text" placeholder="Marża wyrażana w %">                  
                  </div>
                  <label class="label">Marża akcesorii</label>
                  <div class="control">
                    <input v-model="marginB" class="input" type="text" placeholder="Marża wyrażana w %">                  
                  </div>
                  <label class="label">Marża dodatkowa</label>
                  <div class="control">
                    <input class="input" type="text" placeholder="Marża wyrażana w %">                  
                  </div>
                </div>
              </div>
            </div>
            <footer class="card-footer">


             
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
  import { computed, ref } from 'vue'
  import { storeToRefs } from 'pinia'
  
  const marginA = ref()
  const marginB = ref()


  const store = useNewProjectStoreBeta()
  

  const {elements, wood, pricedElements, accesoriesStore, worktimeCost} = storeToRefs(store)


  
 const summElementCosts = computed(() => {
  return pricedElements.value.reduce((n, {price}) => n + parseFloat(price), 0)
  
 })
 
 const summAccesoriesCosts = computed(() => {
  return accesoriesStore.value.reduce((n, {sum}) => n + parseFloat(sum), 0)
 })

const summWorktimeCosts = computed(() => {
  return worktimeCost.value.reduce((n, {sum}) => n + parseFloat(sum), 0)
  
})

const summaryCosts = computed(() => {
  return parseFloat(summWorktimeCosts.value) + parseFloat(summElementCosts.value) + parseFloat(summAccesoriesCosts.value)
})

const summaryCostsWithMarginA = computed(() => {
  let margin = ((parseFloat(summElementCosts.value) * parseInt(marginA.value)) / 100)
  return summaryCosts.value + margin
})

const summaryCostsWithMarginB = computed(() => {
  let margin = ((parseFloat(summAccesoriesCosts.value) * parseInt(marginB.value)) / 100)

})
  
  </script>
  
  
  
  