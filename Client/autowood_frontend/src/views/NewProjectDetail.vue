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

                <div class="card-content">               
                  <div class="content">
                    <div class="field">
                      <label class="label is-size-5">Nazwa projektu</label>
                      <div class="control">
                        <input v-model="projectName" class="input" type="text" placeholder="Nazwa projektu">
                      </div>
                    </div>
  
                    <div class="field">
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
                       

            </div>
          </div>
        </div>
        

        <div class="column is-one-third">
          <ElementsTable v-if="detail_project"  :elements="detail_project.elements"></ElementsTable>
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
  import { onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import ElementsTable from '@/components/ElementsTable'
  import NewProject from './NewProject.vue'

  const route = useRoute()
  const id = route.params.id
  
  const ProjectsListStore = useProjectsListStore()
  const elementStore = useNewProjectStoreBeta()


  const { loadDetailProject, } = ProjectsListStore
  const {projectlist, detail_project} = storeToRefs(ProjectsListStore)
  
  
  loadDetailProject(id)




  </script>
  
  
  
  