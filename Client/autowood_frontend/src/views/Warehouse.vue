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
                </div>
        


        <div v-if="warehouseComponents[0].active | warehouseComponents[1].active" class="box">
          <div class="label has-text is-size-5">{{$t('boards')}}</div>
          <BoardInput
          :elements="warehouseBoards"></BoardInput>
          </div>

        </div>

        <div class="column" >
            <!-- SVG MIDDLE SECTION -->
             <BoardsWarehouse 
             v-if="warehouseComponents[0].active"
             :warehouse-boards="warehouseBoards"
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
import { storeToRefs } from 'pinia'
import axios from 'axios'
import { toast } from 'bulma-toast'
import { useI18n } from 'vue-i18n';



const newProjectStore = useNewProjectStoreBeta()
const {elements} = storeToRefs(newProjectStore)
const {loadData } = newProjectStore
const showBoardWarehouse = ref(false)
const showPaintsWarehouse = ref(false)
const warehouseBoards = ref([])
const warehouseCapacity = ref(100)
const diagramTicks = ref(10)

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

function getBoards() {
   
    axios
    .get(`/api/v1/warehouse/boards/`)
    .then(response =>{
        console.log(response)
        warehouseBoards.value = response.data
    })
    .catch(error => {
        console.log(error)
    })
}
getBoards()
</script>
<style lang="css">




</style>