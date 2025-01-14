<template>
    <div  style="overflow: hidden; text-align: center;">
            <svg 
                id="svgBoard" 
                xmlns="http://www.w3.org/2000/svg" 
                :viewBox="`0 0 ${diagramWidth} ${diagramHeight}`"
                preserveAspectRatio="xMinYMin meet" 
                style="width: 100%; height: 100%;"
                transform="scale(1, -1)"
                >
                
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

                <!-- AXES -->
                <g transform="scale(1, -1) translate(0, -500)">
                 <text v-for="tick in ticks"
                 x="2.5%"
                 :y="tick[0]"
                 
                 
                 >{{ Math.trunc(tick[1]) }}</text>
                 </g>
                 


                <line
                  v-for="tick in ticks"
                  x1="5%"
                  x2="90%"
                  :y1="tick[0]" 
                  :y2="tick[0]"
                  style="stroke: black; stroke-width: 0.2;"
                ></line>

            </svg>

            
        </div>
</template>
<script setup>
import {computed, ref, watch} from 'vue'
import { useNewProjectStoreBeta } from '@/store/newproject'

import { storeToRefs } from 'pinia'
import axios from 'axios'
import { toast } from 'bulma-toast'
import { useI18n } from 'vue-i18n';

const diagramWidth = ref(1000)
const diagramHeight = ref(500)
const diagramTicks = ref(null)
const warehouseCapacity = ref(null)



const props = defineProps({
    warehouseBoards: Array,
    warehouseCapacity: Number,
    diagramTicks: Number
}
)



const newProjectStore = useNewProjectStoreBeta()
const {elements,boards} = storeToRefs(newProjectStore)



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

const tickNumbers = computed(() => {

        const tickNumbers = [0]
        let oneNumber = warehouseCapacity.value / diagramTicks.value
        let newNumber = oneNumber

        for (let i = 0; i < diagramTicks.value; i++) {
            tickNumbers.push(newNumber)
            newNumber += oneNumber
        }
        return tickNumbers
})








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
</script>
<style lang="css">




</style>