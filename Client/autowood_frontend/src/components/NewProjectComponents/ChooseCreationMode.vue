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
                                'is-warning': creationMode === '' || creationMode === 'newProjectMode' ,
                                'is-success': creationMode === 'newProductCatalogMode'
                                
                            }">{{ $t('new_product') }}</div>
                    
                        <article class="message">
                            
                            <div class="message-body">
                                {{ $t('choose_product_description')}}
                            </div>
                        </article>
                        <div @click="setMode('newProductCatalogMode')"  class="button is-success">{{ $t('select') }}</div>
                     
                    </div>
                    <div class="column is-half has-text-centered">
                        <div class="button "
                            
                            :class="{
                                'is-warning': creationMode === '' || creationMode === 'newProductCatalogMode',
                                'is-success': creationMode === 'newProjectMode'
                                
                            }">{{ $t('new_estimate') }}</div>

                        <article class="message">  
                            <div class="message-body">
                                {{$t('choose_estimate_description')}}
                            </div>
                        </article>
                        <div @click="setMode('newProjectMode')"  class="button is-success">{{ $t('select') }}</div>
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
import { ref, watch, computed, watchEffect, onUnmounted } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'



const newProjectStore = useNewProjectStoreBeta()

const {setMode} = newProjectStore
const {creationMode} = storeToRefs(newProjectStore)


const props = defineProps({
    customerProps: Object,
})

onUnmounted(() => {

    let msg = ''
    if (creationMode.value === 'newProductCatalogMode') {
        msg = "Wybrano typ Nowy Produkt do katalogu"
    }
    else if(creationMode.value === 'newProjectMode') {
        msg = "Wybrano Nową Wycenę"
    }
    else {
        console.log(creationMode.value)
        msg = 'ERROR'
    }

    toast({
              message: msg,
              duration: 2000,
              position: "top-center",
              type: 'is-success',
              animate: { in: 'backInDown', out: 'backOutUp' },
            })
})


</script>
<style>

</style>