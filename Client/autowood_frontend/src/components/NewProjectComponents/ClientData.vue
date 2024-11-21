
<template>

<div class="card">
    <header v-if="showCardTitle" class="card-header">
      <p class="card-header-title is-centered is-size-3">{{$t("basic_info")}}
        <span>&nbsp;<i class="fa-solid fa-circle-info"></i></span>
      </p>             
    </header>
    <div class="card-content">
      <div class="content">
        <div class="columns">
            <div class="column is-half">
                
                    <header class="card-header">
                      <p class="card-header-title is-centered is-size-4">{{$t("client_data")}}
                        <span>&nbsp;<i class="fa-solid fa-id-card"></i></span>
                      </p>
                      
                    </header>
                    <div class="card-content">
                      <div class="content">
                        <label class="label is-size-6">{{$t("client_name")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.name" class="input is-small" type="text" :placeholder="$t('client_name')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-user"></i>
                        </span>
                </p>

                <label class="label is-size-5">{{$t("number")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.phone_number" class="input" type="number" :placeholder="$t('number')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-phone"></i>
                        </span>
                </p>

                <label class="label is-size-5">{{$t("street")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.street" class="input" type="text" :placeholder="$t('street')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-signs-post"></i>
                        </span>
                </p>

                <label class="label is-size-5">{{$t("zip_code")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.code"  class="input" type="text" :placeholder="$t('zip_code')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-map"></i>
                        </span>
                </p>

                <label class="label is-size-5">{{$t("city")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.city" class="input" type="text" :placeholder="$t('city')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-house"></i>
                        </span>
                </p>

                <label class="label is-size-5">{{$t("e-mail")}}</label>
                <p class="control has-icons-left">
                    <input v-model="customer.email" class="input" type="text" :placeholder="$t('e-mail')"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-envelope"></i>
                        </span>
                </p>
                        

                      </div>
                    </div>               
                

                
                


            </div>
            <div class="column">

                <div class="card">
                    <header class="card-header">
                      <p class="card-header-title is-centered is-size-4">{{$t("send_files")}}
                        <span>&nbsp;<i class="fa-solid fa-upload"></i></span>
                      </p>
                      
                    </header>
                    <div class="card-content">
                      <div class="content">
                        <div class="columns">
                            <div class="column is-full">
                                <div class="file is-large is-centered is-boxed">
                                    <label class="file-label">

                                      <input class="file-input" type="file" multiple  name="docs" v-on:change="handleFileUpload" />
                                      
                                      <span class="file-cta">
                                        <span class="file-icon">
                                          <i class="fas fa-upload"></i>
                                        </span>
                                        <span class="file-label"> {{$t("choose_files")}} </span>
                                      </span>
                                    </label>
                                  </div>


                            </div>
                        </div>
                        

                        <div class="card">
                          <header class="card-header">
                            <p class="card-header-title is-centered is-size-4">{{$t("files")}}</p>  
                          </header>
                          <div class="card-content">
                            <div class="content">

                              <div class="files-table-container">
                                <table v-if="files.length > 0" class="table is-bordered is-striped is-hoverable is-fullwidth">
                                  <thead>
                                    <tr>
                                      <th>{{$t("file_name")}}</th>
                                      <th>{{$t("size")}}</th>
                                      <th>{{$t("typ")}}</th>
                                      <th>{{$t("Nav")}}</th>
      
                                    </tr>
                          
                                  </thead>
                                  
                                  <tfoot>
                                    
                                    <tr>
                                      
                                    </tr>
                                  
                                  
                                  </tfoot>
                                  <tbody>
                                    <tr v-for="(file,index) in files" :key="files.name">
                                      
                                      <th>{{ file.name }}</th>
                                      <td>{{ ((file.size)/1000000).toFixed(2)}} mb</td>
                                      <td>{{ (file.file_type) }}</td>
                                      <td><b-button class="button" @click="deleteFile(file,index)" type="is-danger"><i class="fa-solid fa-xmark"></i></b-button></td>
                                    </tr>
                                  </tbody>
                                  
                                </table>
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
    </div>
    
  </div>

  

</template>

<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { storeToRefs } from 'pinia'
import { ref, watch, computed } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'





const selectedFile = ref(null)

const newProjectStore = useNewProjectStoreBeta()

const {customer, files} = storeToRefs(newProjectStore)


const props = defineProps({
  customerProps: Object,
  documentsProps: Array,
  imagesProps: Array,
  showCardTitle: Boolean
})

const showCardTitle = computed(() => props.showCardTitle);



watch(
  () => props.customerProps,
  (newCustomer) => {
    if (newCustomer)  {
      customer.value = newCustomer
    }
  },
  { immediate: true }
)

watch (
  () => props.documentsProps,
  (filesTogether) => {
    if (filesTogether)
    files.value = filesTogether

  },
  { immediate: true }
) 



function deleteFile(file,index){

  files.value.splice(index, 1)
}

function handleFileUpload(event) {
    const i = event.target.files.length
    

    for (let file of event.target.files){
      
      files.value.push(file)
    }
    selectedFile.value = event.target.files[0]
}


</script>
<style>
</style>