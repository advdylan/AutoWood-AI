<template>
  <div class="block">
 <div class=columns >
  <div class="column is-full">
 
  
    <div class="notification is-warning">
      <div class="title is-centered is-size-3">
        {{ $t('edit_costs_section') }}     
      </div>
      <div class="text">
        {{ $t('cost_change_info') }}
      </div>
 
  </div>
  </div>
</div>

    <div class="columns is-flex">
        <div class="column is-one-third">
            <div class="card">
                <header class="card-header">
                  <p class="card-header-title is-centered"><i class="fa-solid fa-user"></i>&nbsp; {{ $t('work_costs') }}</p>               
                </header>
                <div class="card-content is-flex is-flex-direction-column" style="height: 100%;">
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
                    <div class="buttons is-flex-align-items-flex-end mt-auto ">
                        <button @click="toggleSaveWindows = !toggleSaveWindows"
                         class="button is-dark"><i class="fa-regular fa-floppy-disk">&nbsp;</i>{{ $t('save') }}</button>  
                        <button @click="toggleAddWorktype = !toggleAddWorktype" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>{{ $t('add') }}</button>   
                        <button @click="toggleDisabled = !toggleDisabled;
                                  if (!toggleDisabled) {
                                    loadData()
                                  }" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>{{ $t('edit') }}</button>                                                  
                    </div>
                </div>
              </div>

        </div>
        <div class="column is-one-third ">

          <div class="card">
            <header class="card-header">
              <p class="card-header-title is-centered"><i class="fa-solid fa-tree">&nbsp;</i>{{ $t('material_costs') }}</p>               
            </header>
            <div class="card-content is-flex is-flex-direction-column" style="height: 100%;">
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
                            <input class="input" type="number" placeholder="bind-to-" v-model=wood_cost.price :disabled="toggleWoodDisabled"/>                                          
                        </div>
                    </div>
                </div>
                <div class="buttons is-flex-align-items-flex-end mt-auto ">
                    <button @click="toggleSaveWindows = !toggleSaveWindows"
                     class="button is-dark "><i class="fa-regular fa-floppy-disk">&nbsp;</i>{{ $t('save') }}</button>  
                    <button @click="toggleAddWood = !toggleAddWood" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>{{ $t('add') }}</button>   
                    <button @click="toggleWoodDisabled = !toggleWoodDisabled;
                            if (!toggleWoodDisabled){
                              loadData()
                            }" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>{{ $t('edit') }}</button>                       
                </div>
            </div>
          </div>
            
        </div>
        <div class="column is-one-third">

          <div class="card">
            <header class="card-header">
              <p class="card-header-title is-centered"> <i class="fa-solid fa-fill-drip fa-lg"></i>&nbsp;{{ $t('paint_costs') }}</p>               
            </header>
            <div class="card-content is-flex is-flex-direction-column" style="height: 100%;">
                <div class="columns">


                    <div class="column is-two-thirds">
                        <div v-for="paint_name in paints" class="field">
                            <div class="control">
                                <input  class="input" type="text" :placeholder="paint_name.name" disabled/>
                            </div>
                        </div>

                    </div>
                    
                    
                    <div class="column">
                        <div v-for="paint_cost in paints" class="field">
                            <input class="input" type="number" placeholder="bind-to-" v-model=paint_cost.cost :disabled="togglePaintDisabled"/>                                          
                        </div>
                    </div>
                    
                </div>
                <div class="buttons is-flex-align-items-flex-end mt-auto ">
                    <button @click="toggleSaveWindows = !toggleSaveWindows"
                     class="button is-dark "><i class="fa-regular fa-floppy-disk">&nbsp;</i>{{ $t('save') }}</button>  
                    <button @click="toggleAddPaint = !toggleAddPaint" class="button is-dark"><i class="fa-solid fa-plus">&nbsp;</i>{{ $t('add') }}</button>   
                    <button @click="togglePaintDisabled = !togglePaintDisabled;
                              if(!togglePaintDisabled){
                                loadData()
                              }" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>{{ $t('edit') }}</button>                       
                </div>
            </div>
          </div>




            
        </div>
    </div>

  </div>


    <div v-bind:class="{'is-active': toggleSaveWindows}" class="modal" style="--bulma-modal-content-width: 30%;">
        <div class="modal-background"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">{{ $t('confirm_changes') }}</p>
            <button @click="toggleSaveWindows = !toggleSaveWindows" class="delete" aria-label="close"></button>
          </header>
          <section class="modal-card-body has-text-centered">
            {{ $t('you_made_changes') }}
            <br>
            {{ $t('do_you_want_to_save') }}
          </section>
          <footer class="modal-card-foot">
            <div class="buttons">
              <button @click="handleUpdateWorktimetypes(worktimetype, wood, paints);
              toggleSaveWindows = !toggleSaveWindows;"     
              class="button is-success"><i class="fa-regular fa-floppy-disk">&nbsp;</i>{{ $t('save') }}</button>
              <button class="button"><i class="fa-solid fa-ban">&nbsp;</i>{{ $t('cancel') }}</button>
              <p class="has-text-left is-size-7">{{ $t('changes_note') }}</p>
              
              <p class="has-text-left is-size-7">{{ $t('only_new_estimates') }}</p>
            </div>
          </footer>
        </div>
      </div>


      <div v-bind:class="{'is-active': toggleAddWorktype}" class="modal" style="--bulma-modal-content-width: 30%;">
        <div class="modal-background"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">{{ $t('add_new_section') }}</p>
            <button @click="toggleAddWorktype = !toggleAddWorktype" class="delete" aria-label="close"></button>
          </header>
          <section class="modal-card-body has-text-centered">

           <div class="card-content">
            <div class="columns">
                <div class="column is-half">
                    <label  class="label">{{ $t('section_name') }}</label>
                    <input v-model="new_worktimetype_name" class="input" type="text" :placeholder="$t('section_name')" />
                </div>
                <div class="column">
                    <label class="label">{{ $t('hourly_cost') }}</label>
                    <input v-model="new_worktimetype_cost" class="input" type="number" :placeholder="$t('hourly_cost')" />
                </div>
            </div>
        </div>
          </section>
          <footer class="modal-card-foot">
            <div class="buttons">
              <button
              @click="addNewWorktimetype(new_worktimetype_name,new_worktimetype_cost);
                      toggleAddWorktype = !toggleAddWorktype" class="button is-success"><i class="fa-regular fa-floppy-disk">&nbsp;</i>{{ $t('save') }}</button>
              <button class="button"><i class="fa-solid fa-ban">&nbsp;</i>{{ $t('cancel') }}</button>
              <p class="has-text-left is-size-7">{{ $t('changes_note') }}</p>
              
              <p class="has-text-left is-size-7">{{ $t('only_new_estimates') }}</p>
            </div>
          </footer>
        </div>
      </div>

      <div v-bind:class="{'is-active': toggleAddWood}" class="modal" style="--bulma-modal-content-width: 30%;">
        <div class="modal-background"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">{{ $t('add_new_woodtype') }}</p>
            <button @click="toggleAddWood = !toggleAddWood" class="delete" aria-label="close"></button>
          </header>
          <section class="modal-card-body has-text-centered">

           <div class="card-content">
            <div class="columns">
                <div class="column is-half">
                    <label  class="label">{{ $t('wood_type') }}</label>
                    <input v-model="new_wood_name" class="input" type="text" :placeholder="$t('wood_type')" />
                </div>
                <div class="column">
                    <label class="label">{{ $t('material_cost') }}</label>
                    <input v-model="new_wood_cost" class="input" type="number" :placeholder="$t('material_cost')" />
                </div>
            </div>
        </div>
          </section>
          <footer class="modal-card-foot">
            <div class="buttons">
              <button
              @click="addNewWood(new_wood_name,new_wood_cost);
              toggleAddWood = !toggleAddWood;
              "
              class="button is-success"><i class="fa-solid fa-plus">&nbsp;</i>{{ $t('add') }}
              </button>
              <button @click="toggleAddWood = !toggleAddWood" class="button"><i class="fa-solid fa-ban">&nbsp;</i>{{ $t('cancel') }}</button>
              <p class="has-text-left is-size-7">{{ $t('changes_note') }}</p>
              
              <p class="has-text-left is-size-7">{{ $t('only_new_estimates') }}</p>
            </div>
          </footer>
        </div>
      </div>


      <div v-bind:class="{'is-active': toggleAddPaint}" class="modal" style="--bulma-modal-content-width: 30%;">
        <div class="modal-background"></div>
        <div class="modal-card">
          <header class="modal-card-head">
            <p class="modal-card-title">{{$t('add_new_paint')}}</p>
            <button @click="toggleAddPaint = !toggleAddPaint" class="delete" aria-label="close"></button>
          </header>
          <section class="modal-card-body has-text-centered">

           <div class="card-content">
            <div class="columns">
                <div class="column is-one-third">
                    <label  class="label">{{$t('paint_name')}}</label>
                    <input v-model="new_paint_name" class="input" type="text" :placeholder="$t('paint_name')" />
                </div>
                <div class="column">
                    <label class="label">{{$t('material_cost')}}</label>
                    <input v-model="new_paint_cost" class="input" type="number" :placeholder="$t('material_cost')" />
                </div>
                <div class="column">
                  <label class="label">{{$t('volume')}}</label>
                  <input v-model="new_paint_volume" class="input" type="number" :placeholder="$t('volume')" />
              </div>
            </div>
        </div>
          </section>
          <footer class="modal-card-foot">
            <div class="buttons">
              <button
              @click="addNewPaint(new_paint_name,new_paint_cost,new_paint_volume);
              toggleAddPaint = !toggleAddPaint;
              "
              class="button is-success"><i class="fa-solid fa-plus">&nbsp;</i>{{$t('add')}}
              </button>
              <button @click="toggleAddPaint = !toggleAddPaint" class="button"><i class="fa-solid fa-ban">&nbsp;</i>{{$t('cancel')}}</button>
              <p class="has-text-left is-size-7">{{$t('changes_note')}}</p>
              
              <p class="has-text-left is-size-7">{{$t('only_new_estimates')}}</p>
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
import {ref, onMounted} from 'vue';
import { toast } from 'bulma-toast';

