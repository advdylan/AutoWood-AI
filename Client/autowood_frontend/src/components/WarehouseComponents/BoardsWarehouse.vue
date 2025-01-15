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


                    <!-- TEXT -->
                 <text v-for="tick in ticks"
                 x="2.5%"
                 :y="diagramHeight - tick[0]"
                 >{{ Math.trunc(tick[1]) }}</text>
                 
                    <!--HORIZONTAL LINES-->
                    <TransitionGroup
                  tag="g"
                  enter-active-class="animate__animated animate__fadeIn"
                  leave-active-class="animate__animated animate__fadeOut"
                  move-class="move-animation"
                >
                  <line
                    v-for="(tick, index) in ticks"
                    :key="tick[0]"
                    :x1="'5%'"
                    :x2="'90%'"
                    :y1="diagramHeight - tick[0]"
                    :y2="diagramHeight - tick[0]"
                    style="stroke: black; stroke-width: 0.2;"
                  ></line>
                </TransitionGroup>

                    

                    

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

onMounted(() => {
  setTimeout(() => {
    isReady.value = true; // Add class to trigger animation
  }, 100);
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
</script>
<style lang="css">
svg {
  opacity: 0;
  transform: translateX(20px);
  transition: opacity 0.5s ease, transform 0.5s ease;
}

svg.data-ready {
  opacity: 1;
  transform: translateY(0);
}

/* Optional: Smooth transitions for moving elements */
.move-animation {
  transition: transform 0.5s ease;
}

</style>