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
                    :x2="'100%'"
                    :y1="diagramHeight - tick[0]"
                    :y2="diagramHeight - tick[0]"
                    style="stroke: black; stroke-width: 0.2;"
                  ></line>

                  <!-- VERTICAL LINES -->




                  <!-- DIAGRAM -->
                   <g v-for="line in daysTicks" :key="line.id">
                      <template v-for="(point, index) in line.data" :key="index">
                        <line
                          v-if="index < line.data.length - 1"
                          :x1="scaleX(point[0])"
                          :y1="point[1]"
                          :x2="scaleX(line.data[index + 1][0])"
                          :y2="line.data[index + 1][1]"
                          :stroke="line.color"
                          stroke-width="2"
                        />
                      </template>
                    </g>

                    <!-- DATA POINTS -->
                    <g v-for="line in daysTicks" :key="line.id">
                    <template v-for="(point,index) in line.data" :key="index">
                      <circle 
                      @mouseenter="(MouseEvent) => displayPointData(line,index, MouseEvent)"
                      @mouseleave="discardPointData()"
                      :cx="scaleX(point[0])" 
                      :cy="point[1]" 
                      r="3"
                      :color="line.color"></circle>
                    </template>
                  </g>
            </svg>
        </div>    

        <!-- DATA BOX -->
        <div
          v-if="tooltipVisible"
          class="box has-background-light has-text-dark"
          :style="{position: 'absolute', top: tooltipY + 'px', left: tooltipX + 'px', zIndex: 100}">
          <p><strong>{{ tooltipData.name }}</strong></p>
          <p>Capacity: {{ tooltipData.capacity }}</p>
          <p>Date: {{ tooltipData.date.toISOString() }}</p>
        </div>


<!--
        <div class="box">
          <div v-for="line in daysTicks" :key="line.id">
            <div class="box" v-for="point,index in line.data" :key="index">
              Current:
              PointX: {{point[0]}}  
              PointY: {{point[1]}}
              <div v-if="index < line.data.length - 1">
              Next:
              PointX: {{ line.data[index + 1][0] }}
              PointY: {{ line.data[index + 1][1] }}
            </div>
            </div>
            
          </div>
        </div>
        !-->

</template>
<script setup>
import {computed, ref, onMounted, watch} from 'vue'
import { useNewProjectStoreBeta } from '@/store/newproject'

import { storeToRefs } from 'pinia'
import axios from 'axios'
import { toast } from 'bulma-toast'
import { useI18n } from 'vue-i18n';
import { useWarehouseStore } from '@/store/warehousestore'
import CatalogList from '@/views/CatalogList.vue'



const warehouseStore = useWarehouseStore()
const {paintsWarehouse} = storeToRefs(warehouseStore)


const diagramWidth = ref(1000)
const diagramHeight = ref(500)
const diagramTicks = ref(null)
const isReady = ref(false)
const warehouseCapacity = ref(null)

const tooltipVisible = ref(false)
const tooltipX = ref(0)
const tooltipY = ref(0)
const tooltipData = ref({})

const props = defineProps({
    warehouseCapacity: Number,
    diagramTicks: Number,
    woodType: String
}
)



const colorPalette = [
  '#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231',
  '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe',
  '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000',
  '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080'
]

const paintColorMap = computed(() => {
  const map = {}
  let index = 0
  for (let paint of paintsWarehouse.value) {
    if (!(paint.name in map)) {
      map[paint.name] = colorPalette[index % colorPalette.length]
      index++
    }
  }
  return map
})

function displayPointData(line,index,event) {
  
  tooltipData.value = {
    name: line.name,
    capacity: line.data[index][2],
    date: line.data[index][3]
  }

  console.log(tooltipData.value)

  const offset = -50;
  const tooltipWidth = 150
  const tooltipHeight = 70
  
  let x = event.clientX + offset
  let y = event.clientY + offset

  if (x + tooltipWidth > window.innerWidth) {
    x = event.clientX - tooltipWidth - offset;
  }

  if (y + tooltipHeight > window.innerHeight) {
    y = event.clientY - tooltipHeight - offset
  }

  tooltipX.value = x
  tooltipY.value = y
  tooltipVisible.value = true;

  console.log(tooltipData.value)
}

function discardPointData() {
  tooltipVisible.value = false;
}

const numberOfTicks = computed(() => {
    return paintsWarehouse.value[0].data.length

})

const daysTicksDistance = computed(() => {
    let spacesBetweenBars = diagramWidth.value / numberOfTicks.value
    return Math.trunc(spacesBetweenBars * 100) / 100;
  })

const daysTicks = computed(() => {

    const daysTicks = []
    let tickX = 0
    
    for (let paint of paintsWarehouse.value) {

      if(paint.isActive) {
        let newPaintObject = {
          name: paint.name,
          color: paintColorMap.value[paint.name],
          data: []
        }
        for (let data of paint.data) {
          console.log(`date.day : ${data.day}`)
          let tickY = diagramHeight.value - (data.capacity / warehouseCapacity.value) * diagramHeight.value
          newPaintObject.data.push([tickX, tickY, data.capacity, data.day])
          tickX += daysTicksDistance.value

        }
        daysTicks.push(newPaintObject)
        tickX = 0
      }
        
    }
    return daysTicks

})



const allPoints = computed(() => {
  return daysTicks.value.flatMap(line => line.data)
})

const maxX = computed(() => {
  return Math.max(...allPoints.value.map(p => p[0]));
})

const minX = computed(() => {
  return Math.min(...allPoints.value.map(p => p[0]))
})

const scaleX = x => {
  const percent = (x - minX.value) / (maxX.value - minX.value)
  console.log(x)
  console.log(`Percent : ${percent}`)
  return diagramWidth.value * (0.05 + percent * 0.95)
};

const ticks = computed(() => {

        const ticks= [[0,0]]
        let oneTick = diagramHeight.value / diagramTicks.value
        let newTick = oneTick
        let oneNumber = warehouseCapacity.value / diagramTicks.value
        console.log(`warehouseCapacity: ${warehouseCapacity.value}`)
        let newNumber = oneNumber

        console.log(`One number: ${oneNumber} newNumber: ${newNumber} oneTick: ${oneTick} newTick :${ newTick}`)
        
        for (let i = 0; i < diagramTicks.value; i++) {
            ticks.push([newTick,newNumber])
            newTick += oneTick
            newNumber += oneNumber
        }
        return ticks
})

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



onMounted(() => {
  setTimeout(() => {
    isReady.value = true; 
  }, 100);
});

</script>
<style scoped lang="css">

svg {
  opacity: 0;
  transform: translateX(100px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}

svg.data-ready {
  opacity: 1;
  transform: translateY(0);
}

line {
  animation-name: drawLine;
  animation-duration: 0.4s;
}

@keyframes drawLine {
  to {
    stroke-dashoffset: 0;
  }
}




</style>