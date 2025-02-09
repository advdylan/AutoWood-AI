<template>
    <div class="card-content">
                            <div class="content">
                              <div class="columns">
                                <div class="column is-half">
                                <div class="box">
                                  <label class="label is-size-6">Dodaj etapy produkcyjne</label>
                                  
                                  <div class="field">
                                    <div class="control">
                                      <input 
                                      class="input" 
                                      type="text" 
                                      placeholder="Nazwa"/>
                                    </div>
                                  </div>
                                  <div class="field">
                                    <div class="control">
                                      <input 
                                      class="input" 
                                      type="text" 
                                      placeholder="Skrót"/>
                                    </div>
                                  </div>
                                </div>

                                  
                                </div>
                                <div class="column is-half">
                                  <label class="label is-size-6">Etapy</label>
                                    <table class="table is-bordered">
                                        <thead>
                                            <tr>
                                                <th>{{ $t('name') }}</th>
                                                <th>{{ $t('shortcut') }}</th>
                                                <th></th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="step in productionSteps">
                                            <td>{{ step.stage_name }}</td>
                                            <td>{{ step.shortcut }}</td>
                                            <td>
                                                <button @click="addNewStage(step)" class="button is-success is-small"><i class="fa-solid fa-plus"></i></button>
                                            </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    

                                </div>

                                
                                
                                

                              </div>
                              <label class="label is-size-6">Etapy</label>
                                    <table class="table is-bordered">
                                        <thead>
                                            <tr>
                                                <th>{{ $t('name') }}</th>
                                                <th>{{ $t('shortcut') }}</th>
                                                <th></th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="step in chosenProductionSteps">
                                            <td>{{ step.stage_name }}</td>
                                            <td>{{ step.shortcut }}</td>
                                            <td>
                                                <button @click="deleteStage(step)" class="button is-danger is-small"><i class="fa-solid fa-trash"></i></button>
                                            </td>
                                            </tr>
                                        </tbody>
                                    </table>

                            </div>
                            </div>


</template>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'
import { ref, watch, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'

const newProjectStore = useNewProjectStoreBeta()
const {getProductionSteps, addNewStage, deleteStage} = newProjectStore
const {productionSteps, chosenProductionSteps} = storeToRefs(newProjectStore)



onMounted(() => {
    getProductionSteps()

})

</script>

<style lang="css">
.button.is-small {
    padding: 0.25rem 0.5rem; /* Adjust padding to make the button smaller */
    font-size: 0.75rem; /* Adjust font size to make the text smaller */
}

td.has-text-centered {
    display: flex;
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
}
</style>