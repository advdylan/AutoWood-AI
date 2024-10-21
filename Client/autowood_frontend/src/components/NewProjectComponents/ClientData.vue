
<template>
<div class="card">
    <header class="card-header">
      <p class="card-header-title is-centered is-size-3">Podstawowe informacje
        <span>&nbsp;<i class="fa-solid fa-circle-info"></i></span>
      </p>
              
    </header>
    <div class="card-content">
      <div class="content">
        <div class="columns">
            <div class="column is-half">
                <div class="card">
                    <header class="card-header">
                      <p class="card-header-title is-centered is-size-4">Dane klienta
                        <span>&nbsp;<i class="fa-solid fa-id-card"></i></span>
                      </p>
                      
                    </header>
                    <div class="card-content">
                      <div class="content">
                        <label class="label is-size-5">Imię i nazwiska / Nazwa firmy</label>
                <p class="control has-icons-left">
                    <input v-model="customer.name" class="input" type="text" placeholder="Imię i nazwisko"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-user"></i>
                        </span>
                </p>

                <label class="label is-size-5">Numer telefonu</label>
                <p class="control has-icons-left">
                    <input v-model="customer.phone_number" class="input" type="number" placeholder="Numer telefonu"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-phone"></i>
                        </span>
                </p>

                <label class="label is-size-5">Ulica</label>
                <p class="control has-icons-left">
                    <input v-model="customer.street" class="input" type="text" placeholder="Ulica"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-signs-post"></i>
                        </span>
                </p>

                <label class="label is-size-5">Kod pocztowy</label>
                <p class="control has-icons-left">
                    <input v-model="customer.code"  class="input" type="text" placeholder="Kod pocztowy"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-map"></i>
                        </span>
                </p>

                <label class="label is-size-5">Miejscowość</label>
                <p class="control has-icons-left">
                    <input v-model="customer.city" class="input" type="text" placeholder="Miejscowość"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-house"></i>
                        </span>
                </p>

                <label class="label is-size-5">E-mail</label>
                <p class="control has-icons-left">
                    <input v-model="customer.email" class="input" type="text" placeholder="Adres e-mail"/>
                        <span class="icon is-small is-left">
                            <i class="fa-solid fa-envelope"></i>
                        </span>
                </p>
                        

                      </div>
                    </div>               
                </div>

                
                


            </div>
            <div class="column">

                <div class="card">
                    <header class="card-header">
                      <p class="card-header-title is-centered is-size-4">Prześlij pliki
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
                                        <span class="file-label"> Wybierz plik </span>
                                      </span>
                                    </label>
                                  </div>


                            </div>
                        </div>
                        

                        <div class="card">
                          <header class="card-header">
                            <p class="card-header-title is-centered is-size-4">Pliki</p>  
                          </header>
                          <div class="card-content">
                            <div class="content">

                              <div class="files-table-container">
                                <table v-if="files.length > 0" class="table is-bordered is-striped is-hoverable is-fullwidth">
                                  <thead>
                                    <tr>
                                      <th>Nazwa</th>
                                      <th>Rozmiar</th>
                                      <th>Typ</th>
                                      <th>Nav</th>
      
                                    </tr>
                          
                                  </thead>
                                  
                                  <tfoot>
                                    
                                    <tr>
                                      
                                    </tr>
                                  
                                  
                                  </tfoot>
                                  <tbody>
                                    <tr v-for="(file,index) in files" :key="files.name">
                                      
                                      <th>{{ file.name }}</th>
                                      <td>{{ ((file.size)/1000000).toFixed(2) }} mb</td>
                                      <td>{{ (file.type).split('/')[1] }}</td>
                                      <td><b-button class="delete-button" @click="deleteFile(file,index)" type="is-danger is-small"><i class="fa-solid fa-xmark"></i></b-button></td>
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
import { ref, watch } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'





const selectedFile = ref(null)

const newProjectStore = useNewProjectStoreBeta()

const {customer, files} = storeToRefs(newProjectStore)


const props = defineProps({
  customerProps: Object,
  documentsProps: Array,
  imagesProps: Array
})

watch(
  () => props.customerProps,
  (newCustomer) => {
    if (newCustomer)  {
    console.log(newCustomer)
      customer.value = newCustomer
    }
  },
  { immediate: true }
)

/* watch (
  () => props.documentsProps,
  (filesTogether) => {
    if (filesTogether)
    files.value = filesTogether

  },
  { immediate: true }
) */

console.log(files.value)

function deleteFile(file,index){

  files.value.splice(index, 1)
}

function handleFileUpload(event) {
    const i = event.target.files.length
    

    for (let file of event.target.files){
      //console.log(file)
      files.value.push(file)
    }
    selectedFile.value = event.target.files[0]
}


</script>
<style>
</style>