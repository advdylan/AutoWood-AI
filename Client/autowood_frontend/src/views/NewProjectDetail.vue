<template>
  <div class="card">
    <header class="card-header">
      <p v-if="detail_project" class="card-header-title is-centered is-size-4">Wycena zamówienia "{{ detail_project.name}}"</p>
    </header>
    <div class="card-content">
      <div class="columns">

        <div class="column is-two-third">
          <div class="card">
            <div class="card-header">
              <p class="card-header-title is-size-5">Szczegóły</p>
            </div>
              <div class="card-content">
                <div class="columns">
                  <div class="column is-one-third">
         
                  <div class="content">
                    <div class="field">
                      <label class="label is-size-5">Nazwa projektu</label>
                      <div class="control">
                        <input v-model="projectName" class="input" type="text" placeholder="Nazwa projektu">
                      </div>
                    </div>
  
                    <div class="field" v-if="selectedWood">
                      <label class="label is-size-5">Materiał</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="selectedWood">
                            <option v-for="woodItem in wood"> {{ woodItem.name }}</option>
                          </select>
                        </div>
                      </div>
                    </div>
  
                    <div class="field">
                      <label class="label is-size-5">Kategoria</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="selectedCategory">
                            <option v-for="categoryItem in category"> {{ categoryItem.name }}</option>
                          </select>
                        </div>
                      </div>
                    </div>
  
                    <div class="field">
                      <label class="label is-size-5">Kolekcja</label>
                      <div class="control">
                        <div class="select">
                          <select v-model="selectedCollection">
                          <option v-for="collection in collection"> {{ collection.name }}</option>
                          </select>
                        </div>
                      </div>
                      </div>
  
                      <div class="field">
                        <label class="label is-size-5">Malowanie</label>
                        <div class="control">
                          <div class="select">
                            <select v-model="selectedPaint">
                              <option v-for="paints in paints">{{ paints.name}}</option>
                            </select>
                            
                          </div>                   
                        </div>                      
                      </div>     
                      
                    </div>   
                    
                  </div>  
                  <div class="column is-one-third">

                    <div class="elements-table-container">
                      <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                        <thead>
                          <tr>
                            <th>Marża</th>
                            <th>Koszt</th>
                            
                          </tr>
                
                        </thead>
                        <tfoot>
                          
                          <tr>
                            
                          </tr>

                        </tfoot>
                        <tbody v-if="detail_project">
                          
                            <tr>
                              <th>Marża na akcesoria</th>
                                <td>{{ detail_project.accesories_margin}}  zł   
                                </td>
                            </tr>

                            <tr>
                              <th>Marża materiałowa</th>
                              <td>{{ detail_project.elements_margin }} zł</td>
                            </tr>

                            <tr>
                              <th>Dodatkowa marża</th>
                              <td>{{ detail_project.additional_margin}} zł</td>
                            </tr>
                          
                        </tbody>
                        
                      </table>
                    </div>
                    <hr class="dashed">
                    <div class="container">
                      <table class="table is-bordered is-striped is-hoverable is-fullwidth">
                        <thead>
                          <tr>
                            <th>Dział</th>
                            <th>Koszt</th>
                            
                          </tr>
                
                        </thead>
                        <tfoot>
                          
                          <tr>
                            
                          </tr>

                        </tfoot>
                        <tbody>
                          
                          <tr v-if="detail_project" v-for="worktime in detail_project.worktimes">
            
                            <th>{{ worktime.name}}</th>
                            <td>{{ worktime.cost}} zł</td>
                          </tr>
                          
                        </tbody>
                        
                      </table>
                    </div>                
                  </div> 

                </div>  
                <div class="buttons">

                  <b-button @click="submitUpdateForm" type="is-success" >
                    <i class="fa-solid fa-floppy-disk"></i>
                    Zapisz zmiany
                  </b-button>

                  <b-button type="is-danger" >
                    <i class="fa-solid fa-trash"></i>
                    Usuń projekt
                  </b-button>
                  <b-button class="button is-info"><i class="fa-regular fa-file">&nbsp;</i>Raport dla klienta</b-button>
                  <b-button  class="button is-info"><i class="fa-regular fa-file">&nbsp;</i>Wygeneruj rozpiskę</b-button>
                  <button @click="showEditModal = true" data-target="newelement-modal" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj marżę i koszty pracy</button>

                  

                  </div>   
            </div>
            
          </div>
        </div>
        

        <div class="column is-one-third">
          <div class="card">
            <header class="card-header" @click="isCollapsedelements = !isCollapsedelements">
              <p class="card-header-title is-size-5">
                Lista elementów
              </p>
            </header>
              <div class="card-content">


         
          <ElementsTable v-if="detail_project"  :elements="detail_project.elements"></ElementsTable>
          </div>
          

          <div class="buttons">
            <button class="button is-dark" @click="showElementModal = true" data-target="newelement-modal"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj tabelę</button>
        
          </div>
          
          </div>



          <hr class="dashed">

          <div class="container-cost">
            <table class="table is-bordered is-striped is-hoverable is-fullwidth">
              <thead>
                <tr>
                  <th>Nazwa</th>
                  <th>Typ</th>
                  <th>Waga</th>
                  <th>Cena</th>
                  
                </tr>
      
              </thead>
              <tfoot>
                
                <tr>
                  
                </tr>

              </tfoot>
              <tbody>
                
                <tr v-if="detail_project" v-for="akc in detail_project.accessories">
  
                  <th>{{ akc.type.name }}</th>
                  <td>{{ akc.type.type }}</td>
                  <td>{{ akc.type.weight }}</td>
                  <td>{{ akc.type.price }}</td>

                </tr>
                
              </tbody>
              
            </table>
            <button @click="showAccModal = true" data-target="newelement-modal" class="button is-dark"><i class="fa-regular fa-pen-to-square">&nbsp;</i>Edytuj listę akcesorii</button>
        </div>

        <div v-bind:class="{'is-active': showAccModal}" id="newelement-modal" class="modal">
          <div class="modal-background"></div>
          <div class="modal-content">
      
            <div class="modal-card">
              <header class="modal-card-head">
                    <p class="modal-card-title is-centered is-size-3">Akcesoria</p>
                    <button class="delete" aria-label="close" @click="showAccModal = false"></button>        
                  </header>
                  <section class="modal-card-body">
                    <AccessoryTable v-if="detail_project" :propsAccesories="detail_project.accessories" addAccDetail="one"  />
                  </section>
          </div>
          </div>
        </div>
        </div>

        
    
    </div>
