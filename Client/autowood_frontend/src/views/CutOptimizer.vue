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
          <!-- INPUT LEFT SECTION -->

          <div class="box">
            <div class="label has-text is-size-5">{{$t('import_elements')}}</div>

            <div @click="showSearchModal= !showSearchModal" class="button is-info">{{ $t('search') }} &nbsp;<i class="fa-solid fa-magnifying-glass"></i></div>


          </div>

           
           
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

        <div v-if="OccupiedBoards.length" class="column has-text-centered" >
          <!-- SVG MIDDLE SECTION -->
          <div class="box is-fullwidth" style="overflow: hidden; text-align: center;">
          <svg 
              id="svgBoard" 
              xmlns="http://www.w3.org/2000/svg" 
              :viewBox="`0 0 ${boards[0].board.dimX} ${boards[0].board.dimY}`"
              preserveAspectRatio="xMidYMid meet" 
              style="width: 100%; height: 100%; border: 1px solid #ccc;">
              <!-- Example content -->
              <defs>
                <linearGradient id="occupiedBoardGrad" x1="0%" x2="100%" y1="0%" y2="0%">
                  <stop offset="0%" stop-color="rgb(205, 247, 205)" stop-opacity="0.3" />
                  <stop offset="100%" stop-color="rgb(205, 247, 205)" stop-opacity="0.8" />
                </linearGradient>
                <linearGradient id="FreeBoardGrad" x1="0%" x2="100%" y1="0%" y2="0%">
                  <stop offset="0%" stop-color="rgb(250, 237, 237)" stop-opacity="0.1" />
                  <stop offset="100%" stop-color="rgb(245, 230, 230)" stop-opacity="0.3" />
                </linearGradient>
              </defs>

              <rect v-for="format in OccupiedBoards"
              :x="format.start_x"
              :y="format.start_y"
              :width="format.X"
              :height="format.Y"
              style="fill:url(#occupiedBoardGrad);stroke-width:1;stroke:rgb(0,0,0)"          
              />
              <text v-for="textX in OccupiedBoards"
              :key="textX.id"
              :x="(textX.start_x) + (textX.X)/2"
              :y="textX.start_y + 30"
              fill="black"
              style="font-size: 30px;"
              text-anchor="middle"
              >{{ textX.X }} </text>

              <text v-for="textY in OccupiedBoards"
              :key="textY.id"
              :x="textY.start_x + 30"
              :y="(textY.start_y) + (textY.Y)/2"
              fill="black"
              style="font-size: 30px;"
              text-anchor="middle"
              :transform="'rotate(270 ' + (textY.start_x + 30) + ' ' + (textY.start_y + textY.Y / 2) + ')'"
              
              >{{ textY.Y }} </text>


              <rect v-for="format in FreeBoards"
              :x="format.start_x"
              :y="format.start_y"
              :width="format.X"
              :height="format.Y"
              style="fill:url(#FreeBoardGrad);stroke-width:0.2;stroke:rgb(0,0,0)"          
              />
             
    
          </svg>

          
        </div>

        <OptimizerFooter
        :free-boards = "FreeBoards">
        </OptimizerFooter>

        </div>



      </div>
      <div class="columns">
        <div class="column has-text-centered is-half" >
          <button  class="button is-success is-centered" @click="assignBoardToElement"></button>
          H A L O
        </div>
        <div class="column has-text-centered is-half" >
          
          H A L O 2
        </div>

      </div>

      

      
    </div>
  </div>
</div>
</div>


<!-- MODAL -->

<div class="modal" v-bind:class="{'is-active': showSearchModal}" id="newelement-modal" >
        <div class="modal-background"></div>
        <div class="modal-content" style="width: 1400px;">
            <div class="modal-card">
                <header class="modal-card-head">
                    <p class="modal-card-title is-centered is-size-4">{{ $t('search') }}</p>
                    <button class="delete" aria-label="close" @click="showSearchModal = false"></button>
                </header>
                <section class="modal-card-body" >

                  <ProjectsList
                  :search-modal="true"
                  @get-elements="copyElements"                 
                  ></ProjectsList>


                   
                </section>
            </div>
        </div>
    </div>


</template>




<script setup>
import {computed, ref} from 'vue'
import { useNewProjectStoreBeta } from '@/store/newproject'
import ElementsOptimizerTable from '@/components/OptimizerComponents/ElementsOptimizerTable.vue'
import BoardInput from '@/components/OptimizerComponents/BoardInput.vue'
import ProjectsList from './ProjectsList.vue'
import OptimizerFooter from '@/components/OptimizerComponents/OptimizerFooter.vue'
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
const DownloadedElements = ref([])

const showSearchModal = ref(false)

const errors = ref([])


loadData()

const newElement = ref({
  element: {
    name: 'Przód',
    dimX: 200,
    dimY: 250,
    dimZ: 25,
    wood_type: ''
  },
  quantity: 1
})


function copyElements(id) {
  console.log(id)

  try {
     axios
    .get(`api/v1/tools/new-project-elements/${id}/`)
    .then(response => {
      let data = response.data
      console.log(data)
      DownloadedElements.value = data

      for (let element of DownloadedElements.value) {
        elements.value.push({
              element: {
                name: element.element.name,
                dimX: element.element.dimX,
                dimY: element.element.dimY,
                dimZ: element.element.dimZ,
                wood_type: element.element.wood_type
              },
              quantity: element.quantity
            })
      }
      showSearchModal.value = false
     
      
    })
  } catch (error) {
    
  }
  
}

function assignBoardToElement() {

  for (let element of elements.value) {
    for (let i=0; i < element.quantity; i++) {
      console.log(element)
    }
  }

}

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
<style lang="css">

.modal-content
.modal-card {
  width: 90%;

}

</style>