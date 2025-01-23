<template>
<div class="card">


    <div class="card">
    <div class="card-content">
    <div class="content">
        <div class="columns">
            <div class="column has-text-centered is-half is-offset-one-quarter">

                
            </div>
        </div>

        <div class="columns">
        <div class="column has-text-centered is-one-third">
            <!-- INPUT LEFT SECTION -->
            <div class="box">
                    <div class="label has-text is-size-5">{{$t('choose_warehouse')}}</div>
                
                <button 
                class="button mr-5"
                :class="{
                    'is-active': warehouseComponents[0].active,
                    'is-info': !warehouseComponents[0].active
                }"
                @click="toggleWarehouse('boards')"
                style="width:150px;">

                {{$t('boards')}}
                </button>
                <button
                class="button"
                :class="{
                    'is-active': warehouseComponents[1].active,
                    'is-info': !warehouseComponents[1].active,
                }"
                @click="toggleWarehouse('paints')"
                style="width:150px;"
                >
                {{$t('paints')}}
                </button>
                
                <div class="section" v-if="warehouseComponents[0].active">

                <button v-for="woodType in wood"
                :class="{
                    'is-active': chosenWoodType === woodType.name,
                    'is-info': chosenWoodType != woodType.name
                }"
                :key="woodType.name" 
                class="button mr-5"  
                style="width:100px;"
                @click="chooseWoodType(woodType);
                        showThicknessSection = !showThicknessSection;">

                {{ woodType.name }}
                </button>

            </div>
            <div class="section" v-if="warehouseComponents[0].active && showThicknessSection">

                <button v-for="(value, key) in thicknesses" :key="key">
                {{ key }} {{ value }}
                </button>

            </div>
        </div>

            
        


        <div v-if="warehouseComponents[0].active | warehouseComponents[1].active" class="box">
          <div class="label has-text is-size-5">{{$t('boards')}}</div>
          <BoardManager
          ></BoardManager>
          </div>

        </div>

        <div class="column" >
            <!-- SVG MIDDLE SECTION -->
            



             <BoardsWarehouse 
             v-if="warehouseComponents[0].active"
             
             :warehouse-capacity="warehouseCapacity"
             :diagram-ticks="diagramTicks"
             
             ></BoardsWarehouse>

             

             


             <PaintsWarehouse v-if="warehouseComponents[1].active"
             ></PaintsWarehouse>

        <div class="box">
        <div class="label has-text is-size-5">{{$t('settings')}}</div>
        <div class="columns">
            <div class="column is-half">
                <nav class="level">
                    <div class="level-left">
                        <div class="level-item">
                            <div class="label has-text is-size-8  mr-2"> {{ $t('warehouse_capacity') }}:</div>
                            <input style="width: 20%;" class="input is-small " v-model="warehouseCapacity">
                        </div>
                    </div>
                </nav>
                <nav class="level">
                    <div class="level-left">
                        <div class="level-item">
                            <div type="number" class="label has-text is-size-8  mr-2">Ticks: </div>
                            <input style="width: 20%;" class="input is-small " v-model="diagramTicks">
                        </div>
                    </div>
                </nav>
                
            </div>
        </div>
        </div>
            
        </div>



        </div>
        <div class="columns">
        <div class="column has-text-centered is-half" >

        </div>
        <div class="column has-text-centered is-half" >
            
            
        </div>

        </div>

        

        
    </div>
    </div>
</div>
</div>


<!-- MODAL -->




</template>




<script setup>
import {computed, ref} from 'vue'
import { useNewProjectStoreBeta } from '@/store/newproject'
import BoardInput from '@/components/OptimizerComponents/BoardInput.vue'
import BoardsWarehouse from '@/components/WarehouseComponents/BoardsWarehouse.vue'
import PaintsWarehouse from '@/components/WarehouseComponents/PaintsWarehouse.vue'
import BoardManager from '@/components/WarehouseComponents/BoardManager.vue'
import { storeToRefs } from 'pinia'
import axios from 'axios'
import { toast } from 'bulma-toast'
import { useI18n } from 'vue-i18n';





const newProjectStore = useNewProjectStoreBeta()
const {warehouseBoards, wood, chosenWoodType} = storeToRefs(newProjectStore)
const {loadData, chooseWoodType } = newProjectStore
const showBoardWarehouse = ref(false)
const showPaintsWarehouse = ref(false)
const warehouseCapacity = ref(100)
const diagramTicks = ref(10)
const showThicknessSection = ref(false)


const warehouseComponents = ref([
    {name: 'boards', component: BoardsWarehouse, active: false},
    {name: 'paints', component: PaintsWarehouse, active: false}
])


loadData()

function toggleWarehouse(type){
    let warehouseToActivate = warehouseComponents.value.map((warehouse) => {
        if (warehouse.active){
            warehouse.active = false
        }
        else if (warehouse.name == type){
            warehouse.active = true
        }
    }) 
}

const thicknesses = computed(() => {
  const result = new Map()

    warehouseBoards.value.forEach(item => {
      const woodName = item.wood_type.name
      const dimZ = item.dimZ

      if (!result.has(woodName)) {
        result.set(woodName, new Set())
      }

      result.get(woodName).add(dimZ)
    });

    // Convert the sets to arrays and sort them
    const finalResult = {}
    result.forEach((dimZSet, woodName) => {
      finalResult[woodName] = Array.from(dimZSet).sort((a, b) => a - b)
    });

    console.log(finalResult)
    return finalResult
})



</script>
<style lang="css">




</style>