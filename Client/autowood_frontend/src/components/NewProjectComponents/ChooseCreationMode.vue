<template>

    <div class="section">
        
        <div class="columns">
            
            <div class="column is-half has-text-centered is-offset-one-quarter">
                <div class="box">
                <div class="label has-text is-size-4">{{ $t('choose_mode_type') }}</div>
                <div class="columns">
                   
                    <div class="column is-half has-text-centered">
                        
                        <div class="button" 
                            :class="{
                                'is-info' : NewProductCatalogMode,
                                'is-active' : !NewProductCatalogMode
                            }">{{ $t('new_product') }}</div>
                    
                        <article class="message">
                            
                            <div class="message-body">
                                {{ $t('choose_product_description')}}
                            </div>
                        </article>
                        <div class="button is-success">{{ $t('select') }}</div>
                     
                    </div>
                    <div class="column is-half has-text-centered">
                        <div class="button" 
                :class="{
                    'is-info' : NewProjectMode,
                    'is-active' : !NewProjectMode
                }">{{ $t('new_estimate') }}</div>

                        <article class="message">  
                            <div class="message-body">
                                {{$t('choose_estimate_description')}}
                            </div>
                        </article>
                        <div class="button is-success">{{ $t('select') }}</div>
                    </div>
                </div>
            </div>          
        </div>
    </div>
</div>

    
</template>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'
import { ref, watch, computed, watchEffect } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'

const NewProductCatalogMode = ref(false)
const NewProjectMode = ref(false)




const newProjectStore = useNewProjectStoreBeta()

const {customer,files,category,wood,collection,paints, selectedCategory, selectedWood, selectedPaint, selectedCollection, selectedFile, projectName} = storeToRefs(newProjectStore)


const props = defineProps({
    customerProps: Object,
})

</script>
<style>

</style>