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
                      <th v-if="marginA"> Marża na materiał : {{ parseFloat(elementsMargin).toFixed(2) }}
                      
                      </th>
                    </tr>
                    <tr>
                      <th v-if="marginB"> Marża na akcesoria: {{ parseFloat(accesoriesMargin).toFixed(2)}}</th>
                    </tr>
                    <tr>
                      <th v-if="marginC">Marża dodatkowa: {{ parseFloat(additionalMargin).toFixed(2) }}</th>
                    </tr>
                    <tr>
                      <th v-if="marginC || marginB || marginA">Suma z marżami: {{ parseFloat(summaryCostsWithMargin).toFixed(2) }}</th>
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
              <p class="card-header-title is-size-5">Marże wyrażane w %</p>           
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
                  <label  class="label">Marża dodatkowa <strong class="is-underlined">(Dotyczy wszystkich elementów wyceny)</strong></label>
                  <div class="control">
                    <input v-model="marginC" class="input" type="text" placeholder="Marża wyrażana w %">                  
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
  import { useSummaryStore } from '@/store/summary'
  import { computed, ref, watch, watchEffect } from 'vue'
  import { storeToRefs } from 'pinia'
  
  const marginA = ref()
  const marginB = ref()
  const marginC = ref()

  const props = defineProps({
    propMarginA: Number,
    propMarginB: Number,
    propMarginC: Number
  })

  if (props) {
    console.log(props.propMarginA)
    
  }


  const store = useNewProjectStoreBeta()
  const summaryStore = useSummaryStore()
  

  const {elements, wood, pricedElements, accesoriesStore, worktimeCost} = storeToRefs(store)


  
 const summElementCosts = computed(() => {
  return pricedElements.value.reduce((n, {price}) => n + parseFloat(price), 0).toFixed(2)
  
 })
  
 const summAccesoriesCosts = computed(() => {
  return accesoriesStore.value.reduce((n, {sum}) => n + parseFloat(sum), 0).toFixed(2)
 })

const summWorktimeCosts = computed(() => {
  return worktimeCost.value.reduce((n, {sum}) => n + parseFloat(sum), 0).toFixed(2)
  
})

const summaryCosts = computed(() => {
  return parseFloat(summWorktimeCosts.value) + parseFloat(summElementCosts.value) + parseFloat(summAccesoriesCosts.value)
})

const elementsMargin = computed(() => {
  let margin = ((parseFloat(summElementCosts.value) * parseInt(marginA.value)) / 100)
  return margin
})

const accesoriesMargin = computed(() => {
  let margin = ((parseFloat(summAccesoriesCosts.value) * parseInt(marginB.value)) / 100)
  return margin
})

const additionalMargin = computed(() => {
  let margin = ((parseFloat(summWorktimeCosts.value)+ parseFloat(summElementCosts.value) + parseFloat(summAccesoriesCosts.value)) * parseInt(marginC.value) / 100)
  return margin
})

const summaryCostsWithMargin = computed(() => {
  let sum = ((parseFloat(summaryCosts.value) + parseFloat(elementsMargin.value || 0) + parseFloat(accesoriesMargin.value || 0) + parseFloat(additionalMargin.value || 0)))
  return sum

})

watchEffect(() => {
summaryStore.setSummaryCosts(summaryCosts.value)
summaryStore.setElementsMargin(elementsMargin.value)
summaryStore.setAccesoriesMargin(accesoriesMargin.value)
summaryStore.setAdditionalMargin(additionalMargin.value)
summaryStore.calculateSummaryCostsWithMargin(summaryCostsWithMargin.value)
})


  </script>
  
  
  
  