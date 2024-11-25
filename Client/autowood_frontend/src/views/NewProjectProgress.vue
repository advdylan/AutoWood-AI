<template>


<div class="card">

  <div class="box">
    <div class="columns">
      <div class="column is-two-fifths">
        <div class="button is-rounded">1</div>
      </div>
      <div class="column">  
        <div class="button is-rounded is-justify-content-center">2</div>
      </div>
      <div class="column">  
        <div class="button is-rounded">3</div>
      </div>
    </div>

  </div>
  
    
  

  <div class="card-content">
    <div class="content">
      <ClientData :show-card-title="false"></ClientData>

    </div>
  </div>
  <footer class="card-footer">
    <div class="sphere"></div>
    <a href="#" class="card-footer-item">Edit</a>
    <a href="#" class="card-footer-item">Delete</a>
  </footer>
</div>





 
</template>
  
<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { useSummaryStore } from '@/store/summary'
import {ref, computed, onUnmounted, watch, watchEffect} from 'vue'
import { storeToRefs } from 'pinia'
import {validateFormData} from '@/validators/Validators.js'
import { useI18n } from 'vue-i18n';

import ElementsTable from '@/components/ElementsTable'
import WorktimeType from '@/components/WorktimeType'
import AccessoryTable from '@/components/AccessoryTable.vue'
import Summary from '@/components/Summary.vue'
import ClientData from '@/components/NewProjectComponents/ClientData.vue'


import axios from 'axios'
import { toast } from 'bulma-toast'







</script>

<style>

.modal{
  --bulma-modal-content-width: 70%;
}



</style>
