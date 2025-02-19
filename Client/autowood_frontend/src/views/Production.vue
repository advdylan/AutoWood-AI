<template>

<div class="card">


    <div class="card">
        <div class="card-content">
            <div class="columns">
                <div class="column is-full">
                    <div class="label has-text-centered is-size-5"> {{ $t('production') }}</div>
                    <div class="box">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Order number</th>
                                    <th>Order name</th>
                                    <th>Category</th>
                                    <th>Paint</th>
                                    <th>Wood</th>
                                    <th :colspan="maxStages">Stages</th>
                                    <th>Status</th>
                                    <th>Notes</th>
                                    <th>Date of order</th>
                                    <th>Delivery time</th>
                                </tr>

                            </thead>
                            <tr v-for="order in productionList">
                                <td>{{ order.order.id }}</td>
                                <td>{{ order.order.name }}</td>
                                <td>{{ order.order.category.name }}</td>
                                <td>{{ order.order.paints.name }}</td>
                                <td>{{ order.order.wood.name }}</td>
                                
                                <td v-for="stage in order.stages">
                                   
                                        <label class="checkbox">
                                        <input type="checkbox">
                                            {{ stage.stage.shortcut }}
                                            
                                        </label>
                                       
                                                          
                                </td>
                                <td>{{ order.status }}</td>
                                <td>{{ order.notes }}</td>
                                <td>{{ order.date_ordered }}</td>
                                <td>{{ order.date_of_delivery }}</td>
                           
                               
                                
                            </tr>
                           
                        </table>


                        
                        
                    </div>

                </div>
            </div>

   
</div>
    </div>
        </div>



</template>

<script setup>
import axios from 'axios';
import { productionStore } from '@/store/production';
import { ref, onMounted, computed } from 'vue';
import { storeToRefs } from 'pinia';

//store data 
const store = productionStore()
const {getProductionList} = store
const {productionList} = storeToRefs(store)

//const variables
const maxStages = computed(() => {return Math.max(...productionList.value.map(order => order.stages.length+1))})

//computed values
const processedProductionList = ref([])


















onMounted(() => {
    getProductionList()
})
</script>

<style lang="css" scoped>

</style>