</div>
</div>





<div v-bind:class="{'is-active': showElementModal}" id="newelement-modal" class="modal">
  <div class="modal-background"></div>
  <div class="modal-content">


    <div class="modal-card">
      <header class="modal-card-head">
            <p class="modal-card-title is-centered is-size-3">Dodaj element</p>
            <button class="delete" aria-label="close" @click="showElementModal = false"></button>        
          </header>
          
      
      <section class="modal-card-body">
        <div class="columns">
          <div class="column is-two-fifths">

        <form @submit.prevent="submitForm">

        <div class="field">
          <label class="label">Nazwa</label>
          <div class="control">
            <input class="input" type="text" placeholder="Nazwa" v-model="newElement.element.name">             
          </div>
        </div>

        <div class="field">
          <label class="label">Długość</label>
          <div class="control">
            <input class="input" type="number" placeholder="Długość" v-model="newElement.element.dimX">           
          </div>
        </div>

        <div class="field">
          <label class="label">Szerokość</label>
          <div class="control">
            <input class="input" type="number" placeholder="Szerokosć" v-model="newElement.element.dimY" >             
          </div>
        </div>

        <div class="field">
          <label class="label">Grubość</label>
          <div class="control">
            <input class="input" type="number" placeholder="Grubość" v-model="newElement.element.dimZ">             
          </div>
        </div>

        <div class="field">
          <label class="label">Ilość</label>
          <div class="control">
            <input class="input" type="number" placeholder="Ilość" v-model="newElement.quantity" >             
          </div>
        </div>

        <div class="field">
          <label class="label">Materiał</label>
          <div class="control">
            <div class="select">
              <select v-model="newElement.element.wood_type">
                <option v-for="woodItem in wood" :key="woodItem.id" :value="woodItem">
                  {{ woodItem.name }}
                </option>
              </select>
            </div>
          </div>
        </div>

      <footer class="modal-card-foot">
        <div class="buttons">
          <button type="submit" class="button is-success">Dodaj element</button>
         
        </div>
      </footer>
      

    </form>
  </div>
  <div class="column">
    <ElementsTable v-if="detail_project" :elements="detail_project.elements" />
  </div>
  </div>

  </section>

  </div>
  </div>


