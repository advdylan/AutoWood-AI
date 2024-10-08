<template>

 <div class=columns >
  <div class="column is-full">
 
  <div class="container">
    <div class="notification is-warning">
      <div class="title is-centered is-size-4">
        Dział edytowania kosztów usług       
      </div>
      <div class="text">
        Każdorazowa zmiana poniższych kosztów pracy nie działa wstecz. Tylko nowe projekty otrzymają nowe, poniższe wartości.
      </div>
    </div>
  </div>
  </div>
</div>

    <div class="columns is-flex">
        <div class="column is-one-third">
            <div class="card">
                <header class="card-header">
                  <p class="card-header-title is-centered">Koszty pracy zakładu</p>               
                </header>
                <div class="card-content">
                    <div class="columns">


                        <div class="column is-two-thirds">
                            <div v-for="worktime_name in worktimetype" class="field">
                                <div class="control">
                                    <input  class="input" type="text" :placeholder="worktime_name.name" disabled/>
                                </div>
                            </div>

                        </div>

                        <div class="column">
                            <div v-for="worktime_value in worktimetype" class="field">
                                <input class="input" type="number" placeholder="bind-to-" v-model=worktime_value.cost :disabled="toggleDisabled"/>                                          
                            </div>
                        </div>
                    </div>
                    <div class="buttons">
                        <button @click="toggleSaveWindows = !toggleSaveWindows"
                         class="button is-dark"><i class="fa-regular fa-floppy-disk">&nbsp;</i>Zapisz zmiany</button>  
                        <button @click="toggleAddWorktype = !toggleAddWorktype" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>Dodaj dział</button>   
                        <button @click="handleEditButton()" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj</button>                       
                    </div>
                </div>
              </div>

        </div>
        <div class="column is-flex is-one-third">

          <div class="card">
            <header class="card-header">
              <p class="card-header-title is-centered">Koszty materiałów( zł / m3)</p>               
            </header>
            <div class="card-content">
                <div class="columns">


                    <div class="column is-two-thirds">
                        <div v-for="wood_name in wood" class="field">
                            <div class="control">
                                <input  class="input" type="text" :placeholder="wood_name.name" disabled/>
                            </div>
                        </div>

                    </div>

                    <div class="column">
                        <div v-for="wood_cost in wood" class="field">
                            <input class="input" type="number" placeholder="bind-to-" v-model=wood_cost.price :disabled="toggleDisabled"/>                                          
                        </div>
                    </div>
                </div>
                <div class="buttons">
                    <button @click="toggleSaveWindows = !toggleSaveWindows"
                     class="button is-dark"><i class="fa-regular fa-floppy-disk">&nbsp;</i>Zapisz zmiany</button>  
                    <button @click="toggleAddWorktype = !toggleAddWorktype" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>Dodaj nowy materiał</button>   
                    <button @click="handleEditButton()" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj</button>                       
                </div>
            </div>
          </div>
            
        </div>
        <div class="column is-one-third">
            
        </div>
    </div>


    <div v-bind:class="{'is-active': toggleSaveWindows}" class="modal" style="--bulma-modal-content-width: 30%;">
        <div class="modal-background"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">Zatwierdź zmiany</p>
            <button @click="toggleSaveWindows = !toggleSaveWindows" class="delete" aria-label="close"></button>
          </header>
          <section class="modal-card-body has-text-centered">
            Wprowadziłeś zmiany w kosztach pracy poszczególnych zespołów.
            <br>
            Czy chcesz zapisać?* 
          </section>
          <footer class="modal-card-foot">
            <div class="buttons">
              <button @click="handleUpdateWorktimetypes(worktimetype);
              toggleSaveWindows = !toggleSaveWindows;"     
              class="button is-success"><i class="fa-regular fa-floppy-disk">&nbsp;</i>Zapisz</button>
              <button class="button"><i class="fa-solid fa-ban">&nbsp;</i>Anuluj</button>
              <p class="has-text-left is-size-7">*Wprowadzone zmiany nie zmienią wcześniej zapisanych wycen</p>
              
              <p class="has-text-left is-size-7">Tylko nowe wyceny otrzymają wprowadzone wartości</p>
            </div>
          </footer>
        </div>
      </div>


      <div v-bind:class="{'is-active': toggleAddWorktype}" class="modal" style="--bulma-modal-content-width: 30%;">
        <div class="modal-background"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">Dodaj nowy dział</p>
            <button @click="toggleAddWorktype = !toggleAddWorktype" class="delete" aria-label="close"></button>
          </header>
          <section class="modal-card-body has-text-centered">

           <div class="card-content">
            <div class="columns">
                <div class="column is-half">
                    <label  class="label">Nazwa działu</label>
                    <input v-model="new_worktimetype_name" class="input" type="text" placeholder="Dział" />
                </div>
                <div class="column">
                    <label class="label">Koszt pracy na godzinę</label>
                    <input v-model="new_worktimetype_cost" class="input" type="text" placeholder="Koszt" />
                </div>
            </div>
        </div>
            
          </section>
          <footer class="modal-card-foot">
            <div class="buttons">
              <button
              @click="addNewWorktimetype(new_worktimetype_name,new_worktimetype_cost);
                      updateWorktimetypes(worktimetype)" class="button is-success"><i class="fa-regular fa-floppy-disk">&nbsp;</i>Zapisz</button>
              <button class="button"><i class="fa-solid fa-ban">&nbsp;</i>Anuluj</button>
              <p class="has-text-left is-size-7">*Wprowadzone zmiany nie zmienią wcześniej zapisanych wycen</p>
              
              <p class="has-text-left is-size-7">Tylko nowe wyceny otrzymają wprowadzone wartości</p>
            </div>
          </footer>
        </div>
      </div>



