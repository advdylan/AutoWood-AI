<template>

    <div class="section">
        
        <div class="columns">
            
            <div class="column is-half has-text-centered is-offset-one-quarter">
                <div class="box">
                <div class="label has-text is-size-4">{{ $t('choose_mode_type') }}</div>
                <div class="columns">
                   
                    <div class="column is-half has-text-centered">
                        
                        <div class="button"
                            @click="chooseCreationMode('newProductCatalogMode')"
                            :class="{
                                'is-warning': creationMode === '' || creationMode === 'newProjectMode' ,
                                'is-success': creationMode === 'newProductCatalogMode'
                                
                            }">{{ $t('new_product') }}</div>
                    
                        <article class="message">
                            
                            <div class="message-body">
                                {{ $t('choose_product_description')}}
                            </div>
                        </article>
                        <div @click="chooseCreationMode('newProductCatalogMode')"  class="button is-success">{{ $t('select') }}</div>
                     
                    </div>
                    <div class="column is-half has-text-centered">
                        <div class="button "
                            @click="chooseCreationMode('newProjectMode')"     
                            :class="{
                                'is-warning': creationMode === '' || creationMode === 'newProductCatalogMode',
                                'is-success': creationMode === 'newProjectMode'
                                
                            }">{{ $t('new_estimate') }}</div>

                        <article class="message">  
                            <div class="message-body">
                                {{$t('choose_estimate_description')}}
                            </div>
                        </article>
                        <div @click="chooseCreationMode('newProjectMode')"   class="button is-success">{{ $t('select') }}</div>
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
import { onUnmounted } from 'vue'
import { toast } from 'bulma-toast'


const newProjectStore = useNewProjectStoreBeta()

const {setMode} = newProjectStore
const {creationMode} = storeToRefs(newProjectStore)

const emit = defineEmits(['next'])

const props = defineProps({
    customerProps: Object,
})

function triggerNext() {
    emit('next')
}

function chooseCreationMode(mode) {
    setMode(mode)
    triggerNext()
}

onUnmounted(() => {

    let msg = ''
    if (creationMode.value === 'newProductCatalogMode') {
        msg = "Wybrano typ Nowy Produkt do katalogu"
    }
    else if(creationMode.value === 'newProjectMode') {
        msg = "Wybrano Nową Wycenę"
    }

    else {
        msg = "No msg data"
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