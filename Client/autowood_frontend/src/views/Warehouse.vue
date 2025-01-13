<template>
<div class="card">
    <header class="card-header">
    <p class="card-header-title is-size-4"> {{ $t('warehouse') }}</p>

    </header>

    <div class="card">
    <div class="card-content">
    <div class="content">
        <div class="columns">
            <div class="column has-text-centered is-half is-offset-one-quarter">
                <div class="box">
                    <div class="label has-text is-size-5">{{$t('choose_warehouse')}}</div>
                
                <button 
                class="button mr-5"
                :class="{
                    'is-info': !showBoardWarehouse,
                    'is-primary': showBoardWarehouse
                }"
                @click="toggleWarehouse('board')"
                style="width:150px;">

                {{$t('boards')}}
                </button>
                <button
                class="button"
                :class="{
                    'is-info': !showPaintsWarehouse,
                    'is-primary': showPaintsWarehouse,
                }"
                @click="toggleWarehouse('paints')"
                style="width:150px;"
                >
                {{$t('paints')}}
                </button>
                </div>
                
                
                
            </div>
        </div>

        <div class="columns">
        <div class="column has-text-centered is-one-third">
            <!-- INPUT LEFT SECTION -->

            <div class="box">
          <div class="label has-text is-size-5">{{$t('boards')}}</div>
          <BoardInput></BoardInput>
          </div>

        </div>

        <div class="column has-text-centered" >
            <!-- SVG MIDDLE SECTION -->
            <div  style="overflow: hidden; text-align: center;">
            <svg 
                id="svgBoard" 
                xmlns="http://www.w3.org/2000/svg" 
                :viewBox="`-60 -60 1000 800`"
                preserveAspectRatio="xMidYMid meet" 
                style="width: 100%; height: 100%; ">
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

                <rect width="200" height="100" x="10" y="10" rx="20" ry="20" fill="blue" />

                
            </svg>

            
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
const showBoardWarehouse = ref(false)
const showPaintsWarehouse = ref(false)


loadData()

function toggleWarehouse(type){
    if (type === 'board') {
        showBoardWarehouse.value = !showBoardWarehouse.value
    }


}

</script>
<style lang="css">




</style>