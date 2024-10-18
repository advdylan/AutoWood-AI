
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
                    <input v-model="customer.phoneNumber" class="input" type="text" placeholder="Numer telefonu"/>
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
                    <input v-model="customer.city" class="input" type="text" placeholder="Adres e-mail"/>
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
                        <button @click="submitFile" class="button is-primary mt-3">Upload</button>

                        


                        

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
import { ref } from 'vue'
import axios from 'axios'
import { toast } from 'bulma-toast'

const selectedFile = ref(null)

const newProjectStore = useNewProjectStoreBeta()

const {customer, files} = storeToRefs(newProjectStore)


function handleFileUpload(event) {
    const i = event.target.files.length
    

    for (let file of event.target.files){
        console.log(file)
    }
    selectedFile.value = event.target.files[0]
}


</script>