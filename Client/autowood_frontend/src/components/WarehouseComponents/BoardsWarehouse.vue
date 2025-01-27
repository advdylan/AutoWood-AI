<template>
  
        <div  style="overflow: hidden; text-align: center;">
            <svg 
                :class="{ 'data-ready': isReady }"
                id="svgBoard" 
                xmlns="http://www.w3.org/2000/svg" 
                :viewBox="`0 -40 ${diagramWidth} ${diagramHeight+80}`"
                preserveAspectRatio="xMinYMin meet" 
                style="width: 100%; height: 100%;"
                
                >
                <defs>
                <linearGradient id="Buk" x1="0%" x2="0%" y1="100%" y2="0%">
                    <stop offset="0%" stop-color="rgb(192, 153, 153)" stop-opacity="0.9" />
                    <stop offset="100%" stop-color="rgb(192, 153, 153)" stop-opacity="1" />
                </linearGradient>
                <linearGradient id="Sosna" x1="0%" x2="0%" y1="100%" y2="0%">
                  <stop offset="0%" stop-color="rgb(237, 198, 152)" stop-opacity="0.9" />
                  <stop offset="100%" stop-color="rgb(237, 198, 152)" stop-opacity="1" />
                </linearGradient>
                <linearGradient id="Dąb" x1="0%" x2="0%" y1="100%" y2="0%">
                  <stop offset="0%" stop-color="rgb(124, 95, 53)" stop-opacity="0.9" />
                  <stop offset="100%" stop-color="rgb(124, 95, 53)" stop-opacity="1" />
                </linearGradient>
                </defs>
                

                <!-- AXES -->


                    <!-- TEXT -->
                 <text v-for="tick in ticks"
                 x="2.5%"
                 :y="diagramHeight - tick[0]"
                 >{{ Math.trunc(tick[1]) }}</text>
                 
                    <!--HORIZONTAL LINES-->

                  
                  <line
                    v-for="(tick, index) in ticks"
                    :key="tick[0]"
                    :x1="'5%'"
                    :x2="'90%'"
                    :y1="diagramHeight - tick[0]"
                    :y2="diagramHeight - tick[0]"
                    style="stroke: black; stroke-width: 0.2;"
                  ></line>

                  <g :key="chosenWoodType">
                  <rect v-for="(board) in processedBoards"
                  @click="highlightRow(board)"
                  :key=board.key
                  :width=diagramBarsWidth
                  :height=board.height 
                  :x=board.x
                  :y=board.y
                  :style="{
                    fill: `url(#${board.wood_type.name})`,
                    strokeWidth: highlightedRows.has(board) ? '2px' : '0px',
                    stroke: highlightedRows.has(board) ? 'rgb(65, 149, 244)' : 'red',
                    strokeDasharray: 10
                  }">
                  </rect>
                  </g>
                  <g :key="chosenWoodType">
                    <text
                      v-for="(board) in processedBoards"
                      :x= "(board.x + (diagramBarsWidth/2))"
                      :y=diagramHeight+30
                      text-anchor="middle"
                      font-size="11px"
                      >
                      {{ board.name }} ({{ board.dimX }}x{{ board.dimY }})
                      
                    </text>
                  </g>
            </svg>
        </div>

        
</template>
<script setup>
import {computed, onMounted, ref, watch} from 'vue'
import { useNewProjectStoreBeta } from '@/store/newproject'

import { storeToRefs } from 'pinia'
import axios from 'axios'
import { toast } from 'bulma-toast'
import { useI18n } from 'vue-i18n';
import 'animate.css'

const diagramWidth = ref(1000)
const diagramHeight = ref(500)
const diagramTicks = ref(null)
const warehouseCapacity = ref(null)
const isReady = ref(false)
const isRendered = ref(false)
const barsQuantity = ref(null)
const spacesBetweenBars = ref(null)
const woodType = ref('')


