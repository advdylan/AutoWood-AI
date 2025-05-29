<template>
    <div class="card-content">
                            <div class="content">

                              
                              <div class="columns">
                                <div class="column is-half">
                                <div class="box">
                                  <label class="label is-size-6">Dodaj etapy produkcyjne</label>

                                  <form @submit.prevent="submitForm">


                                  
                                  <div class="field">
                                    <div class="control">
                                      <input 
                                      class="input is-small" 
                                      type="text" 
                                      placeholder="Nazwa"
                                      v-model="newStageName"/>
                                    </div>
                                  </div>
                                  <div class="field">
                                    <div class="control">
                                      <input 
                                      class="input is-small
                                      " 
                                      type="text" 
                                      placeholder="Skrót"
                                      v-model="newStageShortcut"/>
                                    </div>
                                  </div>
                                  <button @click="updateProductionStages(productionSteps)" type="submit" class="button is-success">{{ $t("add")}}</button>
                                  </form>
                                </div>
                             

                                  
                                </div>
                                <div class="column is-half">
                                  <div class="box"> 
                                  <label class="label is-size-6">Etapy</label>
                                    <table class="table is-bordered is-striped">
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
                                                <button @click="deleteNewStage(step), updateProductionStages(productionSteps)" class="button is-danger is-small"><i class="fa-solid fa-trash"></i></button>
                                         
                                            </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                  </div>
                                    

                                </div>

                                
                                
                                

                              </div>
                              <div class="box">
                              <label class="label is-size-6">Etapy</label>
                                    <table class="table is-bordered is-striped">
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
                            </div>


</template>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'
import { ref, watch, computed, watchEffect, onMounted } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'
import { validateNewStage } from '@/validators/Validators'

const newProjectStore = useNewProjectStoreBeta()
const {getProductionSteps, addNewStage, deleteStage, deleteNewStage} = newProjectStore
const {productionSteps, chosenProductionSteps, deletedIDs} = storeToRefs(newProjectStore)

const newStageName = ref('')
const newStageShortcut = ref('')
const errors = ref([])

const props = defineProps({
  productionSteps: Array
})

function submitForm(){
  validateNewStage(newStageName,newStageShortcut, errors);

  if (!errors.value.length) {
    alert('Udalo sie ')
    let newStage = {
      stage_name: newStageName,
      shortcut: newStageShortcut      
    }
    productionSteps.value.push(newStage)
  }
  else {
    
    for (let error of errors.value) {
      let msg = ''
      msg += error += "\n"
      toast({
      message: msg,
      duration: 5000,
      position: "top-center",
      type: 'is-danger',
      animate: { in: 'backInDown', out: 'backOutUp' },
    })
    }
  }

}

function updateStages(data) {

    console.log(data)
      try {
          let response =  axios.post(`api/v1/production/update-production-stages/`, {
            data: data,
            deletedIDs: deletedIDs.value
          },
          {
            headers: {
              'Content-Type': 'application/json',
            },
          })
          console.log('Server response:', response)
          console.log('Project updated successfully:', response.data)
    } catch (error) {
          console.error('Error saving the project:', error)
    }

}

function updateProductionStages(value) {

  let timeoutId = setTimeout(function() {
        console.log(`Update notes fired value: ${JSON.stringify(value)}'`)
        updateStages(value)

    }, 3000)

}


watch(
  () => props.productionSteps,
  (newVal) => {
    chosenProductionSteps.value = newVal || []
  },
  { immediate: true }
)


onMounted(() => {
    getProductionSteps()
})

</script>

<style lang="css">
.button.is-small {
    padding: 0.25rem 0.5rem; 
    font-size: 0.75rem; 
}

td.has-text-centered {
    display: flex;
    justify-content: center;
    align-items: center; 
}
</style>