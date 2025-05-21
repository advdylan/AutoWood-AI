<template>
    <div class="columns">
        <div class="column">
            <div v-for="paint in paintsWarehouse"  class="box">
                <nav class="level">
                    <div class="level-left">
                        <div class="level-item">
                            <div 
                            @click="togglePaint(paint)"
                            class="button"
                            :class="{
                                'is-active' : paint.isActive
                            }"
                            >{{ paint.name }}</div>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from "vue";
import { useWarehouseStore } from "@/store/warehousestore";
import { useI18n } from 'vue-i18n';
import { storeToRefs } from 'pinia';

const warehouseStore = useWarehouseStore()
const {paintsWarehouse} = storeToRefs(warehouseStore)
const {togglePaint} = warehouseStore

</script>

<style lang="css" scoped>

</style>