const toggleDisabled = ref(true)
const toggleWoodDisabled = ref(true)
const togglePaintDisabled = ref(true)
const toggleSaveWindows = ref(false)
const toggleAddWorktype = ref(false)
const toggleAddWood = ref(false)
const toggleAddPaint = ref(false)
const new_worktimetype_name = ref('')
const new_worktimetype_cost = ref('')
const new_wood_cost = ref('')
const new_wood_name = ref('')
const new_paint_cost = ref('')
const new_paint_name = ref('')
const new_paint_volume = ref('')
const errors = ref([])

const temporaryWorktimetypes = ref()

//MAIN STORE
const mainstore = useNewProjectStoreBeta()

const {loadData} = mainstore
const {worktimeCost, worktimetype, wood, paints} = storeToRefs(mainstore)

//PRICE SETUP STORE
const pricesstore = usePricesSetup()

const {updateWorktimetypes} = pricesstore
const {newWorktimeCost} = storeToRefs(pricesstore)

onMounted(() => {
  loadData()
})


function addNewWorktimetype(new_worktimetype_name, new_worktimetype_cost) {
  const new_worktimetype = {
    name: new_worktimetype_name,
    cost: new_worktimetype_cost
  }
  worktimetype.value.push(new_worktimetype)
}

function addNewWood(new_wood_name, new_wood_cost){

  if (typeof new_wood_name !== 'string' || new_wood_name.trim === ''){
    errors.value.push('Podaj właściwą nazwę')
  }

  if (typeof new_wood_cost !== 'number' || new_wood_cost <= 0) {
    errors.value.push('Podaj właściwy koszt materiału')
  }

  if(!errors.value.length) {
    const new_wood = {
    name: new_wood_name,
    density: 670,
    price: String(new_wood_cost)
  }

  wood.value.push(new_wood)

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

function addNewPaint(new_paint_name, new_paint_cost,new_paint_volume){

if (typeof new_paint_name !== 'string' || new_paint_name.trim === ''){
  errors.value.push('Podaj właściwą nazwę')
}

if (typeof new_paint_cost !== 'number' || new_paint_cost <= 0) {
  errors.value.push('Podaj właściwy koszt materiału')
}

if(!errors.value.length) {
  const new_paint = {
  name: new_paint_name,
  cost: new_paint_cost,
  volume: String(new_paint_volume)
}

paints.value.push(new_paint)

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

function handleUpdateWorktimetypes(worktimetype, wood,paints) {

  for ( let type of worktimetype) {
    //console.log(type.cost)
    //console.log(type.name)

    if (typeof type.cost !== 'number' || type.cost < 0) {
      errors.value.push('Błędny koszt pracy. Podaj właściwą liczbę całkowitą')
    }
  }

 /*
  for (let new_wood of wood) {
    //console.log(new_wood.name)
    //console.log(new_wood.price)

    if (typeof Number(parseFloat(new_wood.price)) !== 'number' || Number(parseFloat(new_wood.price)) < 0) {
      errors.value.push('Błędny koszt nowego materiału. Podaj właściwą liczbę całkowitą')
    }

  }
    */


  if(!errors.value.length) {      

    let updatedData = {
      worktimetype: worktimetype,
      wood: wood,
      paints: paints
    }
    console.log(updatedData)
    const result = updateWorktimetypes(updatedData)
    

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