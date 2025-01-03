<template>
<div class="card">
  <header class="card-header">
    <p class="card-header-title"> {{ $t('cut-optimizer') }}</p>

  </header>

  <div class="card">
  <div class="card-content">
    <div class="content">
      <div class="columns">

        <div class="column has-text-centered is-one-third">

        <div class="box">
        <div class="label has-text is-size-5">{{$t('elements_list')}}</div>
          <ElementsOptimizerTable></ElementsOptimizerTable>
        </div>

        <div class="box">
        <div class="label has-text is-size-5">{{$t('boards')}}</div>
        <BoardInput></BoardInput>
        </div>

        <button @click="generateBoardWithElements()" v-if="elements.length" style="width: 50%;" class="button is-success is-centered">{{ $t('generate') }}</button>  
        </div>

        <div class="column">
            
        </div>

        




      </div>
    </div>
  </div>
</div>
</div>


</template>




<script setup>
import {ref} from 'vue'
import { useNewProjectStoreBeta } from '@/store/newproject'
import ElementsOptimizerTable from '@/components/ElementsOptimizerTable.vue'
import BoardInput from '@/components/BoardInput.vue'
import { storeToRefs } from 'pinia'
import axios from 'axios'
import { toast } from 'bulma-toast'
import { useI18n } from 'vue-i18n';

const newProjectStore = useNewProjectStoreBeta()
const {elements,boards} = storeToRefs(newProjectStore)
const {loadData } = newProjectStore
const { t } = useI18n()

const FreeBoards = ref([])
const OccupiedBoards = ref([])
const ElementsOmmited = ref([])

const errors = ref([])


loadData()

const newElement = ref({
  element: {
    name: 'Przód',
    dimX: 2500,
    dimY: 250,
    dimZ: 25,
    wood_type: ''
  },
  quantity: 1
})

async function generateBoardWithElements() {

  const combined = [
  ...boards.value.map((board) => ({ type: "board", ...board })),
  ...elements.value.map((element) => ({ type: "element", ...element })),
];

 
  

  if (!errors.value.length) {

try{
  await axios
  .post(`/api/v1/tools/cut-optimizer/`, combined ,{
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => {
        
        let data = response.data
        if (data){
          FreeBoards.value = data.free_boards
          ElementsOmmited.value = data.formats_ommited,
          OccupiedBoards.value = data.occupied_boards
        }
        return true   
      })
  .catch(error => {
    //console.log(JSON.stringify(response.data))  
    console.log(error)
    return false
  })
} 

catch (error) {
  console.error('Error saving the project:', error)
  
}
toast({
        message: t('save_msg'),
        duration: 5000,
        position: "top-center",
        type: 'is-success',
        animate: { in: 'backInDown', out: 'backOutUp' },
      })
} 

else {
    let msg = ''

    for (let i=0; i <errors.value.length; i++){
      msg += errors.value[i] += "\n"
    }
    toast({
        message: msg,
        duration: 5000,
        position: "top-center",
        type: 'is-danger',
        animate: { in: 'backInDown', out: 'backOutUp' },
      })

      errors.value = []
    }


}

</script>
<style lang="scss">

</style>