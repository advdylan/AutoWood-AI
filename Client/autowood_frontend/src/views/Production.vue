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
                    <div class="box">
                        <div class="columns">
                            <div v-for="header in headers" class="column">
                                <div class="box">
                             <div class="label has-text-centered is-size-6"> {{header.name}} </div>
                                </div>
                            </div>
                        </div>
                        <div class="columns">
                            <div class="column">

                                <div class="section" v-for="order in productionList">
                                    <div class="box"> {{ order.order.id }} </div>
                                </div>
                                
                            </div>
                        </div>


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

const headers = [
    {name: "Nr", size: 5},
    {name: "Name", size: 5},
    {name: "Date of order", size: 5},
    {name: "Delivery time", size: 5},
    {name: "Category", size: 5},
    {name: "Paint", size: 5},
    {name: "Wood", size: 5},
    {name: "Status", size: 5},
    {name: "Notes", size: 5},   
]

//computed values
/* const processedProductionList = computed(() => {
    const orders = [];

    for (let order of productionList.value) {
        console.log(order);



        let newOrder = {
            headerNames: headers.value,
            id: order.order.id,
            name: order.order.name,
            date_ordered: order.date_ordered,
            date_of_delivery: order.date_of_delivery,
            category: order.order.category,
            paint: order.order.paints.name,
            wood: order.order.wood.name,
            stages: order.order.stages,
            status: order.order.status,
            notes: order.notes
        } 
        console.log(newOrder);
        orders.push(newOrder);

    }
    
    console.log(orders);
        
   
    return orders;

}) */


















onMounted(() => {
    getProductionList()
})
</script>

<style lang="css" scoped>

</style>