const props = defineProps({
    warehouseCapacity: Number,
    diagramTicks: Number,
    woodType: String
}
)

const newProjectStore = useNewProjectStoreBeta()
const {elements,boards, warehouseBoards, filteredBoards, chosenWoodType, highlightedRows, chosenThicknesses} = storeToRefs(newProjectStore)
const {loadBoards, highlightRow} = newProjectStore

loadBoards()


const ticks= computed(() => {

        const ticks= [[0,0]]
        let oneTick = diagramHeight.value / diagramTicks.value
        let newTick = oneTick
        let oneNumber = warehouseCapacity.value / diagramTicks.value
        let newNumber = oneNumber
        
        for (let i = 0; i < diagramTicks.value; i++) {
            ticks.push([newTick,newNumber])
            newTick += oneTick
            newNumber += oneNumber
        }
        return ticks
})



const diagramBarsWidth = computed (() => {
  
 barsQuantity.value = warehouseBoards.value.length
 //console.log(barsQuantity)

 if( barsQuantity.value <= 3) {
    spacesBetweenBars.value = 30
    let diagramBarsWidth = ((diagramWidth.value/2) - (spacesBetweenBars.value * barsQuantity.value + 1))/3
    return diagramBarsWidth
 }
 else if (barsQuantity.value >= 4) {
    spacesBetweenBars.value = 10
    let diagramBarsWidth = ((diagramWidth.value/2) - (spacesBetweenBars.value * barsQuantity.value + 1))/3
    return diagramBarsWidth

 }
})

const processedBoards = computed (() => {
  const Boards = []
  filteredBoards.value.forEach((board,index) => {

    const height = (board.quantity / warehouseCapacity.value) * diagramHeight.value
    const x = 20 + index * (diagramBarsWidth.value + spacesBetweenBars.value) + 30
    const y = diagramHeight.value - (board.quantity / warehouseCapacity.value) * diagramHeight.value
    const barSignatureX = (x + diagramBarsWidth.value)/2  
    const newBar = {
      key: index,
      wood_type: board.wood_type,
      name: board.name,
      dimX: board.dimX,
      dimY: board.dimY,
      dimZ: board.dimZ,
      quantity: board.quantity,
      width: diagramBarsWidth.value,
      height: height,
      x: x,
      y: y,
      barSignatureX: barSignatureX
    }
    Boards.push(newBar)})
  return Boards
} )




onMounted(() => {
  setTimeout(() => {
    isReady.value = true; // Add class to trigger animation
  }, 100);
});

onMounted(() => {
  setTimeout(() => {
    isRendered.value = true; // Add class to trigger animation
  }, 300);
});



// WATCHERS
watch(
  () => props.diagramTicks,
  (ticks) => {
    if (ticks)  {
      diagramTicks.value = ticks
    }
  },
  { immediate: true }
)

watch(
  () => props.warehouseCapacity,
  (propswarehouseCapacity) => {
    if (propswarehouseCapacity)  {
      warehouseCapacity.value = propswarehouseCapacity
    }
  },
  { immediate: true }
)

watch(
  () => props.warehouseBoards,
  (propsWareHouseBoards) => {
    if (propsWareHouseBoards)  {
      warehouseBoards.value = propsWareHouseBoards
    }
  },
  { immediate: true }

  
)
watch(
  () => props.woodType,
  (selectedWoodType) => {
    if (selectedWoodType)  {
      woodType.value = selectedWoodType
    }
  },
  { immediate: true }

  
)
</script>
<style lang="css" scoped>
svg {
  opacity: 0;
  transform: translateX(100px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}

svg.data-ready {
  opacity: 1;
  transform: translateY(0);
}

rect {
  animation-name: grow;
  animation-duration: 0.4s;
  animation-timing-function: linear;
  transform-origin: bottom; 
  transform-box: fill-box;
}

@keyframes grow {
  from {
    transform: scaleY(0.3); 
  }
  to {
    transform: scaleY(1); 
  }
}

</style>