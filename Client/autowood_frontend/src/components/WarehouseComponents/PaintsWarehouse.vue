<template>
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
                <text>PAINTS WAREHOUSE</text>

                
            </svg>

            
        </div>
</template>
<script setup>
import {computed, ref} from 'vue'
import { useNewProjectStoreBeta } from '@/store/newproject'

import { storeToRefs } from 'pinia'
import axios from 'axios'
import { toast } from 'bulma-toast'
import { useI18n } from 'vue-i18n';



const newProjectStore = useNewProjectStoreBeta()
const {elements,boards} = storeToRefs(newProjectStore)


</script>
<style lang="css">




</style>