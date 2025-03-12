<template>

<div class="card">


    <div class="card">
        <div class="card-content">
            <div class="columns">
                <div class="column is-full">
                    <div class="label has-text-centered is-size-5"> {{ $t('production') }}</div>
                    <div class="box">

                        <!-- HEADER -->
    <div id="columns" class="columns">
        
        <div v-for="header in headersWithSize" :key="header.id" class="column custom-column" 
        :style="{ flexBasis: header.size}">
            <div class="box custom-header">
                <div class="label has-text-centered is-size-6">{{ header.name }}</div>
            
            </div>

                        <!-- ORDERS SECTION -->
           
            <div class="section has-text-centered custom-section" v-for="(order, index) in productionList" :key="index">

                    <div
                     id="status-indicator" 
                     :class="{
                    'stages-done': areAllStagesTrue(order.stages),
                    'stages-in-progress': !areAllStagesTrue(order.stages)}"
                     class="box custom-box" 
                     v-if="header.name === 'Nr'">

                        {{ order.order.id }}
                    </div>

                    <div class="box has-text-centered custom-box" v-if="header.name === 'Name'">
                        {{ order.order.name }}
                    </div>

                    <div class="box has-text-centered custom-box" v-if="header.name === 'Date of order'">
                        {{ order.date_ordered }}
                    </div>

                    <div 
                    v-if="header.name === 'Delivery time'"
                    class="box has-text-centered custom-box"
                    :class="calculateDeliveryDate(order.date_ordered, order.date_of_delivery)"
                   
                   >
                        {{ order.date_of_delivery }}
                    </div>

                    <div class="box has-text-centered custom-box" v-if="header.name === 'Stages'">
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

                    <div class="box has-text-centered custom-box"  v-if="header.name === 'Category'">
                        {{ order.order.category.name }}
                    </div>

                    <div class="box has-text-centered custom-box" v-if="header.name === 'Paint'">
                        {{ order.order.paints.name }}
                    </div>

                    <div class="box has-text-centered custom-box" v-if="header.name === 'Wood'">
                        {{ order.order.wood.name }}
                    </div>

                    <div class="box has-text-centered custom-box" v-if="header.name === 'Status'">
                        {{ order.status }}
                    </div>

                    <div class="box custom-box" v-if="header.name === 'Notes'">
                        <input class="input custom-input" v-model="order.notes">
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

        <button @click="calculateDeliveryDate('2025-02-13','2025-02-14')" class="button">calculateDeliveryDate</button>

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
const containerWidth = ref(0)





const headers = ref([
    {name: "Nr", size: '50px'},
    {name: "Name", size: '80px'},
    {name: "Date of order", size: '140px'},
    {name: "Delivery time", size: 5},
    {name: "Stages", size: 5},
    {name: "Category", size: 5},
    {name: "Paint", size: 5},
    {name: "Wood", size: 5},
    {name: "Status", size: 5},
    {name: "Notes", size: 5},   
])


//computed values
const maxStages = computed(() => {return Math.max(...productionList.value.map(order => order.stages.length+1))})

const headersWithSize = computed(() => {
    return headers.value.map(header => ({
        ...header,
        size: calculateWidth(header.name)

    }))
})

const totalTextWidth = computed(() => {
    return headers.value.reduce((sum,header) => sum + calculateWidth(header.name), 0)
})



//functions

function areAllStagesTrue(stages) {
    return stages.every(stage => stage.is_done === true);
}

function calculateDeliveryDate(dateOrder,date_of_delivery) {

    let parsedDateOfDelivery = new Date(date_of_delivery)
    let currentDate = new Date()

    console.log(parsedDateOfDelivery)
    console.log(`Current date: ${currentDate}`)

    let difference = (parsedDateOfDelivery - currentDate) / (1000*60*60*24)
    console.log(difference)

    if (difference < 0.7) {
        return 'warning';
      } else if (difference <= 1) {
        return 'danger';
      } else if (difference >= 2) {
        return 'success';
      } else {
        return ''; // Default class (if needed)
      }
}

function calculateWidth(name) {
    return `${name.length * 10 + 20} px`
}














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
    containerWidth.value = document.getElementById('columns')?.offsetWidth
})
</script>



<style scoped>
.custom-section {
  padding: 3px 3px; /* Override Bulma's section padding */
}

.custom-box {
  background-color: rgb(248, 248, 248);
  padding: 5px; /* Override Bulma's box padding */
  height: 40px;
  box-sizing: border-box; /* Ensure padding is included in the height */
}

.custom-box .input {
  width: 100%; /* Make the input fill the container */
  height: 100%; /* Make the input fill the container */
  box-sizing: border-box; /* Ensure padding and border are included in the height */
  border: none; /* Remove default border if needed */
  background-color: transparent; /* Match the background of the container */
  outline: none; /* Remove focus outline if desired */
}

.custom-header {
    margin: 3px;
    margin-top: 3px;
    margin-bottom: 50px;
    
}


.custom-column {
    padding: 0.1rem;
    flex-basis: auto; /* or remove it if not needed */
    flex-grow: 0;

   
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
.stages-done {
    background-color: rgb(97, 173, 110);
}
.stages-in-progress {
    background-color: rgb(255, 230, 169);
}
.success{
    background-color: rgb(97, 173, 110);
}
.danger{
    background-color: rgb(255, 230, 169);
}
.warning{
    background-color: hsl(348, 86%, 61%);
}
</style>

