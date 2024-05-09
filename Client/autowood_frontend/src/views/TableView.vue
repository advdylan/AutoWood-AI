<template>

        <table class="table is-bordered is-striped is-hoverable is-fullwidth">
          <thead>
            <tr>
              <th>Name</th>
              <th>Długość</th>
              <th>Wysokość</th>
              <th>Grubość</th>
              <th>Materiał</th>
              <th>Ilość</th>
            </tr>
  
          </thead>
          
          <tfoot>
            <tr>
              <th>Podsumowanie</th>
            </tr>
          </tfoot>
          <tbody>
            <tr v-for="element in elements" :key="element.name">
              
              <th>{{ element.name }}</th>
              <td>{{ element.dimX }}</td>
              <td>{{ element.dimY }}</td>
              <td>{{ element.dimZ }}</td>
              <td>{{ element.wood_type }}</td>
              <td>{{ element.quantity }}</td>          
            </tr>
          </tbody>
          
        </table>

        <form @submit.prevent="addElement">

            <div class="field">
              <label class="label">Nazwa</label>
              <div class="control">
                <input class="input" type="text" placeholder="Nazwa" v-model="newElement.name" >             
              </div>
            </div>

            <div class="field">
              <label class="label">Długość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Długość" v-model="newElement.dimX" >             
              </div>
            </div>

            <div class="field">
              <label class="label">Szerokość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Szerokosć" v-model="newElement.dimY" >             
              </div>
            </div>

            <div class="field">
              <label class="label">Grubość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Grubość" v-model="newElement.dimZ">             
              </div>
            </div>

            <div class="field">
              <label class="label">Ilość</label>
              <div class="control">
                <input class="input" type="text" placeholder="Ilość" v-model="newElement.quantity" >             
              </div>
            </div>

            <div class="field">
              <label class="label">Materiał</label>
              <div class="control">
                <div class="select">
                  <select v-model="newElement.wood_type">
                    <option v-for="wood in wood"> {{ wood.name}}</option >
                  </select>
                </div>
              </div>
            </div>

            
          <footer class="modal-card-foot">
            <div class="buttons">
              <button @click="addElement(newElement)" type="submit" class="button is-success">Zapisz</button>
              <button class="button">Anuluj</button>
            </div>
            </footer>
        </form>
      
    </template>


<script setup>
import { useNewProjectStoreBeta } from '@/store/newprojectbeta'
import {ref} from 'vue'
import { storeToRefs } from 'pinia'


const newElement = ref({
  name: '',
  dimX: '',
  dimY: '',
  dimZ: '',
  quantity: '',
  wood_type: ''
})

const elementStore = useNewProjectStoreBeta()

const {elements } = storeToRefs(elementStore)
const { addElement } = elementStore








</script>


