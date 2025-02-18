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
                                </tr>

                            </thead>
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

//computed values
const processedProductionList = ref([])


















onMounted(() => {
    getProductionList()
})
</script>

<style lang="css" scoped>

</style>