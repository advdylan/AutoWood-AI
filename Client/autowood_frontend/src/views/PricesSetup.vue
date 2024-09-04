<template>

    <div class="columns">
        <div class="column is-one-third">
            <div class="card">
                <header class="card-header">
                  <p class="card-header-title is-centered">Koszty pracy</p>               
                </header>
                <div class="card-content">
                    <div class="columns">


                        <div class="column is-two-thirds">
                            <div v-for="worktime_name in worktimeCost" class="field">
                                <div class="control">
                                    <input  class="input" type="text" :placeholder="worktime_name.text" disabled/>
                                </div>
                            </div>

                        </div>

                        <div class="column">
                            <div v-for="worktime_value in worktimeCost" class="field">
                                <input class="input" type="text" placeholder="bind-to-" :value="worktime_value.value" :disabled="toggleDisabled"/>                                          
                            </div>
                        </div>
                    </div>
                    <div class="buttons">
                        <button class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>Dodaj dział</button>   
                        <button @click="toggleDisabled = !toggleDisabled" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj koszty pracy</button>                       
                    </div>
                </div>
              </div>

        </div>
        <div class="column is-one-third">
            
        </div>
        <div class="column is-one-third">
            
        </div>
    </div>



</template>
<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import axios from 'axios'
import { storeToRefs } from 'pinia';
import {ref} from 'vue'

const toggleDisabled = ref(true)

const mainstore = useNewProjectStoreBeta()

const {loadData} = mainstore
const {worktimeCost} = storeToRefs(mainstore)

loadData()



</script>