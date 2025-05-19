<template>

    <div class="columns">
        <div class="column is-10 is-offset-1">
            {{ paintsWarehouse }}
        </div>
    </div>

</template>

<script setup>
import { ref, watch } from "vue";
import { useNewProjectStoreBeta } from '@/store/newproject'
import { useI18n } from 'vue-i18n';
import { storeToRefs } from 'pinia';

const store = useNewProjectStoreBeta()
const {paintsWarehouse} = storeToRefs(store)

</script>

<style lang="css" scoped>

</style>