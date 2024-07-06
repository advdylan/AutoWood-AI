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

                  <b-button type="is-primary" >
                    <i class="fa-solid fa-floppy-disk"></i>
                    Zapisz zmiany
                  </b-button>

                  <b-button type="is-danger" >
                    <i class="fa-solid fa-trash"></i>
                    Usuń projekt
                  </b-button>
                  <b-button class="button is-dark"><i class="fa-regular fa-file">&nbsp;</i>Raport dla klienta</b-button>
                  <b-button @click="submitForm" class="button is-dark"><i class="fa-regular fa-file">&nbsp;</i>Rozpiska</b-button>
                  

                  </div>   
            </div>
            
          </div>
        </div>
        

        <div class="column is-one-third">

          <ElementsTable v-if="detail_project"  :elements="detail_project.elements"></ElementsTable>

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
  
                  <th>{{ akc.name }}</th>
                  <td>{{ akc.type }}</td>
                  <td>{{ akc.weight }}</td>
                  <td>{{ akc.price }}</td>

                </tr>
                
              </tbody>
              
            </table>

        </div>
        </div>

        
    
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
  import { ref } from 'vue'
  import { useRoute } from 'vue-router'
  import ElementsTable from '@/components/ElementsTable'
  import NewProject from './NewProject.vue'

  const projectName = ref()
  const selectedWood = ref()
  const selectedCategory = ref()
  const selectedCollection = ref()
  const selectedPaint = ref()

  const route = useRoute()
  const id = route.params.id
  
  const ProjectsListStore = useProjectsListStore()
  const elementStore = useNewProjectStoreBeta()


  const { loadDetailProject,} = ProjectsListStore

  const {loadData} = elementStore
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


  async function submitForm() {
                  const formData = detail_project.value
                  
              }

</script>


  
  
  
  