<template>
  <div class="box">
    <form @submit.prevent="submitForm">
                
                <nav class="level">
              <div class="field">
                <label class="label has-text-centered">X</label>
                <div class="control">
                  <input class="input is-small"  v-model="newBoard.board.dimX">           
                </div>
              </div>
    
              <div class="field">
                <label class="label has-text-centered">Y</label>
                <div class="control">
                  <input class="input is-small" v-model="newBoard.board.dimY" >             
                </div>
              </div>
    
              <div class="field">
                <label class="label has-text-centered">Z</label>
                <div class="control">
                  <input class="input is-small"   v-model="newBoard.board.dimZ">             
                </div>
              </div>
    
              <div class="field">
                <label class="label has-text-centered">{{ $t("quantity")}}</label>
                <div class="control">
                  <input class="input is-small"   v-model="newBoard.quantity" >             
                </div>
              </div>
    
              <div class="field">
                <label class="label has-text-centered">{{ $t("wood_type")}}</label>
                <div class="control">
                  <div class="select is-small">
                    <select v-model="newBoard.board.wood_type">
                      <option v-for="woodItem in wood" :key="woodItem.id" :value="woodItem">
                        {{ woodItem.name }}
                      </option>
                    </select>
                  </div>
                </div>
              </div>
    
                <div class="field" style="padding-top: 1.15rem;">
                  <button type="submit"  class="button is-success is-small"><i class="fa-solid fa-plus"></i></button>
               
                </div>
                </nav>    
              
          </form>
        </div>

      
<div class="section" v-if="filteredBoards.length">
  <label class="label has-text-centered is-size-5">Zasoby</label>
  

      <b-table :key="tableKey" :data="filteredBoards">
      <b-table-column >
        <template #default="props">
          <input :class="{
            'input is-small': filteredBoards,
            'input is-small active': checkForRows(props.row)
          }"  v-model="props.row.dimX"/>
        </template> 
      </b-table-column>
    
      <b-table-column >
        <template #default="props">
          <input :class="{
            'input is-small': filteredBoards,
            'input is-small active': checkForRows(props.row)
          }"  v-model="props.row.dimY"/>
        </template> 
      </b-table-column>
      
      <b-table-column >
        <template  #default="props">
          <input :class="{
            'input is-small': filteredBoards,
            'input is-small active': checkForRows(props.row)
          }"  v-model="props.row.dimZ"/>
        </template> 
      </b-table-column>
    
      <b-table-column >
        <template #default="props">    
            <input :class="{
            'input is-small': filteredBoards,
            'input is-small active': checkForRows(props.row)
          }"  v-model="props.row.wood_type.name" disabled />
        </template>  
      </b-table-column>
    
      <b-table-column >
        <template #default="props">
          <input :class="{
            'input is-small': filteredBoards,
            'input is-small active': checkForRows(props.row)
          }"  v-model="props.row.quantity" />
        </template> 
      </b-table-column>
    
      <b-table-column >
        <template #default="props">
          <b-button @click="handleDeleteButton(props.row)" type="is-danger is-small" icon-left="x">    
          </b-button>
        </template>
      </b-table-column>
    </b-table>                            
    </div>

</template>
<script setup>
import { ref, watch } from "vue";
import { useNewProjectStoreBeta } from '@/store/newproject'
import { useI18n } from 'vue-i18n';
import { storeToRefs } from 'pinia';
import { toast } from 'bulma-toast';

const store = useNewProjectStoreBeta()
const { boards,wood, warehouseBoards,filteredBoards, highlightedRows} = storeToRefs(store)
const {addWarehouseBoard} = store
const errors = ref([])
const tableKey = ref(0)
const previousWarehouseBoards = ref([])
const timeoutIDs = ref(null)

const newBoard = ref({
          board: {
          dimX: 2500,
          dimY: 700,
          dimZ: 25,
          wood_type: ''
          },
          quantity: 1
    })

function checkForRows(props) {
  for (const board of highlightedRows.value) {
    if (
      props.name === board.name &&
      props.wood_type === board.wood_type &&
      props.dimX === board.dimX &&
      props.dimY === board.dimY &&
      props.dimZ === board.dimZ &&
      props.quantity === board.quantity
    ) {
      return true
    }
  }
  return false
}

const submitForm = () => {

console.log(newBoard)

if (newBoard.value.board.dimX <= 0) {
errors.value.push('Podaj długość większą niż 0')
}

if (newBoard.value.board.dimY <= 0) {
errors.value.push('Podaj wysokość większą niż 0')
}
if (newBoard.value.board.dimZ <= 0) {
errors.value.push('Podaj grubość większą niż 0')
}
console.log(newBoard.value.board.wood_type)
if (newBoard.value.board.wood_type == '') {
errors.value.push('Wybierz materiał')
}

if (!errors.value.length) {
addWarehouseBoard(newBoard.value)

newBoard.value = {
board: {
    dimX: 2200,
    dimY: 800,
    dimZ: 25,
    wood_type: ''
        },
quantity: 1
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


function saveWarehouseBoard(boards) {

 
  let timeoutID = setTimeout(function() {
    console.log(`Update of warehouse fired. Value :${JSON.stringify(boards)}`)
  }, 3000)

  if (timeoutIDs.value === timeoutID) {
    clearTimeout(timeoutID)
  }
  timeoutIDs.value = timeoutID
}

watch(warehouseBoards, (newList) => {
  console.log(`Newlist detected in warehouseboards, calling saveWarehouseBoards`)

  if (!previousWarehouseBoards.value.length) {
    console.log("First fire, do not save")
  }
  else {
    for (let newObject of newList) {
      let oldObject = previousWarehouseBoards.value.find(board => board.id === newObject.id)

      if (oldObject) {
        if (oldObject.quantity !== newObject.quantity) {
        console.log(`Changes detected in quantity of oldObject: ${oldObject.name} ${oldObject.quantity} to newObject${newObject.name} ${newObject.quantity}`)
        saveWarehouseBoard(newList)
      }
      }
    }
  }

  previousWarehouseBoards.value = JSON.parse(JSON.stringify(newList))


 
}, {deep: true})

</script>
<style lang="css" scoped>

.input.active {
  background-color: rgb(158, 225, 103);

}



</style>