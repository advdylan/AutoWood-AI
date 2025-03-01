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

                        <!-- HEADER -->
    <div class="columns">
        
        <div v-for="header in headers" :key="header.id" class="column custom-column">
            <div class="box custom-header">
                <div class="label has-text-centered is-size-6">{{ header.name }}</div>
            
            </div>

                        <!-- ORDERS SECTION -->
           
            <div class="section custom-section" v-for="(order, index) in productionList" :key="index">

                    <div id="status-indicator" class="box custom-box" v-if="header.name === 'Nr'">
                        {{ order.order.id }}
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Name'">
                        {{ order.order.name }}
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Date of order'">
                        {{ order.date_ordered }}
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Delivery time'">
                        {{ order.date_of_delivery }}
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Stages'">
                        <nav class="level" >
                            <div class="level-left">

                                <div class="level-item" v-for="stage in order.stages">
                                    
                                    <label class="custom-checkbox">
                                        <input v-model="stage.is_done" type="checkbox" class="custom-checkbox-input">
                                        <span class="custom-checkbox-label">{{ stage.stage.shortcut }}</span>
                                        <span class="custom-checkbox-checkmark"></span>
                                    </label>       
                                </div>
                            </div>           
                        </nav>
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Category'">
                        {{ order.order.category.name }}
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Paint'">
                        {{ order.order.paints.name }}
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Wood'">
                        {{ order.order.wood.name }}
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Status'">
                        {{ order.status }}
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Notes'">
                        {{ order.notes }}
                    </div>
            </div>
        </div>
    </div>
</div>
                </div>
            </div>

   
</div>
    </div>
        </div>


        <button @click="checkStages()" class="button">CHECK STAGES</button>

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
const orderColor = ref('')


const headers = [
    {name: "Nr", size: 5},
    {name: "Name", size: 5},
    {name: "Date of order", size: 5},
    {name: "Delivery time", size: 5},
    {name: "Stages", size: 5},
    {name: "Category", size: 5},
    {name: "Paint", size: 5},
    {name: "Wood", size: 5},
    {name: "Status", size: 5},
    {name: "Notes", size: 5},   
]


//computed values
const maxStages = computed(() => {return Math.max(...productionList.value.map(order => order.stages.length+1))})

function areAllStagesTrue(stages) {
    return stages.every(stage => stage.is_done === true);
}

function checkStages() {
    for (let order of productionList.value) {
        
        let status = areAllStagesTrue(order.stages)
        console.log(status);
     
    }
}


//functions

















/* const processedProductionList = computed(() => {
    const orders = [];

    for (let order of productionList.value) {
        console.log(order);

        let newOrder = {
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

})  */


















onMounted(() => {
    getProductionList()
})
</script>



<style scoped>
.custom-section {
  padding: 3px 3px; /* Override Bulma's section padding */
}

.custom-box {
  background-color: rgb(248, 248, 248);
  padding: 3px 3px; /* Override Bulma's box padding */
  height: 40px;
}

.custom-header {
    margin: 3px;
    margin-top: 3px;
    margin-bottom: 50px;
    
}

.custom-column {
    padding: 0.1rem;
}

.custom-checkbox {
    position: relative;
    display: inline-block;
    cursor: pointer;
    font-size: 13px; /* Adjust size as needed */
    padding-left: 23px; /* Space for the custom checkbox */
    margin-right: 15px; /* Spacing between checkboxes */
}

.custom-checkbox-input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
}

.custom-checkbox-checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 20px; /* Size of the checkbox */
    width: 20px; /* Size of the checkbox */
    background-color: #eee;
    border: 2px solid #ccc;
    border-radius: 5px; /* Rounded corners */
    transition: background-color 0.3s, border-color 0.3s;
}

.custom-checkbox-label {
    display: block;
    margin-bottom: 5px; /* Space between label and checkbox */
    font-weight: bold;
}

/* When the checkbox is checked */
.custom-checkbox-input:checked ~ .custom-checkbox-checkmark {
    background-color: #2196F3; /* Blue background */
    border-color: #2196F3;
}

/* Checkmark icon (hidden by default) */
.custom-checkbox-checkmark:after {
    content: "";
    position: absolute;
    display: none;
    left: 6.5px;
    top: 2.5px;
    width: 5px;
    height: 10px;
    border: solid white;
    border-width: 0 2px 2px 0;
    transform: rotate(45deg);
}

/* Show the checkmark when checked */
.custom-checkbox-input:checked ~ .custom-checkbox-checkmark:after {
    display: block;
}
</style>