</div>

<div v-bind:class="{'is-active': showEditModal}" id="newelement-modal" class="modal">
  <div class="modal-background"></div>
  <div class="modal-content">

    <div class="modal-card">
      <header class="modal-card-head">
            <p class="modal-card-title is-centered is-size-3">Marże i koszty pracy</p>
            <button class="delete" aria-label="close" @click="showEditModal = false"></button>        
          </header>
          <section class="modal-card-body">
            <Summary v-if="detail_project" 
            :propMarginA="Number(parseFloat(detail_project.percent_elements_margin).toFixed(2))"
            :propMarginB="Number(parseFloat(detail_project.percent_accesories_margin).toFixed(2))"
            :propMarginC="Number(parseFloat(detail_project.percent_additional_margin).toFixed(2))"
            :propElements="detail_project.elements"
            :propAccesories="detail_project.accessories"
            :propWorktimecosts="detail_project.propWorktimecosts" >

            
                      
            </Summary>
          </section>
          
      
  </div>
  </div>


</div>
   
    
</template>
  
  <script>
  export default {
    name: 'NewProjectDetail'
  }
  
  </script>
  
  <script setup>
  import { useNewProjectStoreBeta } from '@/store/newproject'
  import { useProjectsListStore } from '@/store/projectslist'
  import { storeToRefs } from 'pinia'
  import { ref, watchEffect, onUnmounted } from 'vue'
  import { useRoute } from 'vue-router'
  import ElementsTable from '@/components/ElementsTable'
  import AccessoryTable from '@/components/AccessoryTable.vue'
  import NewProject from './NewProject.vue'
  import Summary from '@/components/Summary.vue'

  const projectName = ref()
  const selectedWood = ref()
  const selectedCategory = ref()
  const selectedCollection = ref()
  const selectedPaint = ref()
  const showElementModal = ref(false)
  const showAccModal = ref(false)
  const showEditModal = ref(false)

  const newElement = ref({
  element: {
    name: 'Przód',
    dimX: 2500,
    dimY: 250,
    dimZ: 25,
    wood_type: ''
  },
  quantity: 1
})

  const route = useRoute()
  const id = route.params.id
  
  const ProjectsListStore = useProjectsListStore()
  const elementStore = useNewProjectStoreBeta()


  const { loadDetailProject, updateProject, addElement} = ProjectsListStore

  const {loadData, $reset } = elementStore
  loadData()


  const {detail_project} = storeToRefs(ProjectsListStore)
  const {elements, wood, collection, paints, category, boxes, accesories} = storeToRefs(elementStore)

  loadDetailProject(id).then(() => {
  if (detail_project.value) {
    projectName.value = detail_project.value.name
    selectedWood.value = detail_project.value.wood.name
    selectedCategory.value = detail_project.value.category.name
    selectedCollection.value = detail_project.value.collection.name
    selectedPaint.value = detail_project.value.paints.name
  }
})

const submitForm = () => {
  addElement(newElement.value);
  newElement.value = {
    element: {
      name: '',
      dimX: 0,
      dimY: 0,
      dimZ: 0,
      wood_type: ''
    },
    quantity: 0
  };
};


  async function submitUpdateForm() {
        const formData = {

          id: id,
          name: projectName.value,
          category: selectedCategory.value,
          wood: selectedWood.value,
          collection: selectedCollection.value,
          paints: selectedPaint.value,
          elements_margin: detail_project.value.elements_margin,
          accesories_margin: detail_project.value.accesories_margin,
          additional_margin: detail_project.value.additional_margin,
          summary_with_margin: detail_project.value.summary_with_margin,
          summary_without_margin: detail_project.value.summary_without_margin,
          elements: detail_project.value.elements,
          worktime: boxes.value,
          accessories: detail_project.value.accessories,
          
  }

  console.log('Form Data before sending:', formData)
                                
  updateProject(id, formData)

              }

  onUnmounted(()=> {
    console.log("Unmount the NewProjectDetail")
    $reset()
  })

  

</script>


  
  
  
  