</template>
<script setup>
import { useNewProjectStoreBeta } from '@/store/newproject'
import { usePricesSetup } from '@/store/pricessetup';
import axios from 'axios'
import { storeToRefs } from 'pinia';
import {ref} from 'vue'
import { toast } from 'bulma-toast';

const toggleDisabled = ref(true)
const toggleSaveWindows = ref(false)
const toggleAddWorktype = ref(false)
const new_worktimetype_name = ref('')
const new_worktimetype_cost = ref('')
const errors = ref([])

const temporaryWorktimetypes = ref()

//MAIN STORE
const mainstore = useNewProjectStoreBeta()

const {loadData} = mainstore
const {worktimeCost, worktimetype, wood} = storeToRefs(mainstore)

//PRICE SETUP STORE
const pricesstore = usePricesSetup()

const {updateWorktimetypes} = pricesstore
const {newWorktimeCost} = storeToRefs(pricesstore)

loadData()

function handleEditButton() {
  if (toggleDisabled.value === false) {
    toggleDisabled.value = true
    console.log("pt1")
  }
  else {
    toggleDisabled.value = false
    loadData()
    console.log("pt2")
  }
}

function addNewWorktimetype(new_worktimetype_name, new_worktimetype_cost) {
  const new_worktimetype = {
    name: new_worktimetype_name,
    cost: new_worktimetype_cost
  }
  this.worktimetype.push(new_worktimetype)
}

function handleUpdateWorktimetypes(worktimetype) {

  

  for ( let type of worktimetype) {
    console.log(type.cost)
    console.log(type.name)
    if (typeof type.cost !== 'number' || type.cost < 0) {
      errors.value.push('Błędny koszt pracy. Podaj właściwą liczbę całkowitą')
    }
  }


  if(!errors.value.length) {

    const result = updateWorktimetypes(worktimetype)

    if (result) {
      toast({
            message: `Czasy pracy zaktualizowane poprawnie`,
            duration: 5000,
            position: "top-center",
            type: 'is-success',
            animate: { in: 'backInDown', out: 'backOutUp' },
          })
    }

    else {
      toast({
            message: `Czasy pracy nie zaktualizowane poprawnie`,
            duration: 5000,
            position: "top-center",
            type: 'is-danger',
            animate: { in: 'backInDown', out: 'backOutUp' },
          })
    }
}

  else {
    let msg = ''

    for (let i=0; i <errors.value.length; i++){
      msg += errors.value[i] += "\n"
    }

    toast({
        message: msg,
        duration: 5000,
        position: "top-center",
        type: 'is-danger',
        animate: { in: 'backInDown', out: 'backOutUp' },
      })

      errors.value = []
}

  }
  

</script>

<style>
.modal-prices{
    --bulma-modal-content-width: 20%;
  }

</style>